import socket
import time


HOST = '10.92.1.61'
PORT = 14000


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


client_time = time.time()
client_socket.send(str(client_time).encode())
server_time = float(client_socket.recv(1024).decode())


time_difference = server_time - client_time
print(f"client time: {client_time}")
print(f"Server time: {server_time}")
print(f"Time difference: {time_difference} seconds")


client_socket.close()