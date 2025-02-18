# cmds

[curl](75/README.md)

echo

* `-e`: option enables interpretation of backslash escapes.
* `-n`: option suppresses the trailing newline.

sort

* `-n`: option ensures numerical sorting.

jq

* `-r`: outputs just the raw content of the strings (without quotes).

[netcat](74/README.md)

ls

* `-a`: show hidden files.
* `-ld`: more details of directories.

base64

* `-d`: decoding

gz

* `-d`: decompression.s

mysql

* `-u`: username
* `-p`: password

bash

* `-i`: interactive mode

find

* `-user`
* `-group`
* `-exec grep`
* `/`
* `-perm`: files that are executable, supports many modes, `-u=s`
* `-type`: f for regular file
* `find / -iname "*docker*" 2>/dev/null`: search for a regex in file name

stat

* `-c`
* `%s`

`ssh [user]@[IP] [command]`

* `-i`: the file to read the identity (private key), also allows for
multiple identities.

* `-t /bin/bash`: runs a pseudo-terminal
* `-p`: port

id - display user identity

chmod - change a file's mode

* `octal 4000`, `u+s`: setuid bit
* `octal 2000`, `g+s`: setgid bit
* `octal 1000`, `+t`: sticky bit

umask - set the default file permissions

su - run a shell as another user

* `-l [user]`: login shell, loads user's environment.
* `-c "command"`: execute a single command.
* `<user> -c`: exec a command as some user.

sudo - execute a command as another user

* `--preserver-env=PATH`: use the current environment factor.

`chown [owner][:[group]] file...`

ps – report a snapshot of current processes

* `x`: all processes regardless of TTY
* `aux`: the processes belonging to every user

* use it with grep, then `kill <PID>`

w - info about users and what they are doing

jobs – List active jobs

`bg %[job number]` – resume process execution in the background

* `ctrl-z`: stops a foreground process and move it to the
  background

`fg %[job number]` – Place a job in the foreground

`kill [-signal] PID...`

* `-1`: hangup, cause a reinitialization
* `-2`: interrupt, terminates a program
* `-9`: kill, terminated by kernel, messy
* `15`: terminal, default
* `18`: continue, sent by fg and bg
* `19`: stop, is sent to kernel
* `20`: terminal stop, `Ctrl-z`, received by the program

`killall [-u user] [-signal] name...`

openssl

* `s_client -connect`: connect to a server speaking ssl/tls

nmap

* `-A`: aggressive
* `-p-`: ports or port range
* `-sV`: version scanning
* `-o`: specify operating system
* `-oA`: output to file
* `-v`: increased verbosity, more info

# `diff [file1] [file2]`; compare files

  * `-u`: unified format
  * `-c`: context format
  * `-y`: compares side by side

`sort [file1] [file2] | uniqe -u`

`nslookup -option1 –option2 host-to-find dns-server`

it resolves a domain name into it's IP.

hydra

* `-L usernames.txt -P password.txt http-get|ssh://{server_ip}:port`

timeout:

* `-s`: signal (see `kill -l`)

mktemp:

* `-d`: creates dir

more:

* `v`: interacitve vi mode.

git:

* `log`
* `show <commit>`
* `branch -a`
* `checkout <branch_name>`
* `tag`: see tags Git tagging is a way to mark specific points in the
  history of the repository.
* `commit`: `-a` for all
* `push -u <branch>`
* `add`: updates what files are going to be committed. `-f` forces
  ignored files.

sherlock: to find usernames across social media.

current timestamp:

```sh
date +%s%3N
```
