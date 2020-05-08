import asyncio
import websockets
import main
direction = ""

async def hello(websocket, path):
    async for message in websocket:
        try:
            global direction
            direction = message
            print(f"< {message}")
            if message == "Standing":
                greeting = f"{message}!"
                print(f"> {greeting}")
                
                await websocket.send(greeting)
            else:
                greeting = f"Moving {message}!"
                print(f"> {greeting}")
                await websocket.send(greeting)
        except KeyboardInterrupt:
            print("Ending Scipt")

async def eventhandler(direction):
    print("Wurde ausgeführt")
    main.moving(direction)    
    
start_server = websockets.serve(hello, "192.168.178.112", 8001, ping_interval=None)

asyncio.get_event_loop().run_until_complete(start_server)
hello, eventhandler = asyncio.get_event_loop().run_forever()