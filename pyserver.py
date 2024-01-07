import http.server
import socketserver
import threading
import time

PORT = 8000
SERVER_DURATION_SECONDS = 300  # Set the duration for the server to run (in seconds)

handler = http.server.SimpleHTTPRequestHandler
httpd = None  # Declare httpd as a global variable

def run_server():
    global httpd
    with socketserver.TCPServer(("", PORT), handler) as server:
        httpd = server  # Assign server to the global httpd variable
        print("Server started at localhost:" + str(PORT))
        server.serve_forever()

# Start the server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.start()

try:
    # Wait for the specified duration
    time.sleep(SERVER_DURATION_SECONDS)
finally:
    if httpd:
        # Stop the server by shutting down the server socket
        httpd.shutdown()
        httpd.server_close()  # Close the server socket
        print("Server stopped after {} seconds.".format(SERVER_DURATION_SECONDS))