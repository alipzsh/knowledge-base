
- `/etc/fstab` lists devices that are to be mounted at boot.
- `lsblk -o +MODEL,SERIAL` to list the system's disks

- `df -h` to see filesysmtem size, used and available space
- `vgdisplay` to see unallocated space in the volume group
- `du -h|-s` storage space usage by file

- `mount`
  - list of currently mounted files
  - mount file systems

- monitor logs in real-time
  - `tail -f /var/log/syslog`
  - `journalctl -f`

- `dd` to copy blocks of data.
  - `dd if=input_file of=output_file [[bs=block_size [count=blocks]]`
  - `dd if=/dev/cdrom of=ubuntu.iso`

## creating new filesystem

first create partitions

- `parted /dev/sdd`
  - `print` see the partition table.
  - `rm 1` delete the first partition
  - `mkpart` create a new partition
  - quit

create filesystems

`mkfd -t ext4 -L EXT4_Disk{volume label} /dev/sdd1`

## managing partitions

- `fdisk /dev/sdb`  more on ULSA 20.1
## Extend the Logical Volume

This command assigns all the remaining free space in the volume group to the logical volume.
`sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv`

## Resize the Filesystem

After extending the logical volume, resize the filesystem to use the new space:
`sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv`

- *LVM* for flexibility in managing the root filesystem, and a separate unencrypted /boot. It's a typical Ubuntu full-disk LVM layout.
