after searching the host and `stream:http`, we find out there are too many requests that happened in a small period.

after more investigation we find a request that contains ``

```
Acunetix-Product: WVS/10.0 (Acunetix Web Vulnerability Scanner - Free Edition)
Acunetix-Scanning-agreement: Third Party Scanning PROHIBITED
Acunetix-User-agreement: http://www.acunetix.com/wvs/disc.htm
```
`src_ip: 40.80.148.42`
`dest_ip: 192.168.250.70`

so we found the malicious source of requests IP.

we can also search our server IP to see if a request were sent (which shouldn't be allowed, e.g. reverse sell.)
`sourcetype="stream:http" c_ip="dest_ip"`, then we found 9 suspicious events.

#att be sure not to sample the output at this point.

	after analyzing the requests to get info on the staging server:
```http
dest_ip: 23.22.63.114
request: GET /poisonivy-is-coming-for-you-batman.jpeg HTTP/1.0
site: prankglassinebracket.jumpingcrab.com:1337
```

there are brute-force attacks, from `40.80.148.42`.
uploaded file `filename="3791.exe"`