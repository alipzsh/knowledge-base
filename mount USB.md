```
ali@hp:~$ sudo mount /dev/sdb /mnt
mount: /mnt: wrong fs type, bad option, bad superblock on /dev/sdb, missing codepage or helper p
rogram, or other error.
       dmesg(1) may have more information after failed mount system call.
```

```
sudo ntfsfix /dev/sdb1
sudo mount /dev/sdb1 /mnt
```