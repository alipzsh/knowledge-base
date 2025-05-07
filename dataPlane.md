# dataPlane

* The primary data-plane role of each router is to forward datagrams from
its input links to its output links

* the primary role of the network control plane is to coordinate these
  local, per-router forwarding actions.

* two important network-layer functions:
* Forwarding (data plane): moving a packet from input link to the
  appropriate output link.

  * router-local action
  * implemented in hardware

  * by examining one or more fields in the packet's header, indexing
  into it's **forwarding table**, decides the outgoing link.

* Routing (control plane): determining the path taken by packets as they
  flow from a sender to a receiver.

  * network-wide
  * takes much longer
  * often implemented in software
  * the routing algorithm function in one router communicates with the
  routing algorithm function in other routers to compute the values for
  its forwarding table.

  or
  * SDN (software-defined networking): a remote controller computes and
  distributes the forwarding tables which is implemented in software.

* packet switch: a general packet-switching device, transferring a
  packet from input to output link, according to header fields.

* link-layer switches (device): forward based on fields of link-layer
  frame.

* routers (network-layer devices): based on their network-layer datagram
  header fields.

* generic router architecture:

* port: physical input and output interfaces.

  * input port:
   * line-termination: terminating an incoming physical link
   * link-layer processing:performing link-layer functions to interoperate with the link-layer
   at the other side of the incoming link.
   * lookup: using the forwarding table to determine output.
   * checking packet's version number, checksum and time-to-live field.
   * updating counters used for network management.

  * control packet are forwarded to the routing processor.

  * switching fabric: connects input ports to output ports.

  * output port: stores packets and transmits them on the link by
  performing link-layer and physical-layer functions.

  * router processor:
   * performs control-plane functions.
   * executes routing protocols
   * maintains routing tables and link state information and computes
   the forwarding table for the router
   * in SDN; communicating with the remote controller.
   * network management functions

* line cards: processing parts in input and output link, responsible for
  executing functions.

* other than processor (duh), all others are implemented in hardware
  because they have to be done in nano seconds compared to milliseconds
  or seconds.

* destination-based forwarding:

 the router matches a prefix of packet's destination address with the
 entries in the table.

 * longest prefix matching rule:
  if there are multiple matches, the router forwards the packet to the
  longest longest prefix match.

 * a packet might be temporarily blocked from entering the switching
   fabric and will be queued (blocking,queueing and scheduling).

 (match plus action)

* NAT: a packet with certain transport-layer port number will have its
 port number rewritten before forwarding (action).

* *switching*:
 * via memory: traditional computers, between input and output ports,
   under control of the CPU.
   * packet was copied into processor memory
   * the routing process (CPU) extracted the destination address from
     the header.

   * find the appropriate output port in the forwarding table
   * copy the packet to the output port's buffer.

 * forwarding through put: the rate at which packets are transferred
   from input to output.

   two packets can not be forwarded because only one memory read/write
   can be done at a time over the shared bus.

 * shared bus: input transfers directly to the output port through a
   shared bus, by pre-pending a switch-internal label.
   all output ports receive the packet, but if the label matched, it
   will be kept.

 * via an interconnection network: to overcome the bandwidth limitation
   of s *shared bus*.

  * corssbar switch: an interconnection network to connect N input port
   to N output ports with 2N buses.

   the crosspoint at the intersections will be closed when the packet is
   being sent so multiple packets could be forwarded in parallel.

   it's *non-blocking*: as long as no other packet is being sent to that
   output port the packet won't be blocked.

 * there is also somthing called a multi-stage switching fabric.

 * multiple switching fabric in parallel: input port breaks packets into
   K smaller chunks, sends (sprays) the chunks through N switching
   fabric to the output port.

* output port processing:

 * transmitting the packets stored in the memory (buffer) over the output
 link: selecting, dequeueing, doing link-layer and physical-layer
 functions.

 * location and extent of queueing depends on the traffic load, speed of
 switching fabric and the line speed.

