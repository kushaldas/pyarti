API
===


.. class:: OnionProxy() -> None:

        Returns an OnionProxy which opens up a SOCKS5 proxy on port 9150. It sends termination signal to the child process when the object is garbage collected.

    .. method:: pid() -> int:

        Returns the PID of the child process running the actual proxy.

    .. method:: kill() -> None:

        Kills the child proxy process.

    .. method:: terminate() -> None:

        Sends the termination signal to the child proxy process.

    .. method:: verify(url: str="https://www.torproject.org", blocking: bool=False) -> bool:

        Verifies that the proxy is working. If we pass `blocking=True`, then for the next 30 seconds it will
        try to access the given URL and sleeps for 1 second in case it can not.
