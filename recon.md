# recon

* find machine IP:
  `nmap -sn <ip_range, 192.168.56.3/24>`

# use `nmap`

```sh
ports=$(nmap -p- --min-rate=1000 -Pn -T4 10.10.10.245 | grep '^[0-9]' | cut -d
'/' -f 1 | tr '\n' ',' | sed s/,$//)
```

`nmap -p $ports -Pn -sC -sV 10.10.10.245` to get the opened ones

`nmap -sV -sC -Pn 10.10.11.38` " this does the basic useful stuff

  * `-A`: aggressive
  * `-p-`: get ports
  * `-p {ports}`: ports to scan
  * `-Pn` might be needed in case there is firewall
  * `--mine-rate=1000`
  * `-o` save to a file
  * `-sV`: version scanning
  * `-sC`
  * `-oA`: output to file
  * `-v`: increased verbosity, more info

* use `https://www.exploit-db.com/` to check if there are vulnerable
  running software.

* check ssl certificate:

```sh
 443/tcp open  ssl/http Apache httpd 2.4.51 ((Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9)
 | ssl-cert: Subject: commonName=earth.local/stateOrProvinceName=Space
 | Subject Alternative Name: DNS:earth.local, DNS:terratest.earth.local
 | Issuer: commonName=earth.local/stateOrProvinceName=Space
```

## if there are multiple servers on the same hosts

it needs a hostname to be [specified](80/README.md#add_hostname).

* find domains based on IP: `dig -x`

* use *curl* for more info
  `
  curl <ip:port>/<dir>
  `

* stack trace: report of the active stack frames at a certain point in time
during the execution of a program

# where to look for vulnerabilities

https://attackerkb.com

# general recon notes

if an application (e.g. web server) is showing system status, it's executing system commands.
