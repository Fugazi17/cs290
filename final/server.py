import http.server
import socketserver

PORT = 6969
handler = http.server.CGIHTTPRequestHandler

with http.server.HTTPServer(("", PORT), handler) as httpd:
    print(f"Server starting on port {PORT}")
    httpd.serve_forever()