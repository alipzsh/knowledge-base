# usefuLinux

## qemu

virsh {start, suspend, resume, shutdown?, destroy}
# virtualbox

* get virtual box vm ip:
  `
  vboxmanage list hostonlyifs
  vboxmanage list runningvms
  vboxmanage showvminfo --details <uuid from previous command> | fgrep mac
  vboxmanage dhcpserver findlease --interface vboxnet0 --mac-address=<>
  `
  `vboxmanage dhcpserver findlease --network natnetwork
  --mac-address=08002783e8bb
  `

  or `# nmap -sn 192.168.4.1-254`

* start and shutdown a vm:
  `
  vboxmanage list vms
  "myvm" {e4b0c92c-4301-4a7d-8af8-fe02fed00451}
  vboxmanage startvm myvm --type headless
  vboxmanage controlvm myvm poweroff
  `
* pause and resume:
  `
  vboxmanage controlvm mercury pause
  `

# vim

search and replace: `%s/<search-phrase>/<replace-phrase>`
* whole file: `:%s/search_pattern/replace_pattern/g`
* multi line: `:start_line,end_lines/search_pattern/replace_pattern/g`
* confirm: `:%s/search_pattern/replace_pattern/gc`
* case insensitive: `:%s/search_pattern/replace_pattern/gi`
* in v mode: `:'<,'>s/foo/bar/g`

case insensitive search : add \c somewhere: `:/somthing\c`
go to line: `<number> double g or G>`

# tmux

source configuration inside tmux: prefix, `:source ~/.tmux.conf`

use images in markdown: ![picture of spaghetti](images/spaghetti.jpg)

# Linux

reset xfce panel: `xfce4-panel -r`
grep -r "<something>"
cat links | xargs -n1 -P1 wget
use proxy:
  discord: `discord --proxy-server="socks5://127.0.0.1:2080"`
  chrome: `google-chrome --proxy-server=localhost:2081`

## what to backup

* scp films, music
* backup.sh: commit .dot, notes, projects, to GitHub

1. day.md
2. ssh
3. zet
4. books
5. Documents/backup:
	install.md
	wall
	aahhh.odt
6. bookmarks/passwords


* if wanna be more sure, .dot

1. projects
2. notes
3. dotfiles

### to backup DEll

* turn on penvm
* backup (using backup.sh on local) then clone attack VMs
* every other thing should be in .dot, so run backup.sh

## mirrors

in ubuntu: /etc/apt/sources.list.d, and use https://launchpad.net/ubuntu/+archivemirrors
