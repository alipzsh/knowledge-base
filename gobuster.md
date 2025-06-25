### dir

  `gobuster dir -u <http://ip:port/> -w <wordListDir>`

`-r` redirect, is really important, otherwise nothing works.

`-x php,html,txt`: the string extensions we are expecting to find.
(the result can be achieved by using other directory enumeration
tools).
  
`-s <errorCodes>`
  
* try https too.
 `k`: skip tls (for https).

### dns

`$ gobuster dns -d mydomain.com -w /usr/share/wordlists/dirb/common.txt`

* might even want to use ffuf in place of `gobuster` so that we could
  control the rate and timing options.

* query strings (url parameter): a part of a URL that assigns values to
  specified parameters, `https://example.com/over/there?name=ferret`

  parameter value fuzzing: `http://10.10.0.50/dvwa/instructions.php?doc=FUZZ`
  parameter fuzzing `http://10.0.0.12/secret/evil.php?FUZZ=/etc/passwd`

* `dirb` (for some reason couldn't use gobuster on https)
  `dirb <target> <list>`
