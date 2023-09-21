import socket
from threading import *
import time


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('votre ipv4', 12345)
client_socket.settimeout(1)

start_time = time.time()
ping_message = b'Ping'


def ping_client(server_address, ping_message, client):

    while True:

        client_socket.sendto(ping_message, server_address)

        try:

            response, server_address = client_socket.recvfrom(1024)
            end_time = time.time()
            
            rtt = (end_time - start_time) * 1000  
            print(f'Received response from {server_address}, RTT: {rtt:.2f} ms (for client {client})')
            break
        
        except socket.timeout:
            print(f'Ping request to {server_address} timed out (for client {client})')


"""while True:
    Thread(target=ping_client, args=(server_address, ping_message),).start()
    print('All ping requests completed.')
"""


import threading
num_clients = 5


threads = []
for _ in range(num_clients):
    thread = threading.Thread(target=ping_client, args=(server_address, ping_message, _))
    threads.append(thread)


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

print('All ping requests completed.')

client_socket.close()