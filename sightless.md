# sightless

# /etc/hosts

I got a redirection and can't access the website:

```
hunter@penvm:~/hunt/htb/sightless$ curl --head 10.10.11.32
HTTP/1.1 302 Moved Temporarily
Server: nginx/1.18.0 (Ubuntu)
Location: http://sightless.htb/
```

add into `/etc/hosts`: `10.10.11.32 sightless.htb`.

also in `/etc/hosts` on the target machine:

```
127.0.0.1 sightless.htb sqlpad.sightless.htb admin.sightless.htb
```
so add these to `/etc/hosts` on the attack machine.

# CVE-2022-0944

https://huntr.com/bounties/46630727-d923-4444-a421-537ecd63e7fb

You could somehow use `FFUF` to fuzz the ports and in this case the one that hanged in the
one in use.
`https://youtu.be/6CsH0DO_00w?t=508`

# docker

we are in a docker. and `/etc/shadow` is readable, if we are lucky the password used in the
docker is the same in the main host, then try to crack the password.

# pass crack

```
./unshadow /etc/passwd /etc/shadow > mypasswd
john mypasswd -w=<path_to_wordlist>
```

hashed password for michael: `insaneclownposse`.

`froxlor` is running on port `8080`.

create an ssh tunnel

`curl localhost:7000` => nothing
`curl -L localhost:7000` => `localhost:7000/notice.html`
`curl 127.0.0.1:7000` the same as `curl admin.sightless.htb:7000`=> a login page at `127.0.0.1:7000/`

`netstat -nltp`:

```
0.0.0.0:22
127.0.0.1:3000
0.0.0.0:80
127.0.0.1:33060
127.0.0.1:8080
127.0.0.53:53
127.0.0.1:40433
127.0.0.1:37959
127.0.0.1:56381
127.0.0.1:3306
```

`https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/chrome-remote-debugger-pentesting/`

couldn't get root, it isn't anything technical, already spent so much time.

# learned

if one thing doesn't work, try different stuff instead of trying to fix it right away,
EX: if a payload doesn't work, first check if you can have any interaction to the target
using ping or wget. or try it with something else; write a script.
also you shouldn't do these manually, that's the point of programming.

read the documentations for a tool

if you can't get something done, learn more / do some related project even if you want to
get back to it.

if there is something new (which there are a lot and hopefully) take a deep breathe and
research, even create an instance of the app for yourself, it will take much less time than
frustrations.
