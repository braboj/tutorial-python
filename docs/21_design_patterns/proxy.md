# proxy

```python
# Example: Proxy Pattern

class Server(object):

    def request(self):
        raise NotImplementedError


class RealServer(Server):

    def request(self):
        print("RealServer: Handling request.")


class ProxyServer(Server):

    def __init__(self, server: Server = None):
        self._server = server

    def request(self):
        if self.check_access():
            self._server.request()
            self.log_access()

    @staticmethod
    def check_access():
        print("ProxyServer: Checking access prior to firing a real request.")
        return True

    @staticmethod
    def log_access():
        print("ProxyServer: Logging the time of request.", end="")


class Client(object):

    def __init__(self, server: Server):
        self._server = server

    def execute(self):
        self._server.request()


if __name__ == "__main__":

    print("Client: Executing the client code with a real server")
    real_server = RealServer()
    client = Client(server=real_server)
    client.execute()

    print("")

    print("Client: Executing the same client code with a proxy server")
    client = Client(server=ProxyServer(real_server))
    client.execute()
```
