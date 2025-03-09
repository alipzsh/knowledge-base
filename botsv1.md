
## level 1

in the selected fields, view the top `sourcetype` values.

then to view http traffic: `index="botsv1" sourcetype="stream:http"`

we see that each event is parsed into different fields.

adding host `imreallynotbatman.com` to the search, we see some attack strings, that also include a header field that belongs to a vulnerability scanner.

```http
Acunetix-Product: WVS/10.0 (Acunetix Web Vulnerability Scanner - Free Edition)
Acunetix-Scanning-agreement: Third Party Scanning PROHIBITED
Acunetix-User-agreement: http://www.acunetix.com/wvs/disc.htm
```

noting the fields, we find info:

`src_ip: 40.80.148.42` (attacker's IP)
`dest_ip: 192.168.250.70`  (target IP)

if we search for target IP as the source of the request, we find 9 suspicious events (no *request* from a server is allowed):

`sourcetype="stream:http" c_ip="dest_ip"`

analyze the requests to get info on the staging server:

```http
dest_ip: 23.22.63.114
request: GET /poisonivy-is-coming-for-you-batman.jpeg HTTP/1.0
site: prankglassinebracket.jumpingcrab.com:1337
```

## level 2

looking for bruteforce attacks:

`sourcetype="stream:http" http_method=POST NOT Acunetix`

excluding requests that came from the scanner, we will have 431 remaining events.

`form_data` fields on some of them (containing the POST data), has admin as username and multiple passwords.

`sourcetype="stream:http" http_method=POST NOT Acunetix "passwd=" | table _time, form_data `

attacks are coming from `23.22.63.114`

`http_user_agent` is an interesting field, in this case there are a browser and something indicating a python script.

after the script executed, there is a browser request from the same IP.
they successfully logged in to a `joomla` control panel.

on further investigation, a familiar executable in uploaded. `filename="3791.exe"`

## level 3

first: find the MD5 hash of the uploaded file.

`sysmon`: a simpler alternative to windows events log.

use the appropriate `sourcetype` to get it in the results.
`sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"`

`EventID` field captures `sysmon` Event's IDs. which is one for process creation (lunches a process).

searching for executed with that file name.

`sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventID=1 3791.exe`

we will find couple of stuff.

there are multiple events (and hashes) because by executing a file other processes are also running.

to find the correct one add a table: `| table CommandLine, MD5`

![[Pasted image 20250305021051.png]]

## level 4

`we8105desk source="stream:ldap"` IP address = 192.168.250.100

to find the FQDN the cerber ransomware tries to direct the users to:
* look for onion domain lookups
* look for dns lookups close to that time, (dns lookup happens if users are accessing a new domain, the rest are cached)

query field of `stream:dns`