import socket
from threading import *
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1) 

def ping_client(server_address, ping_message, client):
    
    seq = 4

    while True:

        start_time = time.time()
        client_socket.sendto(ping_message.encode(), server_address)

        try:
            response, _ = client_socket.recvfrom(1024)
            end_time = time.time()
            rtt = (end_time - start_time) * 1000 
            print(f'Received response from {server_address}, RTT: {rtt:.2f} ms (for client {client})')
        except socket.timeout:
            print(f'Ping request to {server_address} timed out (for client {client})')

        seq = seq - 1

        if seq == 0:
            break


server_address = ('votre ipv4', 12345)
ping_message = 'Ping'


"""
while True:
    Thread(target=ping_client, args=(server_address, ping_message),).start()
"""



import threading


num_clients = 10

threads = []
for _ in range(num_clients):
    thread = threading.Thread(target=ping_client, args=(server_address, ping_message, _))
    threads.append(thread)


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


client_socket.close()
print('All ping requests completed.')


