import asyncio
import websockets
import json
import nest_asyncio
nest_asyncio.apply()

DOCUMENT = {"text": "// Collaborative document\nStart typing...\n", "version": 0}
clients = set()

async def broadcast_state():
    if not clients: 
        return
    message = json.dumps({
        "type": "full",
        "text": DOCUMENT["text"],
        "version": DOCUMENT["version"]
    })
    await asyncio.gather(*(ws.send(message) for ws in clients))

async def handler(ws, path):
    clients.add(ws)
    try:
        await ws.send(json.dumps({"type":"full","text":DOCUMENT["text"],"version":DOCUMENT["version"]}))
        async for message in ws:
            msg = json.loads(message)
            if msg.get("type") == "patch":
                if msg.get("version") == DOCUMENT["version"]:
                    DOCUMENT["text"] = msg["text"]
                    DOCUMENT["version"] += 1
                    await broadcast_state()
                else:
                    await ws.send(json.dumps({"type":"full","text":DOCUMENT["text"],"version":DOCUMENT["version"]}))
            elif msg.get("type")=="request_full":
                await ws.send(json.dumps({"type":"full","text":DOCUMENT["text"],"version":DOCUMENT["version"]}))
    finally:
        clients.remove(ws)

async def start_ws_server(host='0.0.0.0', port=8765):
    print(f"Starting WebSocket server on {host}:{port}")
    server = await websockets.serve(handler, host, port)
    return server

# Run server
PORT = 8765
loop = asyncio.get_event_loop()
ws_server = loop.run_until_complete(start_ws_server('0.0.0.0', PORT))
print(f"WebSocket server running at ws://0.0.0.0:{PORT}")
