import queue
from simpletcp.tcpserver import TCPServer

def echoreverse(queue, data):
    queue.put(bytes("".join([chr(b) for b in list(reversed(data))]), "UTF-8"))

server = TCPServer("localhost", 5000, echoreverse)
server.run()
