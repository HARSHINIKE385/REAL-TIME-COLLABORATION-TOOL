import asyncio
import websockets
import json

DOCUMENT = {"text":"// Collaborative document\nStart typing...\n", "version": 0}
clients = set()

async def broadcast_state():
    if not clients: return
    message = json.dumps({"type":"full","text":DOCUMENT["text"],"version":DOCUMENT["version"]})
    await asyncio.gather(*(ws.send(message) for ws in clients))

async def handler(ws):
    clients.add(ws)
    try:
        await ws.send(json.dumps({"type":"full","text":DOCUMENT["text"],"version":DOCUMENT["version"]}))
        async for message in ws:
            msg = json.loads(message)
            if msg.get("type") == "patch" and msg.get("version") == DOCUMENT["version"]:
                DOCUMENT["text"] = msg["text"]
                DOCUMENT["version"] += 1
                await broadcast_state()
            else:
                await ws.send(json.dumps({"type":"full","text":DOCUMENT["text"],"version":DOCUMENT["version"]}))
    finally:
        clients.remove(ws)

async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765):
        print("Server running at ws://127.0.0.1:8765")
        await asyncio.Future()  # run forever

asyncio.run(main())
