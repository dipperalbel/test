import http.server
import socketserver
import json

# Define the handler for your server
class JSONHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Create a JSON response
        response_data = {'hi': 'world'}
        response_json = json.dumps(response_data)

        # Send the JSON response
        self.wfile.write(response_json.encode('utf-8'))

# Set the port you want to use (e.g., 8000)
port = 8000

# Create the server
with socketserver.TCPServer(("", port), JSONHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()