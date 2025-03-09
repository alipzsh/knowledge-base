`https://github.com/dwisiswant0/awesome-oneliner-bugbounty`

# dorking

github search: "'website' password"

[[scope discovery]]
[[subdomain enumeration]]: host => subdomains
[[gowitness]]: working subdomains => screenshots of them => interesting subdomains
[[directory enumeration]]: interesting subdomains => content discovery
[[port scanning]] more info on interesting subdomains

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

there are differences in response stats codes of `httpx`, `curl`, `gowitness` and
tunneled browser.

which I'm assuming is because of the way gowitness and browser will interact with the
server in multiple requests. I can see this in a consistent difference between using curl
in a script versus in a one line terminal request.
# how to bypass different status codes:

* 200 range: the file or directory exists and accessible
* 403: exists but protected, try to bypass

* something like `can't GET <path>` means the path exists, maybe try a different request method?
* try with `curl -I` for more info.

* how is it that ns lookup for domains and subdomains are different.

* The subdomain may resolve to multiple IP addresses for load balancing or redundancy.

* nslookup:

  why IP changes: 
  CDN Load Balancing or Caching
  Fallback or Failover Configuration: primary IP became unavailable
  Use of Multiple IPs for Redundancy

