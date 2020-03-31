import websocket

from .model import Request


class Client:

    def __init__(self, *, host: str = "localhost", port: int = 8880, path: str = "/websockets/service"):
        self.ws = websocket.WebSocket()
        self.ws.connect(f"ws://{host}:{port}{path}")
        self.ws.send("client")

    def send(self, request: Request):
        schema = getattr(request, '__schema__')
        json = schema.dumps(request)
        print(json)
        self.ws.send(json)

    def close(self):
        self.ws.close()
