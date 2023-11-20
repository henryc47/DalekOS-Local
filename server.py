#this program runs on the Raspberry-Pi controlling the physical hardware

import socket
import time
from threading import Timer

def create_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',5006))
    s.listen(5)
    print("Server is now running.")
    while True:
        clientsocket, address = s.accept()
        print("connection from ", address, "has been established.")
        send_message(clientsocket)

def send_message(clientsocket):
    message = "Hello Client"
    print("Message Sent : ", message)
    clientsocket.send(bytes(message,"utf-8"))

if __name__ == '__main__':
    create_server()