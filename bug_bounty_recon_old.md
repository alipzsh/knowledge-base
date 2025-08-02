`https://github.com/dwisiswant0/awesome-oneliner-bugbounty`

[[dorking]]

[[scope discovery]]
[[subdomain enumeration]]: host => subdomains
[[crawl]]
[[gowitness]]: working subdomains => screenshots of them => interesting subdomains
[[directory enumeration]]: interesting subdomains => content discovery
[[port scanning]] more info on interesting subdomains

[[API analysis]]

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

Etc

 4. Send the probed-domains list to httpx to remove dead domains using the -fc flag

cat probed-domains.txt | httpx -fc 404 | tee -a live-domains.txt

5. Send the live domains to httpx to fetch interesting headers:

cat live-domains.txt | httpx -title -sc -server -location -td -method -silent | tee -a final-domains.txt 
