import json
import websocket
import threading
import time
import requests
import subprocess
import os
import signal

class CDPDriver:
    """
    Direct websocket communicator for Chrome DevTools Protocol.
    This avoids relying on heavy CDP wrapper dependencies.
    """
    def __init__(self, port=9222):
        self.port = port
        self.ws = None
        self.msg_id = 1
        self.responses = {}
        self.events = []
        self._browser_process = None
        self.connected_event = threading.Event()

    def start_chrome(self, headless=False):
        # We need a robust way to find/start Chrome across platforms.
        # For Windows, typically it's in Program Files.
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if not os.path.exists(chrome_path):
            chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        
        args = [
            chrome_path,
            f"--remote-debugging-port={self.port}",
            "--remote-allow-origins=*",
            "--user-data-dir=C:\\Temp\\pyquality_profile" # Temporary profile
        ]
        
        if headless:
            args.append("--headless")
            args.append("--disable-gpu")
            args.append("--no-sandbox")
        
        self._browser_process = subprocess.Popen(args)
        time.sleep(2) # Give it time to start

    def stop_chrome(self):
        if self._browser_process:
            self._browser_process.send_signal(signal.SIGTERM)
            
    def _on_open(self, ws):
        self.connected_event.set()

    def _on_error(self, ws, error):
        print(f"WebSocket Error: {error}")

    def _on_close(self, ws, close_status_code, close_msg):
        print("WebSocket Closed")

    def connect(self):
        # Fetch the websocket debugger URL
        url = f"http://127.0.0.1:{self.port}/json"
        
        # Add a retry logic in case Chrome takes time to open the port
        response = None
        for _ in range(5):
            try:
                response = requests.get(url).json()
                break
            except Exception:
                time.sleep(1)
                
        # We just grab the first page
        if not response:
            raise Exception("No active pages found or CDP port not responding!")
            
        page_ws_url = response[0]['webSocketDebuggerUrl']
        self.ws = websocket.WebSocketApp(
            page_ws_url,
            on_message=self._on_message,
            on_open=self._on_open,
            on_error=self._on_error,
            on_close=self._on_close
        )
        
        # Start receiver thread
        self.connected_event.clear()
        self._thread = threading.Thread(target=self.ws.run_forever, kwargs={"suppress_origin": True})
        self._thread.daemon = True
        self._thread.start()
        
        # Wait up to 5 seconds for the connection to establish
        if not self.connected_event.wait(5):
            raise Exception("Failed to connect to browser websocket within 5 seconds")

    def _on_message(self, ws, message):
        data = json.loads(message)
        if 'id' in data:
            self.responses[data['id']] = data
        else:
            self.events.append(data)

    def send_command(self, method, params=None):
        if params is None:
            params = {}
        
        cmd = {
            "id": self.msg_id,
            "method": method,
            "params": params
        }
        self.ws.send(json.dumps(cmd))
        current_id = self.msg_id
        self.msg_id += 1
        return current_id
        
    def wait_for_response(self, msg_id, timeout=5):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if msg_id in self.responses:
                return self.responses.pop(msg_id)
            time.sleep(0.01)
        raise TimeoutError(f"No response for message {msg_id}")

    def execute_and_wait(self, method, params=None):
        msg_id = self.send_command(method, params)
        return self.wait_for_response(msg_id)
