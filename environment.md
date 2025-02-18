# environment
* some programmes look for values stored in the environment.

* set shows shell and environment variables and shell functions.

* view variable's value:
 `
 printenv USER
 echo $HOME
 `
* see aliases: `alias`

* some environment variables:

 `TERM`: the protocol to be used with terminal emulator

* on login, bash reads *startup files* (defines the default environment
  shared by all users) and then startup files in the home directory.

* two type of shell sessions:
 * login shell: being prompted for username and password, e.g in virtual
  console sessions.

  configuration files:
  `/etc/profile` global

  and one of below:
  `~/.bash_profile`
  `~/.bash_login`
  `~/.profile` default in Debian-based

 * non-login shell: a terminal session in GUI.
  `/etc/bash/bash.bashrc` global
  `~/.bashrc`

  * non-login shells inherit the environment from their parent process,
  usually a login shell.
