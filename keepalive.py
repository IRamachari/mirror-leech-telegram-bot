from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run():
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()

threading.Thread(target=run, daemon=True).start()
