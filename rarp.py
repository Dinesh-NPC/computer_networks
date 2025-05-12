from scapy.all import RARP, Ether, srp
target_mac = " 02-8b-53-06-ce-0a " # Replace with a real MAC address
# Create RARP request
rarp_request = RARP(hwsrc=target_mac)
ether = Ether(dst="ff:ff:ff:ff:ff:ff") # Broadcast request
packet = ether / rarp_request
# Send the packet and receive response
result = srp(packet, timeout=2, verbose=False)[0]
# Extract and print IP address
for sent, received in result:
    print(f"MAC Address: {received.hwsrc} | IP Address: {received.psrc}")
