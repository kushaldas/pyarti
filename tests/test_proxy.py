import time
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
    assert proxy.is_alive()
    # Now let us kill it
    proxy.kill()
    time.sleep(1)
    assert not proxy.is_alive()


def test_different_port():
    "Tests a different port than default"
    proxy = OnionProxy(9000)
    assert proxy.verify(blocking=True)
    transport = SyncProxyTransport.from_url("socks5://127.0.0.1:9000")
    with httpx.Client(transport=transport) as client:
        res = client.get("https://www.torproject.org")
        assert res.status_code == 200
