# transport_layer
* bidirectional: functioning in two directions.

# rdt2.1

* sequence numbers show wethere the next packet is being sent or the
  last one is being retransmeitted.
* sender:
    * state1 (wait for call0 from above):
        sends data with seq0
        move to state2
    * state2 (wait for rcvpkt):
        if (corrupted || isNAK) retransmit seq0
        if (notcorrupted && isACK) move to state3
    * state3 (wait for call1 from above):
        send data with seq1
        move to state4
    * state4 (wait for rcvpkt)
        if (corrupted || isNAK) retransmit seq1
        if (notcorrupted && isACK) move to state1
* receiver:
    * state1 (wait for seq0):
        if (notcorrupt && seq0) send ACK and move state2
        if (corrupted) send NAK
        if (notcorrupted && seq1) send ACK
            # last response was was corrupted, so the sender retransmits
            pkt1 again.

# rdt2.1

* ACK<n>: positive acknowledgement for PKT<n>

# rdt2.1

* why while waiting for call0,1 and also waiting for ACK0,1 there are
  some conditions that we take no actions.
  there were these things in previous diagrams but then we would move
  into next state.

  answer: if it's waiting for ACK<n> and receiving another one, it's due
  to premature timeout, meaning that ACK was delayed, there is nothing
  to do here.

  still don't know what it's for in first and third states.

* transmition rate: the amount of time it takes for a bit to enter
  a channel, for example a 1 Gbps channel can transmit $10^9$ bits per
  second.

  knowing the size of the packet and R, you can measure the amount of
  time needed to transmit the packet into the channel.

* RTT: round trip propagation delay is the amount of time it takes for
  a packet to reach the receiver plus the amount time it takes for the
  acknowledgement of that packet to be received.

* sender utilization is the fractin of time it takes to transmit the
  packer into the channel, to the amount of time until it receives the
  acknowledgement.

# GBN

* sender:
  * invocation from above:
    * if (base == nextseqnum) start time // at the start of sending packets

  * receipt of an ack:
    * if (base == nextseqnum) stop timer // there is no unack packet,
      otherwise it will be restarted.

  * the timer is for the oldest but not yet acked packet.

* receiver:

  * packets are cumulatively delivered.
  * discards out of order packets.

* bandwidth-delay product: is the product of a data link's capacity (in
  bits per second) and its round-trip delay time (in seconds).

# SR

* Packet with sequence number in [rcv_base-N, rcv_base-1] are acked
  again. why? they have been retransmitted due to delay or problems with
  previous acked packet.

* MTU: maximum transmission unit, largest link-layer frame that can be
  sent.

  then setting the MSS (maximum segment size) plus tcp/ip header length
  based (40 bytes)  on that.

* MSS: the maximum amount of application layer data in a segment.

# TCP

* the sequence number of the segment is the is the sequence number of
  the first byte in the data field.
* the acknowledgement number is the sequence number of the next byte of
  data the host is waiting for.
* uses cumulative acknowledgments
* sends acknowledgments for every received segment.
* it resends the packet, for wchich the timer started.
* it's cumulative so if a previously sent ack is lost but the next ones
  are received at the sender, it will assume all the previous ones are
  received.

* host A not overflowing the receive buffer at Host B:
  LastByteSent – LastByteAcked <= min {cwnd, rwnd}

  amount of unacked packets shouldn't be more than the min of window or
  congenstion constraint rate.

* cookie: a TCP sequence number that is a complicated function (hash
  function) of source and destination IP addresses and port numbers of
  the SYN segment, as well as a secret number only known to the server.

* offered load ($\psi'$): The rate at which the transport layer sends segments
  (original and retransmitted data) into the network.

# congenstion avoidance

* suppose MSS 1460 byte, cwnd 14600, 10 segments will be sent each RTT.
  if all of those are acked, 1 MSS will be added to cwnd (1/10 of MSS
  per ack).

  cwnd += MSS • (MSS/cwnd)
