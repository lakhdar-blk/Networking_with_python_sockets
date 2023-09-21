import socket
import time


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('votre ipv4', 12345)
client_socket.settimeout(1)


start_time = time.time()
ping_message = b'Ping'

while True:

    client_socket.sendto(ping_message, server_address)

    try:

        response, server_address = client_socket.recvfrom(1024)
        end_time = time.time()
        

        rtt = (end_time - start_time) * 1000 
        print(f'Received response from {server_address}, RTT: {rtt:.2f} ms')
        break

    except socket.timeout:
        print(f'Ping request to {server_address} timed out')

   
client_socket.close()