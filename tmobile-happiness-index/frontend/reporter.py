import http.server
import socketserver
import json
import cgi

# --- 1. CONFIGURATION ---
PORT = 8001

class MyReportHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple request handler that listens for POST requests and
    prints the JSON payload.
    """
    
    def _send_response(self, status_code, message):
        """Helper to send a JSON response."""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        # Add CORS headers to allow requests from any origin
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))

    def do_POST(self):
        """
        Handles incoming POST requests. This is where your
        agent_listener.py will send its data.
        """
        try:
            # 1. Read the length of the incoming data
            content_length = int(self.headers['Content-Length'])
            
            # 2. Read the data itself (it comes in as bytes)
            post_data_bytes = self.rfile.read(content_length)
            
            # 3. Decode the bytes to a string and parse it as JSON
            post_data_json = json.loads(post_data_bytes.decode('utf-8'))
            
            # 4. --- THIS IS THE GOAL ---
            # Print the received report beautifully to the console
            print("\n" + "="*50)
            print(f"✅ RECEIVED REPORT at {time.strftime('%H:%M:%S')}")
            print("="*50)
            print(json.dumps(post_data_json, indent=2))
            print("="*50 + "\n")
            
            # 5. Send a "200 OK" success response back to the agent
            self._send_response(200, {"status": "ok", "message": "Report received"})
        
        except Exception as e:
            print(f"❗️ Error processing POST request: {e}")
            self._send_response(500, {"status": "error", "message": str(e)})

    def do_OPTIONS(self):
        """
        Handles OPTIONS pre-flight requests, which browsers
        might send. This is good practice for a server.
        """
        self._send_response(200, {"status": "ok"})

def run_server():
    """
    Starts the server on the specified PORT.
    """
    try:
        # We use socketserver.TCPServer to create the server
        with socketserver.TCPServer(("", PORT), MyReportHandler) as httpd:
            print(f"--- 🚀 Report Server START ---")
            print(f"Listening on http://localhost:{PORT} for incoming reports...")
            
            # Keep the server running until you stop it (Ctrl+C)
            httpd.serve_forever()
            
    except OSError:
        print(f"--- ❗️ COULD NOT START SERVER on port {PORT}. Is it already in use? ---")
    except KeyboardInterrupt:
        print("\n--- 🛑 Report Server Stopped ---")

if __name__ == "__main__":
    import time # Import here since it's only used for printing
    run_server()