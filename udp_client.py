import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
while True:
    message = input("Enter message: ")

    client.sendto(message.encode(), server_address)
    if message.lower() == "end":
        print("Closing client...")
        break
    data, _ = client.recvfrom(1024)
    print("Server:", data.decode())
client.close()
