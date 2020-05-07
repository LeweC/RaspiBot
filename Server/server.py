import main
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.178.112", 8001))
s.listen(10)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes(f"Connection from has been established.","utf-8"))
    while True:
        msg = s.accept(1024)
        
        clientsocket.send(bytes(msg,"utf-8"))