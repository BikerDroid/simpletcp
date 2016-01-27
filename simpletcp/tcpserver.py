from simpletcp.serversocket import ServerSocket

class TCPServer:
    def __init__(self, mode, port):
        self.serversocket = ServerSocket(mode, port)

    def run(self):
        self.serversocket.run()

    @property
    def ip(self):
        return self.serversocket.ip

    @property
    def port(self):
        return self.serversocket.port
