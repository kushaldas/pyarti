import subprocess
from typing import Optional

from .pyarti import start_proxy


class TProxy:
    def __init__(
        self,
    ):
        args = ["python", "-m", "pyarti"]
        self.child: subprocess.Popen = subprocess.Popen(args, stdout=subprocess.PIPE)

    def pid(self) -> int:
        return self.child.pid

    def terminate(self) -> None:
        self.child.terminate()

    def kill(self) -> None:
        self.child.kill()