* input queueing:

 * if there are N input ports and fabric switch is N times faster than
 the input and output line speeds, there will be little to no queueing
 in the input port.

 if it's not fast enough: delay accrues.

 if two packets are supposed to be forwarded into the same output queue,
 then one of the packets will be blocked.

 head of the line blocking: in an input-queued switch, a queued packet
 must wait (even though it's output port is free) because it is blocked
 by another packet at the head of the line.

* output queueing:

 * when there is not enough memory to buffer incoming packets; either
   drooping the incoming packets or already queued ones.

 * dropping a packet or marking the header, before full buffer to
   provide a congestion signal to the sender.

* packet scheduling:

 * first-in-first-out: transmits them in the order they arrived at the
   output link queue.

 * priority queueing: classified into priority classes upon arrival,
   with each class having it's own queue.

   packets in a class are chose in FIFO manner.

  none preemptive primary queueing: the transition of a packet is not
  interrupted once it has begun.

 * round robin: classified into classes without a strict service
   priority. instead a round robin scheduler, alternates services among
   classes.

   weighted fair queueing: a generalized form of round robin. in the
   each class is assigned a weight, in worst case even if all classes
   have queued packets, class i will be guaranteed to receive a fraction
   of the bandwidth.

* IP

* IPv4 datagram format:
 * version number: 4 bit's to specify the version of the protocol.
   router determins how to interpret the remaider of the datagram.

 * header length: to determine where the payload actually begins. it's
   typically a 20-byter header.

 * type of service: to distinguish different types of IP datagram.
   e.g, real-time from none-real-time.

 * datagram length: total size of header plus data.

 * Identifier, flags, fragmentation offset:  when a large IP datagram is
   broken into several smaller IP datagrams which are then forwarded
   independently to the destination.

 * time-to-live: if the ttl reaches 0 a router must drop that datagram.

 * protocol: when it reaches it's destination. indicates the specific
   transport-layer protocol to which the data should be passed.
   like port in transport-layer.
   the glue that binds the network and transport layers together.
   port number glues transport and application layers together.

 * header checksum: detecting bit errors in a received IP datagram.
 * source and destination IP addresses.
 * data(payload): transport-layer segment or other types of data.

* if an IP datagram carries a TCP segment, it will carry another 20
  bytes of TCP header.

* **IP addressing** :

* interface (or socket?): the boundary between the host and the physical
  link.

* host: one single link; router: two or more (to receive and send) so it
  has multiple interfaces.

* IP address is associated with an interface rather than host or router
  containing that interface.

* a part of interface's IP address will be determined by the subnet to
   which it's connected.

* subnet (IP network): the network interconnecting host and router
  interfaces

  IP addressing assings an address to this subnet: 223.1.1.0/24. /24,
  * subnet mask: indicates that the leftmost 24 bits of the IP defines
  the subnet addess.

  so any host connected to the subnet has an address of the form
  223.1.1.xxx.

* CIDR: generalizes the notion of subnet addressing.

  the 32-bit IP address is divided into two parts with the dotted-decimal
  form a.b.c.d/x;

  x indicates the number of bits in the first part of the address.

* prefix (network prefix): x constitutes the network portion of the IP
address.

 the IP addresses of of devices within the organization share the common
 prefix.

 * only the x leading prefix are considered by routers outside the
 organization.
 the remaining bits are to distinguish among the devices within the
 organization.

* address aggregation (route aggregation or route summarization):
using a single prefix to advertise multiple networks.

e.g: 200.23.16.0/20, any datagrams should be sent here the first 20 bits
match. But there might be other organization within the address block
that the rest of the world aren't aware of.

* IP broadcast address: 255.255.255.255, a datagram with this
destination address is delivered to all hosts on the same subnet.

* DHCP(dynamic host configuration protocol) allows hosts to be allocated
  an IP address automatically.

  it could be configured so a certain host always receives the same IP.
  or it could be a temporary IP that will be different each time.

  things a host can get out of DHCP: it's subnet mask, address of it's
  first-hop router (default gateway), address of it's local DNS server.

  each subnet has a DHCP server, if no server is present on the subnet,
  a router (DHCP relay agent) that knows the DHCP server for that
  network is needed.

* four steps of a DHCP protocol:
 * DHCP server discovery: client sends a UDP packet to port 67,
   encapsulated in an IP datagram with the destination address
   255.255.255.255 and source address 0.0.0.0.

   the client doesn't know the IP of the network to which it's
   attaching.

 * DHCP offer: contains the transaction ID of the received message,
 purposed IP address, the network mask and the IP address lease time
 (the amount of time the IP will be vaild) and is broadcast to all hosts
 on the subnet.

 several DHCP servers might be available so the client might have
 several options.

 * DHCP request: the client will respond to it's selected offer echoing
   back the configuration parameters.

 * DHCP ack: server confirming the requested parameters.

 the client can renew it's lease on the IP address.


* NAT:
 * e.g: 10.0.0.0/24 subnet address, used by devices within the network
        10.0.0.0/8  reserved for a private network or a realm with
        private addresses
 * realm with private network: refers to a network whose addresses only
   have meaning to devices on the network.

 * the NAT router looks like a single device with an IP address to the
   outside world and runs a DHCP router.

 * to distinguish the internal hosts:
   it uses a NAT translation table which includes the port numbers and
   IP addresses.

 * the router changes the port number and internal IP of the host
   request with it's WAN IP and it's arbitrary port.

* IPv6:
 * increases the size of IP address.
 * some of IPv4 fields are dropped or optional. header is now 40 byte
   length, so faster processing in the routers.
 * flow labeling: packets could be labeled so that they belong to a
   particular flow.

* fields:
 * version: 4 bits, the IP version number. which is 6.
 * traffic class: 8 bits, like TOS in IPv4, priority stuff.
 * flow label: 20 bits to identify a flow of datagrams.
 * payload length: 16 bits, unsigned int, the length of bytes after the
   header.
 * next header: the protocol to which the datagram will be delivered.
 * Hop limit: (similar too TTL) decremented by on, by each router that
   forwards the datagram. zero? the router discards it.
 * source and destination addresses.
 * data.

* comparison to IPv4:
 * fragmentation and reassembly done in end systems rather than routers
   to speed up IP forwarding.
 * header checksum: transport-layer and link-layer have their own
   checksum, so why to slow the process.
 * option field: not standard but can be the next header pointed to.

* generalized forwarding and SDN:
* match plus action paradigm:
