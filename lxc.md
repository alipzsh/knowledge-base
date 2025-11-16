# lxc

```
apt install lxc
lxc-create -n myContainer -t ubuntu  # for more options, check the website
lxc-start -d -n myContainer
lxc-attach -n myContainer
exit
```

-d: detach

`lxc-ls -f` to check the status

access it through host: /var/lib/lxc

- remove a container:
  - stop if running: `lxc-stop -n <container_name>`
  - `sudo lxc-destroy -n test mycontainer`

# ufw configuration

```
sudo ufw allow in on lxcbr0
sudo ufw allow out on lxcbr0
```

and perhaps `sudo ufw default allow forward`


* you might need to configure the network [bridge](bridge)
* you can configure each container in `/var/lib/lxc/<name>/config`
