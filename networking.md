# networking

* subnet (IP network, or just network): a network interconnecting host
  and router interfaces forms a subnet.
* interface: The boundary between the host and the physical link.
* each interface has it's own IP address.
* IP address is technically associated with an interface.
* IP addresses of different interfaces in a network:
  * router: 192.168.1.1, host_1: 192.168.1.51, host_2: 192.168.1.59
  * this network is a subnet.
  * so the first 24 bits are the same: 192.168.1.0/24 is the subnet
    address. "/24" is the subnet mask.
    [subnet](./subnet.png)

* `arp` resolves MAC to IP, kinda similar to DNS.
* `arp -a` shows the arp table, which maps IPs to their corresponding IPs.

* subnet mask determines the allowed range of IPs in the network; e.g. `255.255.255.0`
  allows `192.168.1.1-192.168.1.254`
* cider is a compact way to write subnet mask: 192.168.1.0/24

* switch is in one network, router in between.
* if hosts are in different subnets, switch can't handle a dialog between them, that's where
  you need a router. e.g. machine A: 192.168.1.0, B: 192.168.1.1

* ASN: block of IPs. bunch of IPs. to make IP resolving easier. bigger orgs will have ASNs.
* WAF: web application firewall. that is implemented in CDN.
in this case you should find the actual IP of the server. and even then you might not be
able to connect to it.
