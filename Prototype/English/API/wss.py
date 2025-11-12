import websocket
import ssl
import time
import threading
import json

class SocketIOClient:
    def __init__(self, url):
        self.url = url
        self.ws = None
        self.stop_ping = False

    def on_message(self, ws, message):
        print("Received:", message)

        # Xử lý PING từ server (engine.io type "2")
        if message == "2":
            print("→ Sending PONG")
            ws.send("3")  # PONG

        # Xử lý sự kiện Socket.IO (bắt đầu bằng "4")
        if message.startswith("42"):
            try:
                payload = message[2:]
                event = json.loads(payload)
                print("Event parsed:", event)
            except Exception as e:
                print("Parse error:", e)

    def on_error(self, ws, error):
        print("Error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("### Connection closed ###")
        self.stop_ping = True

    def on_open(self, ws):
        print("### WebSocket connected ###")
        ws.send("40")  # Gửi connect đến namespace mặc định

        # Bắt đầu thread gửi PING định kỳ
        self.stop_ping = False
        threading.Thread(target=self.send_ping, daemon=True).start()

    def send_ping(self):
        while not self.stop_ping:
            time.sleep(20)  # Gửi trước khi timeout (pingInterval = 25s)
            try:
                print("→ Sending PING")
                self.ws.send("2")
            except:
                break

    def run(self):
        headers = {
            "Origin": "https://learn.eltngl.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
        }
        self.ws = websocket.WebSocketApp(
            self.url,
            header=headers,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

# === MAIN ===
socket_id = "_XLlUUgBl9_xI2Wro7-7D"
ws_url = f"wss://0.artico.dev/socket.io/?id={socket_id}&EIO=4&transport=websocket"

client = SocketIOClient(ws_url)
client.run()