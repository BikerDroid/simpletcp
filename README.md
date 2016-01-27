# simpleTCP
simpleTCP is a minimal non-blocking TCP server written for Python 3.

### Installation

simpleTCP is written in pure Python 3. It has no external dependencies. To install,

1. Clone the repository: `git clone https://github.com/gragas/simpletcp`
2. Install the package: `python3 setup.py install`

### Quick Start

simpleTCP just requires that you specify:

* the mode (local or public) of your server
* the port of your server
* what happens when your server receives data

For example, here's an echo server:

```
from simpletcp.tcpserver import TCPServer

def echo(queue, data):
    queue.put(data)

server = TCPServer("localhost", 5000, echo)
server.run()
```

#### Callback functions

`echo` is the server's callback function. This function is called whenever the server receives data.

Callback functions should take two arguments:

1. `queue`: This is a `queue.Queue` object. Any data put into this queue will be asynchronously sent back to the socket it was received from. In this case, our server echoes all data it receives, so we just put all received data right back into this queue with `queue.put(data)`.
2. `data`: This is the data that the server received. It is a string of bytes. Its type is `bytes`.

#### The `TCPServer` itself

The `TCPServer` constructor takes three arguments:

1. The `mode`. There are two valid `modes`: `"localhost"` and `"public"`. They are aptly named --- `"localhost"` means run the server on `127.0.0.1`. Therefore, the server is only visible on the machine on which it is running. `"public"` means run the server on `0.0.0.0` --- make it visible to anything that can see the machine on which it is running.
2. The port. For development, pick a high (four-digit) number.
3. The callback function. This function is called whenever the server receives data.

### Examples

Examples can be found in the `/examples` folder.

# Contributing

### License

Apache Version 2. It looks the coolest.

### Original Author and Maintainer

Thomas Fischer
