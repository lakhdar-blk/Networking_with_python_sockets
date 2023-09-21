import socket
import time


HOST = '10.92.29.200'
PORT = 14000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server listening on {HOST}:{PORT}")

while True:
    
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")


    server_time = time.time()
    client_socket.send(str(server_time).encode())
    client_time = float(client_socket.recv(1024).decode())

    time_difference = server_time - client_time
    print(f"Time difference: {time_difference} seconds")

    client_socket.close()