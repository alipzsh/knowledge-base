getting IP spaces
finding top-level domains

### whois

get info on the registered domains and their associated owners.

### reverse whois

(maybe not that useful, EX: it might contains stuff that are owned by the same person but
not in the scope).

find other assets owned by a person or company.

Simply enter the email address or name of the person or company to find other domains
registered using those same details.

`https://viewdns.info/reversewhois/`

### reverse IP lookup/ reverse DNS lookup: domain => info of the host server

Reverse IP Lookup is a way to identify hostnames that have DNS (A) records associated with
an IP address. A web server can be configured to serve multiple virtual hosts from a single
IP address.

[nslookup](109/README.md) `<known_domain>` => IP
`whois <IP>` => `NetRange`
                   `CIDR`
                   `AS`
### ASN

collections of networks assigned to a company; use .
(sometimes, not finding anything?)`https://www.bgp.he.net/`

bgphe.net copy > bgp.sh (to clean the ASNs) > amass intel (to get domains)

if no ASN found in `bgp`, the ASN in `whois` is public, not very useful.
try other stuff with amass.

ASN (IP space owned by an organization) → IP Range (addresses owned) → CIDR (compact
representation of range).

### certificate parsing

find host names that use the same certificate `https://crt.sh/?q=facebook.com&output=json`

also, `sslscrape.py` for each found IP.