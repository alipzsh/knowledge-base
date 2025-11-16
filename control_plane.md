# control plane

## computing forwarding and flow tables

Per-router control: a routing algorithm runs in every router. routers communicate to compute
the values. OSPF and BGP protocols are based on this.

logically centralized control: a controller computes the forwarding tables. used in SDN and
4g/5g.

## routing algorithms

the goal is to find the least cost path through the network of routers.
there are limitations on which packets a router is allowed to forward.

## LS

centralized routing algorithm (link-state): aware of the cost of each link in
the network.

- packets containing information about each link's costs are sent to all other
  routers

decentralized routing algorithm: each node only know the costs of it's own
directly attached links. It gradually calculates the least-cost path to the
destination.


distance-vector algorithm: each node maintains a vector of sesame of costs for
all other nodes in the network.


static routing algorithms: routes costs change very slowly
dynamic routing algorithms: change due to traffic load or topology change.
load sensitive algorithms: costs change due to the level of congestion.

