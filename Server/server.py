import asyncio
import websockets
import main
import camera

handler = None
direction = ""
counter = 0
stream = False
instructions = ["empty", "empty", "off"]

@asyncio.coroutine
async def hello(websocket, path):
    async for message in websocket:
        try:
            print(f"< {message}")
            global instructions
            global counter 
            if counter == 3:            #[0] = Moving direction [1]= Ultrasonic sensor angle [2]= camera angle
                counter = 0
            instructions[counter] = message
            counter = counter + 1
            print(instructions)
        except KeyboardInterrupt:
            print("Ending Scipt")
    
@asyncio.coroutine
def mainloop():
    while True:
        main.handler(instructions)
        yield from asyncio.sleep(0.2)

start_server = websockets.serve(hello, handler, 80, ping_interval=None)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.ensure_future(mainloop())
asyncio.get_event_loop().run_forever()
