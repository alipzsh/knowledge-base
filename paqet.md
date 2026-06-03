- interface and local IP:  ip a
- Find Gateway MAC:
    * gateway's IP: ip r | grep default
    * MAC address: arp -n <gateway_ip> (e.g., arp -n 192.168.1.1).
