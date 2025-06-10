# lab

## methods of installing/managing vms

- `virt-install` command line
- `qemu-system` lower level
- `virt-manager` from the host connected to the server.

## methods of auto deploying an ISO

1. unattended installation from ISO: kickstart to install an OS

2. prebuilt cloud images

- cloud-init to setup username and password on the first boot
- virt-customize: something like cloud init, but more.

```sh
$ virt-customize -a MY-CLOUD-IMAGE.qcow2 \
    --root-password password:SUPER-SECRET-PASSWORD \
    --uninstall cloud-init
```

`virt-sysprep` to clean customization

	
`guestfish`: to directly modify images offlie (e.g. files)
	

--> run your configurations scripts --> clone the image

[[qemu]]

## How to SSH into another computer?

  * use `sudo vi /etc/ssh/sshd_config`:
  
  	* uncomment and change `port 22` to some thing else.
  	* uncomment and change `PasswordAuthentication` to `no`.
  	* uncomment and change `PermitRootLogin` to `no`.
  	* reload everything: `sudo systemctl reload ssh`.
  
  * use `ssh -p port_number user@host_ip`. if your user name matches the host `ssh host_ip`.
  
  * use ssh keys:
  `
  ssh-keygen -t rsa
  ssh-copy-id remote_host
  `

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
