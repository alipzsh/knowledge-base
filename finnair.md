# finnair

### whois

### ASN

AS1748

### route?

```
194.145.52.0/24	    Route 	Finnair Oy
194.145.48.0/22	    Route 	Finnair Oy
194.145.32.0/20	    Route 	Finnair Oy
193.142.247.0/24	Route 	Finnair Oy
157.200.215.0/24	Route 	Finnair Oy
157.200.100.0/24	Route 	Finnair Oy
157.200.0.0/16	    Route 	Finnair Oy
```

### nslookup

```
Non-authoritative answer:
Name:   finnair.com
Address: 108.158.75.61
Name:   finnair.com
Address: 108.158.75.26
Name:   finnair.com
Address: 108.158.75.19
Name:   finnair.com
Address: 108.158.75.68
```

### rev IP

for all finnair IPs:

```
NetRange:       108.156.0.0 - 108.159.255.255
CIDR:           108.156.0.0/14
```

### amass

try these too: `amass enum -brute -min-for-recursive 2 -d finnair.com`

# plan

  1. Screens shots in local folder resulted httprobe => gowitness
  2. 200s in gowitnesse's report (clean both httpx and httprobe \_reports) 3. httpx_200 in the server
  4. search to see if other codes could be important.
  5. scan the IP space for other domains
