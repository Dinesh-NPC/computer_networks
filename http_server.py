from http.server import SimpleHTTPRequestHandler, HTTPServer
# Define the server's address and port
host = "localhost"
port = 8000
# Create and start the server
server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Server running on http://{host}:{port}")
server.serve_forever()
