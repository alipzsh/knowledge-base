# lxc
`
apt install lxc
lxc-create -n myContainer -t ubuntu  # for more options, check the website
lxc-start -d -n myContainer
lxc-attach -n myContainer
exit
`
-d: detach

`sudo lxc-ls --fancy` to check the status

access it through host: /var/lib/lxc


- remove a container: 
	- stop if running: `lxc-stop -n <container_name>`
	- ``sudo lxc-destroy -n test mycontainer`
# ufw configuration

sudo ufw allow in on lxcbr0
sudo ufw allow out on lxcbr0

but it still doesn't work?
`sudo ufw default allow forward`
not sure what it does