# v2ray

you'd better use xray-core as the back-end

* Download and extract it;
* ./v2ray run -c config.json
* curl ipinfo.io

* using export_proxy: export http_proxy=http://127.0.0.1:2081; export https_proxy=http://127.0.0.1:2081; export ALL_PROXY=socks5://127.0.0.1:2080
* using proxychains4:
  /etc/proxychains.conf: add http 127.0.0.1 2081

  then: proxychains curl ipinfo.io
  and much better: proxychains bash

use it with burp (local port forwarding): `ssh -L [bind_address:]port:host:hostport [user@]remote_ssh_server`

burp wont work like this through openvpn. I can't have it through v2ray and openvpn at the
same time: for hackthebox, use dynamic port forwarding: ssh -C -D 8089 `$1`

to setup burp for another browser: `http://burpsuite/` click of certificate and then search
"certificate" in the settings and add in under authority or sth.

* on googlechrom, you should use the appropriate proxy-server option, socks or http.
