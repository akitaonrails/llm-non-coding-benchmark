import http.client
import http.server
import json
from pathlib import Path
import socket
import tempfile
import threading
import unittest

from run_local_baseline import Gateway, UnixServer, sandbox


class UnixConnection(http.client.HTTPConnection):
    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(self.host)


class GatewayTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = str(Path(self.temp.name) / 'gateway.sock')
        self.server = UnixServer(self.path, Gateway)
        self.server.model = 'selected-model'
        self.worker = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.worker.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.temp.cleanup()

    def request(self, method, path, payload=None):
        conn = UnixConnection(self.path)
        conn.request(method, path, json.dumps(payload) if payload else None)
        response = conn.getresponse()
        data = response.read()
        status = response.status
        conn.close()
        return status, data

    def test_model_listing_is_fixed(self):
        status, data = self.request('GET', '/v1/models')
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(data)['data'][0]['id'], 'selected-model')

    def test_no_arbitrary_routes(self):
        self.assertEqual(self.request('GET', '/api/pull')[0], 403)
        self.assertEqual(self.request('POST', '/api/chat', {'model': 'selected-model'})[0], 403)

    def test_no_other_models(self):
        self.assertEqual(self.request('POST', '/v1/chat/completions', {'model': 'other'})[0], 403)

    def test_no_remote_image_fetch(self):
        body = {'model': 'selected-model', 'messages': [{'content': [{'type': 'image_url', 'image_url': {'url': 'http://example.com'}}]}]}
        self.assertEqual(self.request('POST', '/v1/chat/completions', body)[0], 403)

    def test_namespace_has_no_host_network_or_home(self):
        command = sandbox(Path('/case'), Path('/state'), Path('/socket'), Path('/config'))
        self.assertIn('--unshare-all', command)
        self.assertNotIn('--share-net', command)
        self.assertNotIn('/home/akitaonrails', command)

    def test_forwarding_preserves_sse_and_records_final_usage(self):
        received = []
        stream = b'data: {"choices":[{"finish_reason":"stop"}],"usage":{"prompt_tokens":10,"completion_tokens":2}}\n\ndata: [DONE]\n\n'

        class Upstream(http.server.BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_POST(self):
                received.append(json.loads(self.rfile.read(int(self.headers['Content-Length']))))
                self.send_response(200)
                self.send_header('Content-Type', 'text/event-stream')
                self.end_headers()
                self.wfile.write(stream)

        upstream = http.server.HTTPServer(('127.0.0.1', 0), Upstream)
        thread = threading.Thread(target=upstream.serve_forever, daemon=True)
        thread.start()
        self.server.host, self.server.port = upstream.server_address
        self.server.metrics = Path(self.temp.name) / 'metrics.jsonl'
        try:
            status, data = self.request('POST', '/v1/chat/completions', {'model': 'selected-model', 'stream': True, 'messages': []})
            self.assertEqual((status, data), (200, stream))
            self.assertEqual(received[0]['stream_options'], {'include_usage': True})
            self.assertEqual(received[0]['max_tokens'], 16384)
            record = json.loads(self.server.metrics.read_text())
            self.assertEqual(record['finish_reason'], 'stop')
            self.assertEqual(record['usage']['completion_tokens'], 2)
            for requested, expected in [(8, 8), (20000, 16384)]:
                status, _ = self.request('POST', '/v1/chat/completions',
                    {'model': 'selected-model', 'stream': True, 'messages': [], 'max_completion_tokens': requested})
                self.assertEqual(status, 200)
                self.assertEqual(received[-1]['max_tokens'], expected)
                self.assertNotIn('max_completion_tokens', received[-1])
        finally:
            upstream.shutdown()
            upstream.server_close()


if __name__ == '__main__':
    unittest.main()
