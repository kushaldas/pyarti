import time
import subprocess
from typing import Optional

import httpx
from httpx_socks import SyncProxyTransport


class OnionProxy:
    def __init__(
        self,
    ):
        args = ["python", "-m", "pyarti"]
        self.child: subprocess.Popen = subprocess.Popen(args, stdout=subprocess.PIPE)

    def pid(self) -> int:
        """Returns the PID of the running proxy process."""
        return self.child.pid

    def terminate(self) -> None:
        """Terminates the child process."""
        self.child.terminate()

    def kill(self) -> None:
        "Kills the child proxy process."
        self.child.kill()

    def verify(self, url="https://www.torproject.org", blocking=False) -> bool:
        """Verifies if the proxy is working or not. For 30 seconds it keeps trying to access the url, and
        sleeps 1 second in between.

        :param url: str, default is https://www.torproject.org.
        :param blocking: Boolean, it is False by default.

        :returns: True/False based if the proxy is working.

        """
        transport = SyncProxyTransport.from_url("socks5://127.0.0.1:9150")
        with httpx.Client(transport=transport) as client:
            result = False
            for _ in range(30):
                try:
                    res = client.get(url)
                    if res.status_code == 200:
                        result = True
                        break
                except:
                    result = False
                    if not blocking:
                        return result
                # Sleep for 1 second
                time.sleep(1)
            # Now return anyway
            return result

    def __del__(self):
        "Makes sure that we terminate the proxy process"
        self.terminate()
