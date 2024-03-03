import http.server
import socketserver
import threading
import signal
import time

PORT = 8000
SERVER_DURATION_SECONDS = None  # Set to None to run until manually stopped
RETRY_INTERVAL_SECONDS = 5  # Configurable retry interval
MAX_RETRIES = 10  # Maximum number of retry attempts

handler = http.server.SimpleHTTPRequestHandler
httpd = None  # Declare httpd as a global variable
retry_flag = True  # Flag to control whether to retry starting the server
intentional_stop = False  # Flag to check whether the server was stopped intentionally

def run_server():
    global httpd, intentional_stop
    retries = 0

    while retry_flag and retries < MAX_RETRIES:
        try:
            with socketserver.TCPServer(("", PORT), handler) as server:
                httpd = server  # Assign server to the global httpd variable
                print("Server started at localhost:" + str(PORT))
                server.serve_forever()

        except OSError as e:
            if "Address already in use" in str(e):
                if intentional_stop:
                    print("Server stopped intentionally.")
                    break
                else:
                    print(f"Address {PORT} is already in use. Retrying in {RETRY_INTERVAL_SECONDS} seconds...")
                    retries += 1
                    time.sleep(RETRY_INTERVAL_SECONDS)
            else:
                print(f"Error: {e}")
                break

def stop_server(signum, frame):
    global httpd, retry_flag, intentional_stop
    if httpd:
        # Stop the server by shutting down the server socket
        print("Stopping the server...")
        httpd.shutdown()
        httpd.server_close()  # Close the server socket
        print("Server stopped.")
        retry_flag = False  # Set the flag to exit the retry loop
        intentional_stop = True  # Set the flag to indicate intentional stop
        exit()

# Register the signal handler for graceful shutdown
signal.signal(signal.SIGINT, stop_server)
signal.signal(signal.SIGTERM, stop_server)

# Start the server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.start()

if SERVER_DURATION_SECONDS is not None:
    # Wait for the specified duration
    print(f"Server will run for {SERVER_DURATION_SECONDS} seconds.")
    time.sleep(SERVER_DURATION_SECONDS)
    stop_server(signal.SIGINT, None)  # Stop the server after the specified duration

# If SERVER_DURATION_SECONDS is None, run until manually stopped
server_thread.join()