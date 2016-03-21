import sys
from HTTP.server import HTTPServer
from HTTP.server import SimpleHTTPRequestHandler
import HTTP.cookiejar
import HTTP.cookies
import socket
import ssl

class SecureHTTPServer(HTTPServer):

    def __init__(self, server_address, HandlerClass, RequestHandlerClass):
        BaseServer.__init__(self, server_address, HandlerClass)
        super().__init__(server_address, RequestHandlerClass)
        HTTPServer.socket = ssl.wrap_socket(HTTPServer.socket)  # TODO: Finish this. 

        self.server_bind()
        self.server_activate()


class SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    def setup(self):
        self.connection = self.request
        # Convert to python 3


def test(HandlerClass = SecureHTTPRequestHandler,
         ServerClass = SecureHTTPServer):
    server_address = ('', 443)
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsocname()
    print("serving HTTPS on %s port %s", sa[0], sa[1])

    httpd.serve_forever()

if __name__ == '__main__':
    test()
#
# HandlerClass = SimpleHTTPRequestHandler
# ServerClass = HTTPServer
#
# Protocol = "HTTPS/1.1"
#
# if sys.argv[1:]:
#     port = int(sys.argv[1])
# else:
#     port = 443
# server_address = ('', port)
#
# HandlerClass.protocol_version = Protocol
# httpd = ServerClass(server_address, HandlerClass)
#
# sa = httpd.socket.getsockname()
# print("Serving HTTP on", sa[0], "port", sa[1], "...")
# httpd.serve_forever()
