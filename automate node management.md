
- keep GitHub credentials on the control computer.
	- use `rsync` to setup/backup stuff on/from the nodes
- use ssh to access the nodes


## desktop

### setup

- user setup
- install apps
- configuration:
	- curl dotfiles --> symlink

### backup

- dotfiles are symlinked in a Git repo

- large files (film, music):
	- host (dell)
	- container
	- vm
	
- password/bookmarks (encrypted)
	- host (dell)
	- container
	- vm


# TODO

1. make sure dot files symlink setup is idempotent, with proper error logging and handling
	- a simple way to add dotfiles to be tracked
		- the file could already be at a location, so you should first copy it to the repo, then symlink to it.
2. also dots should be automatically synced to Git in time intervals (a separate script, and cron)