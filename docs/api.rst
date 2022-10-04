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


Example usage
==============

Below is an example where are creating the proxy and then calling the **verify** method to make sure that we have a working proxy.


::

    from pyarti import OnionProxy
    import httpx
    from httpx_socks import SyncProxyTransport
    p = OnionProxy()
    assert p.verify(blocking=True)
    # Now we can use the proxy
    transport = SyncProxyTransport.from_url("socks5://127.0.0.1:9150")
    with httpx.Client(transport=transport) as client:
        res = client.get("https://github.com")
        assert res.status_code == 200




Or, you can manually call the verify method too, here we are sleeping for 5 seconds between each call.

::

    p = OnionProxy()
    while not p.verify():
        time.sleep(5)
    ...

