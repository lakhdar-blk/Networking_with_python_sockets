import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('votre ipv4', 12345)
server_socket.bind(server_address)

print('UDP server is listening on {}:{}'.format(*server_address))

while True:

    # recever les données envoyer par un client
    data, client_address = server_socket.recvfrom(1024)
    
    print('Received data from {}: {}'.format(client_address, data.decode()))

    # envoyer une réponse au client
    response = 'Hello, client!'
    server_socket.sendto(response.encode(), client_address)