import asyncio
import websockets

async def hello(websocket, path):
    async for message in websocket:
        print(f"< {message}")

        if message == "Standing":
            greeting = f"{message}!"
        else:
            greeting = f"Moving {message}!"
            await websocket.send(greeting)
            print(f"> {greeting}")
    
        
    

start_server = websockets.serve(hello, "192.168.178.112", 8001, ping_interval=20)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()