
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

there are brute-force attacks, from `40.80.148.42`.
uploaded file `filename="3791.exe"`