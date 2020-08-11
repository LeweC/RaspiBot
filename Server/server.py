import asyncio
import websockets
import main
import camera
handler = None
direction = ""
counter = 0
stream = False

@asyncio.coroutine
async def hello(websocket, path):
    async for message in websocket:
        try:
            print(f"< {message}")
            global direction 
            if message == "Standing":
                greeting = f"{message}!"
                print(f"> {greeting}")
                direction = message
                await websocket.send(greeting)

            elif message == "CameraStart":
                stream = True
                greeting = f"{message}!"
                print(f"> {greeting}")
                direction = message
                await websocket.send(greeting)

            elif message == "CameraStop":
                stream = False
                greeting = f"{message}!"
                print(f"> {greeting}")
                direction = message
                await websocket.send(greeting) 
                  

            else:
                greeting = f"Moving {message}!"
                print(f"> {greeting}")
                direction = message
                await websocket.send(greeting)
        except KeyboardInterrupt:
            print("Ending Scipt")
    


@asyncio.coroutine
def mainloop():
    while True:
        print("---" + direction)
        main.moving(direction)
        yield from asyncio.sleep(0.2)

start_server = websockets.serve(hello, handler, 80, ping_interval=None)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.ensure_future(mainloop())
asyncio.get_event_loop().run_forever()
