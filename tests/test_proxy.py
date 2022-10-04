from pyarti import OnionProxy

import httpx
from httpx_socks import SyncProxyTransport


def test_proxy():
    proxy = OnionProxy()
    assert proxy.verify(blocking=True)
    transport = SyncProxyTransport.from_url("socks5://127.0.0.1:9150")
    with httpx.Client(transport=transport) as client:
        res = client.get("https://github.com")
        assert res.status_code == 200
