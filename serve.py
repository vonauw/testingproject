import os
import http.server
import socketserver

os.chdir("/Users/macbookairm2/Downloads/Claudetest")
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
