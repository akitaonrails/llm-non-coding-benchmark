import io
import json
import unittest
from unittest.mock import patch

from probe_decode import probe


class DecodeProbeTests(unittest.TestCase):
    def test_reasoning_and_content_stream_share_decode_clock(self):
        chunks = [
            {'choices': [{'delta': {'role': 'assistant'}}]},
            {'choices': [{'delta': {'reasoning_content': 'Think'}}]},
            {'choices': [{'delta': {'content': 'Answer'}}]},
            {'choices': [{'finish_reason': 'length'}], 'usage': {'completion_tokens': 501}},
        ]
        stream = io.BytesIO(b''.join(b'data: ' + json.dumps(c).encode() + b'\n\n' for c in chunks) + b'data: [DONE]\n')
        with patch('probe_decode.urllib.request.urlopen', return_value=stream), \
             patch('probe_decode.time.monotonic', side_effect=[0, 2, 7, 8]):
            result = probe('http://localhost:8000', 'test')
        self.assertEqual(result['ttft_seconds'], 2)
        self.assertEqual(result['decode_tokens_per_second'], 100)
        self.assertEqual(result['seconds'], 8)
        self.assertEqual(result['finish_reason'], 'length')

    def test_empty_output_has_no_speed(self):
        stream = io.BytesIO(b'data: {"choices": [], "usage": {"completion_tokens": 0}}\n\ndata: [DONE]\n')
        with patch('probe_decode.urllib.request.urlopen', return_value=stream):
            result = probe('http://localhost:8000', 'test')
        self.assertIsNone(result['decode_tokens_per_second'])


if __name__ == '__main__':
    unittest.main()
