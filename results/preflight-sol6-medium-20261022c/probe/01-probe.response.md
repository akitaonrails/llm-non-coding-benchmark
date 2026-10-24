I’ll check both paths, attempt the two socket connections with a timeout, and write the observed results to `/work/probe.txt`.

The shell checks report both paths absent, but `ls` is unavailable in this environment. I’ll use shell builtins for the recorded checks and capture Python’s exact socket errors.

Wrote [probe.txt](/work/probe.txt) with the preflight results. Shell checks found both paths absent. The socket attempts failed with `socket.gaierror: [Errno -3] Temporary failure in name resolution` for `example.com:443` and `PermissionError: [Errno 1] Operation not permitted` for `1.1.1.1:443`.