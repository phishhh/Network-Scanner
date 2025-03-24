from scapy.all import ARP, Ether, srp


target_ip = "192.168.1.1/24"


arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC
packet = ether/arp  # Combine Ethernet and ARP layers


result = srp(packet, timeout=3, verbose=0)[0]


devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})


print("IP Address\t\tMAC Address")
print("-----------------------------------------")
for device in devices:
    print(f"{device['ip']}\t\t{device['mac']}")