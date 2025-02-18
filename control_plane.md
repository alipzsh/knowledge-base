# control plane

## computing forwarding and flow tables

Per-router control: a routing algorithm runs in every router. routers communicate to compute
the values. OSPF and BGP protocols are based on this.

logically centralized control: a controller computes the forwarding tables. used in SDN and
4g/5g.

## routing algorithms

the goal is to find the least cost path through the network of routers.

there are limitations on packets a router is allowed to forward.

centralized routing algorithm: takes the connectivity between all nodes and all link costs
as inputs, then calculates it. could be in a controller or routers; e.g. link-state
algorithms.

decentralized routing algorithm: calculation is distributed between routers, no node has
complete information about the whole network instead of it's own directly attached links.
then with the help of nearby nodes, it iteratively calculated the costs to the destination;
e.g. distance-vector algorithms.
