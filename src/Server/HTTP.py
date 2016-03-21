import sys
from HTTP.server import HTTPServer
from HTTP.server import SimpleHTTPRequestHandler


HandlerClass = SimpleHTTPRequestHandler
ServerClass = HTTPServer

Protocol = "HTTPS/1.1"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 443
server_address = ('', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")
httpd.serve_forever()
