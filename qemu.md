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

* not sure if qemu could be used to setup an iso and then start it
  through gui. qemu's GUI is much better to use.

  not necessary at the moment but virt-install seems interesting in that case.

  on the other hand I can connect `virt-manager` through ssh which is a
  much smoother experience than x11 forwarding.
  without GUI, the ram usage is lower.

* `virsh <start, shutdown, suspend> <vmName>`

* a VM didn't work in anyway, which was the problem with that one.

  others work fine but I have to wait for them to load all the way.

  it's not worth it to try things on qemu even though it's more pro, but
  the one I tried didn't work on it.

# cloning and snapshots

* a base clone and snapshots.
* really easy from the gui.
* more to learn of the file formats.

# resize the image:

`qemu-img resize vm.qcow2 +10G`
