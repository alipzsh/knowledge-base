# ip

# useful commands

`ip a <addr>`

- `<NO-CARRIER,BROADCAST,MULTICAST,UP>)` show the interface is enabled by you or the system.
- But the `state (DOWN)` means no carrier.

# set up IPs for devices to be on the same network

`ip addr add 10.10.2.5/24 dev <>` the first 24 bits are the network and the last 8 are host address
`ip addr add 10.10.2.10/24 dev <>` the second computer

delete them by `ip addr del 10.10.2.10/24 dev <>`

# routing: connecting two networks

`ip route add 5.5.5.0/24 dev enp0s9` route requests to this IP to enp0s9 device.
`ip route` to see defined routes

but you can't always do these manually; you can't connect to every network manually.

add a default route: sends traffic to it (gateway) for destinations outside the local
network (the network it doesn't know about)

`ip rotue add default dev enp0s3`

your default gateway should be on the same network as you get your IP from.
it should be pingable on mac level.


EX: in [bridge](14/README.md);

in dell we have:

```
dell@ubuntu:lxc$ ip route
default via 192.168.1.1 dev br0 proto static
10.0.3.0/24 dev lxcbr0 proto kernel scope link src 10.0.3.1
192.168.1.0/24 dev br0 proto kernel scope link src 192.168.1.51
```

like what you did manually but here, it was done through /etc/systemd/network

use traceroute for info
