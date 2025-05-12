import socket
# Hostname to IP lookup
hostname = "google.com"
ip_address = socket.gethostbyname(hostname)
print(f"IP Address of {hostname}: {ip_address}")
#Reverse DNS
host = socket.gethostbyaddr(ip_address)
print(f"Hostname for {ip_address}: {host[0]}")
