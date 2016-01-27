from simpletcp.tcpserver import TCPServer

server = TCPServer("localhost", 5000)
server.run()
