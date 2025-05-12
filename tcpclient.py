import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
client.connect(server_address)
print("Connected to server at", server_address)
try:
    while True:
        message = input("You: ")
        client.sendall(message.encode())
        if message.lower() == "end":
            print("Closing connection...")
            break
        data = client.recv(1000).decode()
        if not data:
            print("Server disconnected.")
            break
        print("Server:", data)
finally:
    client.close()
