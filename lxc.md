# lxc
`
apt install lxc
lxc-create -n myContainer -t ubuntu  # more options, check the website
lxc-start -d -n myContainer
lxc-attach -n myContainer
exit
`
-d: detach

`lsc-ls --fancy` to check the status

access it through host: /var/lib/lxc

# ufw configuration

sudo ufw allow in on lxcbr0
sudo ufw allow out on lxcbr0

but it still doesn't work?
`sudo ufw default allow forward`
not sure what it does
