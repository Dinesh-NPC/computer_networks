import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
server.bind(server_address)
server.listen(1)
print("Waiting for a connection...")
connection, client_address = server.accept()
print("Connection established with", client_address)
try:
    while True:
        data = connection.recv(1000).decode()
        if not data:
            print("Client disconnected.")
            break
        print("Client:", data)
        message = input("You: ")
        connection.sendall(message.encode())
        if message.lower() == "end":
            print("Closing connection...")
            break
finally:
    connection.close()
    server.close()
