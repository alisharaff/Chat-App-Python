import socket
#server
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Waiting for a client to connect...')

# Accept a client connection
client_socket, client_address = server_socket.accept()
print('Client connected:', client_address)

try:
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()

        # Process the received data
        if data == 'quit':
            break

        # Send a response back to the client
        response = 'Received: ' + data
        client_socket.send(response.encode())

finally:
    # Close the connection
    client_socket.close()
    server_socket.close()
