Simple Network Scanner using scapy library and python
Devices use ARP(Address Resolution Protocol) to map IP address to mac address
BY sending an arp requests all devices in the subnet reply with their IP address and MAC address

Ether() creates an ehternet frame which is layer 2 - physical layer (OSI Model)
ARP(pdst=target_ip) is literally saying who has this ip address
srp() send this requests and listens for responses

Written by phishhh, only scan networks you own or have permission to scan
