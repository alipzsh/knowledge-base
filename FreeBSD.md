# FreeBSD

before installing de, install xorg or wayland
`useradd` to add users

* while installing or after installation in `tzsetup` command select UTC ("YES"). in ASUS at
  least.

`mount -uo rw /` if can't do stuff as root

when creating a new user, add it to wheel group so it can use `su -`

## vmware

install `xf86-video-vmware emulators/open-vm-tools` before installing graphical stuff.

add `vmware_guestd_enable="YES"` and `vmware_kmod_enable="YES"` to /etc/rc.conf

perhaps a reboot at this point.

## connect to hidden wifi

network={
    scan_ssid=1 # hidden network
    ssid="YourNetworkName"
    psk="YourPassword"
}

sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
sudo dhclient wlan0

if didn't connect:

sysrc wlans_iwn0="wlan0"
sysrc ifconfig_wlan0="WPA DHCP"
service netif restart

## black screen after boot?

search for the version of `drm` installed.

in my case on 14.2 on ASUS, the newer version (`drm-61-kmod`) cause the issue so I installed (`drm-kmod-510`) from the repos.

`networkmgr`  gives you something like xfce network manger

## DE

lxqt and kde were teary but xfce was fine, but so slow with compositor but better without
it. it seems a little configuration should improve it. if I could get Wayland to work on
even on gnome, I would use it.
wow cinnamon is so much better, fast and without tear completely usable out of the box.
other than x265

bluetooth doesn't work. the card doesn't seem to be recognized, the fake dongle doesn't
work.


x265 is playable out of the box.
hwcodecs=all


## issue installing wayland

couldn't get it to work.

and then tried sddm and cinnamon and couldn't get them to work, until ran startx in the root
and then sddm after a reboot

issue is perhaps because I didn't do these in order.

and for some reason labwc also works now.

## mount USB

`-t msdos` or maybe `msdosfs`?
`mount /dev/da0s1 /homem/ali/usb`

* suspend works, it never did on ASUS in Linux. fans didn't work.
