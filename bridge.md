# bridge

* network bridging function: creates a single, aggregate network from
  multiple communication networks or network segments.

  connects two separate networks as if they were a single network.

# use ip-link to make it.
* add the main interface IP and default gateway (router's IP) to the
  bridge
* then make br0 the master of enp9s0
* br0 becomes the main interface that is connected to the network,
  while enp9s0 is now a port of the bridge.
* be sure to add the IP to the router (there might be other ways to
  make it static).

* ufw doesn't seem to be denying the bridged vm, nftables.

# using /etc/systemd/netowrk/ (based on arch wiki)
* active after boot
* and unlike with ip-route, the host doesn't lose internet access.

* three files:
  * 25-br0.en.network; changing the name to 10-netplan-enp9s0.network,
    because this is the one overwriting the configuration in
    /run/systemd/network to a dhcp, instead of enslaving it.
    * found the problem by monitoring systemctl status systemd-networkd

   `
   [Match]
   Name=enp9s0

   [Network]
   Bridge=br0
   `

  * 25-br0.netdev

  `
  [NetDev]
  Name=br0
  Kind=bridge
  `

  * 25-br0.network

  `
  [Match]
  Name=br0

  [Network]
  DNS=192.168.1.1
  Address=192.168.1.51/24
  Gateway=192.168.1.1
  `

  * it's static, so might not need to configure the router for it.
  * also, might not have to configure router so that it would have static IP, maybe like
    this:
    * create a network, named vnet0, give it an static IP, router's gateway and in another
      file, enslave it to br0.

$ networkctl
IDX LINK   TYPE     OPERATIONAL SETUP
  2 enp9s0 ether    enslaved    configured
  4 br0    bridge   routable    configured

  * creating symlink to /etc/systemd/network breaks it.
