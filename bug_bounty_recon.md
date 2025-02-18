# bug bounty recon

`https://github.com/dwisiswant0/awesome-oneliner-bugbounty`

## dorking

github search: "'website' password"

## scope discovery

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

collections of networks assigned to a company; use `https://www.bgp.he.net/`.
(sometimes, not finding anything?)

bgphe.net copy > bgp.sh (to clean the ASNs) > amass intel (to get domains)

if no ASN found in `bgp`, the ASN in `whois` is public, not very useful.
try other stuff with amass.

ASN (IP space owned by an organization) → IP Range (addresses owned) → CIDR (compact
representation of range).

### certificate parsing

find host names that use the same certificate `https://crt.sh/?q=facebook.com&output=json`

also, `sslscrape.py` for each found IP.

## subdomain enumeration; host => subdomains

Subdomain enumeration is dependent on DNS, as subdomains are registered in DNS records.

* remove duplicates from combination of two wordlists: `sort -u wordlist1.txt
  wordlist2.txt`
* find pattern in subdomains
* take note of company's stack; Jenkins: check if `jenkins.example.com` is valid
* run tools recursively.

### amass

`intel` finds root domains (using IP space or ASNs)

`intel -asn 1748`

`enum -d` for subdomain enumeration

to do it in active mode:

`amass enum -active -d <domain> -o <output>`

different options:
  * active: the interesting one
  * passive: found subdomains
  * normal: less than others

### subfinder

(passive): more straight forward
`subfinder -d <domain> -o <output>`

* use amass active and subfinder


#### put the results together

put the result of all used tools together:
`cat * | grep -Eo '([a-zA-Z0-9_-]+\.)+<host_name>' | sort | uniq > subdomains`

#### find the working subdomains: subdomains => working ones

then use curl and `httpx` to check which ones and are UP.

* `httpx -list subdomains -timeout 10 -status-code -silent"`
* `httprobe` could be good to try.
* and [this](32/IPtest.sh) script.

## gowitness: working subdomains => screenshots of them => interesting subdomains
if issues, see the [end](#issues)

`gowitness scan file -f <file> --timeout 10 --write-stdout -t 1`

then `gowitness report server`
then `google-chrome --proxy-server="socks5://localhost:8089"` and use `0.0.0.0:7171`.
you could use a different port that your ssh tunnel.

I can't get them from my headless server. but can from the local:
`gowitness scan file -f httpx --timeout 10 --write-stdout --chrome-proxy=socks://localhost:8089`

`cat report | grep -Eo 'target=http[s]?://[^ ]* status-code=200'` to get 200.

# when you want to find bug on on webpages

then open them in the browser. use `wappalyzer` extension to see the technologies.

## service enum/ port scanning

active scanning: directly sending requests to the target machine, using
nmap.

slow scan on top 100 ports: `nmap -A -v -F -T1 <target>`

passive scanning: using third-party resources to stay hidden; shodan,
census, project sonar.

## directory brute-forcing: interesting subdomains => content discovery

`ffuf -u <url/FUZZ> -w wordlist.txt` and `-fc <status_code>` to exclude

### cleanup

`cat * | grep -E 'Status: (2[0-9]{2}|3[0-9]{2})' | awk '{print $1$2$3}' | sort | uniq > final`

## crawling/spidering

on the whole or maybe on an interesting subdomains spider for more info and parameters that
pass data.

something like this: `domians | httpx | katana`

# next:

enough with enumeration, not that it is ever going to be perfect

loop:
=> check `gowitness` `200`, (then other ones)
=> directory enumeration
=> check for `200`, (then other ones)
=> attack surface?

!issues

1. there are differences in response stats codes of `httpx`, `curl`, `gowitness` and
   tunneled browser.

  which I'm assuming is because of the way gowitness and browser will interact with the
  server in multiple requests. I can see this in a consistent difference between using curl
  in a script versus in a one line terminal request.

  so the best way to validate them is to use them in a script.

  whether they return `200`, `301` or `403`, they should all be checked. so it doesn't
  really matter to check them for a specific code other than prioritizing which ones to
  check first.

  in the initial subdomain evaluation, `httprobe` is more reliable (because it doesn't seem
  to differ based on status code) then passed to gowitness.

2. at first `gobuster` sends a request that doesn't exist, expecting a `404`, otherwise:
   `the server returns a status code that matches the provided options for non existing
   urls.`

# how to bypass different status codes:

* 200 range: the file or directory exists and accessible
* 403: exists but protected, try to bypass
* `403` [possible reason and bypass](87/README.md)

* something like `can't GET <path>` means the path exists, maybe try a different request method?
* try with `curl -I` for more info.

* how is it that ns lookup for domains and subdomains are different.

* The subdomain may resolve to multiple IP addresses for load balancing or redundancy.

* nslookup:

  why IP changes: 
  CDN Load Balancing or Caching
  Fallback or Failover Configuration: primary IP became unavailable
  Use of Multiple IPs for Redundancy

# issues

## gowitness

to try to fix errors, make it simple:
  * `gowitness scan single --url "http://google.com" --screenshot-fullpage --write-stdout`
  * check if you could do this on the network without issue.
  * it seems `screen-shot=false` is due to network issues.
  * remember to use `-t 1` on the server (or 2?).
  * Screenshoting isn't that reliable or I don't get it, so I'll better move on and try
    things manually in layers.
