
- `/etc/fstab` lists devices that are to be mounted at boot.
- `lsblk -o +MODEL,SERIAL` to list the system's disks

- `df -h` to see filesysmtem size, used and available space
- `vgdisplay` to see unallocated space in the volume group

## managing partitions

- `fdisk /dev/sdb`  more on ULSA 20.1
## Extend the Logical Volume

This command assigns all the remaining free space in the volume group to the logical volume.
`sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv`

## Resize the Filesystem

After extending the logical volume, resize the filesystem to use the new space:
`sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv`

- *LVM* for flexibility in managing the root filesystem, and a separate unencrypted /boot. It's a typical Ubuntu full-disk LVM layout.
