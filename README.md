# pyarti

It is a Python module to allow creating of SOCKS5 proxy using [Arti](https://gitlab.torproject.org/tpo/core/arti/) project from the [Tor Project](https://www.torproject.org).

## How to build?

First install [Rustup toolchain](https://rustup.rs) for your user.

### Build dependencies in Fedora

```
sudo dnf install python3-devel openssl-devel
```

### Build dependencies in Debian Bullseye

```
sudo apt install -y python3-dev python3-pip python3-venv


```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python setup.py develop
```

For a release build use the following command.

```
python setup.py bdist_wheel
`````
