from .pyarti import start_proxy

if __name__ == "__main__":
    port = input("provide port number:")
    port = port.strip("\r\n")
    start_proxy(port)
