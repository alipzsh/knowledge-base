# qemu

`
## initial setup

apt-get install --no-install-recommends qemu-system-x86

sudo adduser $USER libvirt
sudo adduser $USER kvm

sudo systemctl start libvirtd
sudo systemctl enable libvirtd
`

on ubuntu it could either be `qemu-kvm` or `qemu-system-x86`
or you could just install: `sudo apt install virt-manager`

`add it to virt-manager: qemu+ssh://dell@ubuntu:4646/system`

permission denied reading the ISO: move the ISO to `/tmp`.
or the qcow2 to /var/lib/libvirt/images

or to fix it perhaps the right way, edit `/etc/libvirt/qemu.conf`:
`
user = "$USER"
group = "libvirt"

## using vboxmanage

start and shutdown a vm:

`
vboxmanage list vms
"myvm" {e4b0c92c-4301-4a7d-8af8-fe02fed00451}
vboxmanage startvm myvm --type headless
vboxmanage controlvm myvm poweroff
`

pause and resume:

`
vboxmanage controlvm mercury pause
  `

# cloning and snapshots

* a base clone and snapshots.
* really easy from the gui.
* more to learn of the file formats.

# resize the image:

`qemu-img resize vm.qcow2 +10G`

# Bridged network with a static IP address
Bridged networking can also be used to configure the guest to use a static IP address. To configure a bridged network with a static IP address for the guest virtual machine, use the following options:
Copy to Clipboard

--network br0 \
--extra-args "ip=192.168.1.2::192.168.1.1:255.255.255.0:test.example.com:eth0:none"

## methods of auto deploying an ISO


1. unattended installation from ISO: kickstart to install an OS

2. prebuilt cloud images

- cloud-init to setup username and password on the first boot
	- you can setup password, but networking issues, so you will have to use cloud-init I assume, virt-* won't work.
	- a workaround that works on debian:     --cloud-init disable=on,root-password-generate=off \
		yet, there will be issues and it's best to use one without/with it.
- virt-customize: something like cloud init, but more.

```sh
$ virt-customize -a MY-CLOUD-IMAGE.qcow2 \
    --root-password password:SUPER-SECRET-PASSWORD \
    --uninstall cloud-init
```

`virt-sysprep` to clean customization

	
`guestfish`: to directly modify images offlie (e.g. files)
	

--> run your configurations scripts --> clone the image

#### thin images


having an updated base image -> faster compared to containers

- info on backing https://libvirt.org/kbase/backing_chains.html
- snapshut, backing store and comming:
  https://dustymabe.com/2015/01/11/qemu-img-backing-files-a-poor-mans-snapshotrollback/

- use `qemu-system-x86_64 -enable-kvm -m 1024 noble-095747.0611.qcow2 -nographic`
which is kinda equivalent to using `virt-install --import`

- some of the stuff won't work if triggered over ssh, like `--noautoconsole`
- doing it over ssh by "ssh -t dell "~/vm_create.sh '$unique_name'"" causes issues, it won't be tracked in virsh list -all.


- to make the thin image trackable on virt:

```sh
virsh define f17vm2-with-b.xml
virsh start f17vm2-with-b --console
```
## virt-install

interesting flags:

--unattended
--print-xml

for more info: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-guest_virtual_machine_installation_overview-creating_guests_with_virt_install#sect-Guest_virtual_machine_installation_overview-virt_install-network_installation 

## virsh

`virsh <start, shutdown, suspend> <vmName>`
`start --console`
`console <vm_name>` connect to an already running vm

```sh
virsh attach-interface --domain myvm \
  --type network --source default \
  --model virtio --config --live
```

```sh
virsh detach-interface myvm \
  --type network \
  --mac 52:54:00:xx:xx:xx \
  --live --config
```

```sh
virt-customize -a MY-CLOUD-IMAGE.qcow2 \
    --root-password password:SUPER-SECRET-PASSWORD \
    --uninstall cloud-init
```

to see list of assigned network: `virsh domiflist noble-072812.0612`

### erros

`virt-customize: error: libguestfs error: guestfs_launch failed.` means the vm is running, it should be stopped.

[[Linux storage]]
