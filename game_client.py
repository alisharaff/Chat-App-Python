import socket
 #
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)
print('Connected to server:', server_address)

try:
    while True:
        # Get user input
        message = input('Enter a message ("quit" to exit): ')

        # Send the message to the server
        client_socket.send(message.encode())

        if message == 'quit':
            break

        # Receive the response from the server
        response = client_socket.recv(1024).decode()

        # Print the response
        print('Server response:', response)

finally:
    # Close the connection
    client_socket.close()
