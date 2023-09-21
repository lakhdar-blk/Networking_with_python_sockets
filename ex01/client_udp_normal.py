import socket
import time


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('votre ipv4', 12345)
client_socket.settimeout(1)

ping_message = b'Ping'


seq = 4

while True:
    
    # envoie d'une requete ping
    start_time = time.time()
    client_socket.sendto(ping_message, server_address)

    try:
        # recoive une réponse envoyer par le serveur
        response, server_address = client_socket.recvfrom(1024)
        end_time = time.time()
        
        # Calculer le (RTT)
        rtt = (end_time - start_time) * 1000  
        print(f'Received response from {server_address}, RTT: {rtt:.2f} ms')

    except socket.timeout:

        print(f'Ping request to {server_address} timed out')

    seq = seq - 1
    if seq == 0:
        break

# fermé la connection
client_socket.close()