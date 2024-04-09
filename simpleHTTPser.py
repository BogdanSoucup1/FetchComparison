from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      time.sleep(3)
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.end_headers()
      self.wfile.write(b"Hello, World!")
host = 'localhost'
port = 8080
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

print(f"Server running at http://{host}:{port}")
server.serve_forever()