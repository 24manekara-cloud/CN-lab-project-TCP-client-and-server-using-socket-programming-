import socket
import time
    # Create a new socket each time
while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

        client.connect(('127.0.0.2', 9999))
        message=input("Enter message to send to the server:")

    # Send the list
        client.sendall(message.encode())

    # Receive response
        response = client.recv(1024).decode()
        print("Response from server:", response)

    # Close socket
        client.close()
        if message.lower() == 'exit':
            break

    # Optional delay to avoid flooding the server
