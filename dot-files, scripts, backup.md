- bootstrap scripts for new system setup
- learn Git, learn how to unfuck things.
- read backup in ULAH and TLCL on backup


- do step by step then make chagnes
# dotfiles

- only restore files, not sym. but how to keep track of changes? rsync and git?
- for now, each device should have it's own repo.

# backup and restore (also dot files)

- some files should be backedup to dell, either the main one or an lxc or vm?

- have I ever used the main one for hacking? I don't think so.
	- I can backup none important stuff there, like films/ music
	- and other to an lxc or vm.
	- encrypt it
- backup to usb
	
# system setup

- one file that includes all tools/programs so that a function goes through that and installs everything.
	- use tags to differ installations methods.
# "scripts"

in ~/bin or ~/.local/bin
or /usr/local/bin
#### maybe usefull

cp -rfT: copy and replace silently
rsync: use it instead of scp
	-u only uploads the changed files
	exclude or include files
git: depth
tar: great; for icremental backups or others
