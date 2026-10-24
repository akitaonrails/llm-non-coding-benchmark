import unittest
from unittest.mock import Mock, patch
import guard_gpu_reserve as guard


class ReserveTests(unittest.TestCase):
    @patch('guard_gpu_reserve.subprocess.Popen')
    @patch('guard_gpu_reserve.free_mib', return_value=3000)
    def test_refuses_launch_below_floor(self, telemetry, launch):
        with patch('sys.argv', ['guard', '--', 'server']), self.assertRaises(SystemExit):
            guard.main()
        launch.assert_not_called()

    @patch('guard_gpu_reserve.time.sleep')
    @patch('guard_gpu_reserve.os.killpg')
    @patch('guard_gpu_reserve.subprocess.Popen')
    @patch('guard_gpu_reserve.free_mib', side_effect=[5000, 3000])
    def test_breach_stops_only_owned_group(self, telemetry, launch, kill, sleep):
        child = Mock(pid=123456)
        child.poll.return_value = None
        launch.return_value = child
        with patch('sys.argv', ['guard', '--', 'server']), self.assertRaises(RuntimeError):
            guard.main()
        self.assertTrue(launch.call_args.kwargs['start_new_session'])
        self.assertEqual([c.args[0] for c in kill.call_args_list], [123456, 123456])
        child.wait.assert_called_once()

    @patch('guard_gpu_reserve.time.sleep')
    @patch('guard_gpu_reserve.os.killpg')
    @patch('guard_gpu_reserve.subprocess.Popen')
    @patch('guard_gpu_reserve.free_mib', side_effect=[5000, RuntimeError('telemetry unavailable')])
    def test_telemetry_failure_stops_owned_group(self, telemetry, launch, kill, sleep):
        child = Mock(pid=123456)
        child.poll.return_value = None
        launch.return_value = child
        with patch('sys.argv', ['guard', '--', 'server']), self.assertRaises(RuntimeError):
            guard.main()
        self.assertEqual([c.args[0] for c in kill.call_args_list], [123456, 123456])


if __name__ == '__main__':
    unittest.main()
