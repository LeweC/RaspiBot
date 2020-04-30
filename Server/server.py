import asyncio
import websockets

async def hello(websocket, path):
    async for message in websocket:
        print(f"< {message}")

        greeting = f"Hello {message}!"

        await websocket.send(greeting)
        print(f"> {greeting}")

start_server = websockets.serve(hello, "192.168.178.112", 8001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()