import queue
from simpletcp.tcpserver import TCPServer

def echo(ip, queue, data):
    queue.put(data)

server = TCPServer("localhost", 5000, echo)
server.run()
