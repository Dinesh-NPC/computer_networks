from scapy.all import ARP, Ether, srp
target_ip = "192.168.231.108" # Change this to the target IP in your network
# Create an ARP request
arp_request = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff") # Broadcast request
packet = ether / arp_request
# Send the packet and receive response
result = srp(packet, timeout=2, verbose=False)[0]
# Extract and print MAC address
for sent, received in result:
    print(f"IP Address: {received.psrc} | MAC Address: {received.hwsrc}")
#pip install scapy
#run "arp -a" to get the targetip
#run "python arp.py"
