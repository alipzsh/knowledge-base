
[[Linux storage]]
# qemu

`
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
`

* `virsh <start, shutdown, suspend> <vmName>`

- using virt-install:

file="ISO/debian-trixie-DI-alpha1-amd64-netinst.iso"

NAME=$(basename $file | cut -d- -f1)

virt-install \
  --connect qemu+ssh://dell@ubuntu:4646/system \
  --name $NAME \
  --memory 2048 \
  --vcpus 1 \
  --disk size=50 \
  --cdrom /home/dell/$file \
  --osinfo linux2022 \
  --accelerate \
  --hvm \


to import a prebuilt disk

virt-install \
  --connect qemu+ssh://dell@ubuntu:4646/system \
  --name $NAME \
  --memory 1048 \
  --vcpus 1 \
  --disk /home/dell/$file \
  --osinfo linux2022 \
  --hvm \
  --import


sudo virt-install --install fedora29 --unattended


An install method must be specified
(--location URL, --cdrom CD/ISO, --pxe, --import, --boot hd|cdrom|...)
for more info: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-guest_virtual_machine_installation_overview-creating_guests_with_virt_install#sect-Guest_virtual_machine_installation_overview-virt_install-network_installation 

### using vboxmanage

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