#this program runs on the Raspberry-Pi controlling the physical hardware

import socket
import time

def create_server():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket uses IPv4 IP addresses and TCP protocol
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #ensure we can reuse the socket
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('',30701)) #bind socket to localhost, port 30699
    server.listen(5) #backlog = 5, only one client may connect to this server at a time
    print("Server is now running. Waiting for client to connect . . .")
    client_socket, client_address = server.accept() #wait for a connection from a client
    print("Accepted connection from ",client_address[0],":",client_address[1])
    while True:
        request = client_socket.recv(1024)
        request = request.decode('utf-8')
        print("recieved message : ",request)
        if request=="exit":
            send_message(client_socket,"exited")
            break
        else:
            send_message(client_socket,"accepted")
    
    #server has finished
    server.close()
    client_socket.close()
    print("connection to client closed, turning off server . . .")
    
def send_message(client_socket,message):
    print("Message Sent : ", message)
    client_socket.send(bytes(message,"utf-8"))


if __name__ == '__main__':
    create_server()
