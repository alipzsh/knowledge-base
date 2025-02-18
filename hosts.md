# /etc/hosts

after requesting an IP you might get a redirection response to a hostname which your system
can't resolve to an IP; because the domain is custom and not in a public DNS. so you have to
[do it manually](80/README.md)

then try it with:
  * `curl -L`
  * or `curl --socks5-hostname localhost:<local_port> http://sightless.htb`
  * or another browser: `google-chrome --proxy-server=socks5://localhost:<local_port>`
  * but on burpsuit you should add it manually in Hostname resolution overrides.
