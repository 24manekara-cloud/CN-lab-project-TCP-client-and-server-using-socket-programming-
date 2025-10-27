import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.2', 9999))
server.listen(5)

print("Server started. Waiting for client connection...")

while True:
    client_socket, address = server.accept()
    print(f"Connected with {address}")

    data = client_socket.recv(1024).decode()
    print("Received from client:", data)

    if data.lower() == "exit":
        client_socket.send("Goodbye!".encode())
        client_socket.close()
        print("Client requested exit. Closing server...")
        break

    # Send response back to client
    response = f"Server Received: {data}"
    client_socket.send(response.encode())

    client_socket.close()

server.close()
