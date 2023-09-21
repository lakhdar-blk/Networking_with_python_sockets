import socket
import random


host = "votre ipv4"
port = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print(f"Server listening on {host}:{port}")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Received data from {addr}: {data.decode('utf-8')}")

    # répondre avec une probabilité de 0.5
    if random.random() < 0.5:
        print("Server forgot to respond to this request.")
    else:
        
        response = "Server response"
        server_socket.sendto(response.encode('utf-8'), addr)
        print(f"Sent response to {addr}: {response}")