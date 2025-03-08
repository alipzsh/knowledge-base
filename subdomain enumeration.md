
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