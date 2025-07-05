# lab

## methods of installing/managing vms

- `virt-install` command line
- `qemu-system` lower level

[[qemu]]
[[qemu#methods of auto deploying an ISO]]
[[bridge]]
[[ip]]

## Move stuff between nodes

Run a python server.

`wget -r http://your-server:8000/desktop/`

```
curl -O http://your-server:8000/desktop.tar.gz
tar -xzf desktop.tar.gz
```

And perhaps do it on installing using `virt-install` or something.

## How to connect with openvpn?

* use `scp` to move configuration files: `scp -P port_number file_name host_ip:/remote/directory`
* so at this point I can change my IP in terminal, but Open VPN doesn't connect.
* then I found a much simpler way to just connect Open VPN through proxy:
  `http-proxy 127.0.0.1 2081` after `proto tcp` in the configuration file.

# use ufw

`ufw allow from <ip address>`

* to use things like netcat, you need the target to be able to access the host:

`ufw allow from <hostonlyRange=192.168.56.1/24> to <hostInterface=192.168.56.1>`
either you have to sudo ufw default allow forward
or 
╚ $ sudo vi /etc/sysctl.conf
╔ dell@openVpn-server:~
╚ $ sudo sysctl -p
net.ipv4.ip_forward = 1

# add proxy to the terminal

`export http_proxy='http://localhost:2081'; export https_proxy='https://localhost:2081'`

# connected devices to wifi

sudo arp-scan --interface=wlp3s0 --localnet
sudo arp-scan -l -t 200 -I $(ls /sys/class/net | grep -o "wl[^\t]\+")
