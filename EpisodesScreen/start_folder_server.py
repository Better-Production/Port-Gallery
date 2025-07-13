import os
import http.server
import socketserver
import threading

# Set the path to the folder you want to open and serve
FOLDER_PATH = r"C:\Users\brand\OneDrive\Desktop\my-church-roku-app\mcra\EpisodesScreen\video_server"  # <-- Change this to your folder
PORT = 8000  # or any free port

def open_folder():
    os.startfile(FOLDER_PATH)

def start_server():
    os.chdir(FOLDER_PATH)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()

# Open the folder
open_folder()

# Start server in a new thread so it doesn't block
thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()

# Keep script alive
input(f"Server running at http://localhost:{PORT}\nPress Enter to stop...\n")
