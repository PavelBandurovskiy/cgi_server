import sqlite3
from http.server import HTTPServer, CGIHTTPRequestHandler

server_adress = ("localhost", 8000)
http_server = HTTPServer(server_adress, CGIHTTPRequestHandler)
http_server.serve_forever()

# chmod -R a+x .
