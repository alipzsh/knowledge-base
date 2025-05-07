# DNS

what it does:

  * translates hostnames to IP addresses.
  * host aliasing: a canonical host name can have aliases.
  * mail server aliasing.
  * load distribution: among replicated servers, each with different IP
    address. a set of IP addresses is associated with one alias
    hostname.

    clients get the whole set in rotated order and usually use the first
    one.

## DNS client process of getting the IP

DNS hierarchy:

  * local DNS: provided by ISP, does the rest of the request by itself.
  * root (contain IPs of TLD servers)
  * TLD  (contain IP of authoritative servers): a TLD server for each top
  level domains (com, net, gov, uk, fr, ...) 
  * then the client queries the authoritative server with the hostname.

recursive queries: between client and local DNS.
iterative queries: between local host and the hierarchy of the DNS.

## DNS caching

the DNS server saves the mapping from a hostname to the IP.

the cached DNS is often discarded after two days.

local DNS servers can cache the IP addresses of TLD servers.

## DNS records

A resource record is a four-tuple that contains the following fields:
(Name, Value, Type, TTL):

  * TTL is the time to live; when the record should be removed from a
    cache.

### A Records

host to address mapping. (relay1.bar.foo.com, 145.37.93.126, A)

  * if a server is authoritative for a hostname, it contains type A
    record for that hostname.
  * in non-authoritative as cache.
  * every root or TLD server: they contain an NS record that maps the
    queried hostname to an authoritative server. they also have a type A
    record that maps the authoritative server to it's IP.

### NS Records

domain (Name) and the hostname of an authoritative DNS server (Value). (foo.com,
dns.foo.com, NS)

  * in non-authoritative servers

### CNAME Records

alias (Name) for the canonical name (Value)

### MX Records

alias (Name) for the canonical name (Value) of an mail server.

### SRV Records

`_citrixreceiver._tcp.finnair.com --> srv_record --> vp.finnair.com`

a service (`citrix...`) is hosted on the server `vp.finnair.com`.

  * in non-authoritative servers
unlike CNAME, it needs more details like port and protocol.

### FQDN

An FQDN provides a full path to the domain, including all necessary components to uniquely identify it in DNS (Domain Name System).

EX:

`FQDN`: `autodiscover.finnair.com`
  * Host: `autodiscover`
  * Domain: `finnair.com`

## practicals

this `ns-465.awsdns-58.com (FQDN) --> a_record --> 205.251.193.209
(IPAddress)` is a A type  record.

`ns-465.awsdns-58.com`: is a NS type hostname with it's IP.

