- bootstrap scripts for new system setup
- Configuration template for machine-specific settings so you could have slightly different stuff on different machines.

## methods of backing up dotfiles

- Git repo: `git init --bare $HOME/.cfg` and some more stuff
- git add .bashrc .vimrc .config/nvim and the rest

this seems good. but how is it different from other stuff.

also add your scripts to `~/bin` or `~/.loal/bin` 

- use symlinks
# where to put scripts
# work on a better backup.

# how to manage other machines? like pen or dell.

managing dotfiles could be a part of something bigger called configuration (cfg)

`git checkout`

Takes the files from your bare Git repo (e.g., .bashrc, .vimrc, .zshrc, etc.)

And copies them into $HOME, overwriting any existing files with the same name

a cfg/setup script


So if you're syncing dotfiles across machines, **`~/.gitconfig` is what you want to track**.

Want to see what’s in it? Run:

```bash
git config --global --list --show-origin
```

So you put them in places that make sense for the type of program you're writing. If you have some things you run for yourself in your user account, like maybe a script to filter your incoming email, that would probably best fit in the `$HOME/bin` directory for your user. For additional software you install, such as Apache tomcat, you might place those in `/opt/tomcat` along with the other tomcat files. For general things that are run system-wide, such as a backup script, that would probably best fit in `/usr/local/bin`.

# traditional .../{s,}bin paths

/usr/bin             An "everyone" script I'll put in /usr/bin
/usr/bin             HOME and I link to them from /usr/bin

/usr/local/[s]bin    For 20+ years I have stored all scripts in /usr/local/[s]bin.
/usr/local/sbin      +1 for /usr/local/sbin
/usr/local/sbin      sudo

/usr/local/bin       /usr/local/bin or ~/bin for user's stuff.
/usr/local/bin       Either $HOME/bin or /usr/local/bin depending 
/usr/local/bin
/usr/local/bin
/usr/local/bin       If the script is actively used as a command in cli
/usr/local/bin       Cron scripts and things like init/systemd helpers

~/bin                /usr/local/bin or ~/bin for user's stuff.
~/bin                Always ~/bin. At least the ones I created. 
~/bin                $HOME/bin
~/bin                Either $HOME/bin or /usr/local/bin depending 
~/bin                personal, not part of a big projet
~/bin                per-user scripts
~/bin                /home/username/bin for me
~/.local/bin         /home/$USERNAME/.local/bin
~/.local/bin         ~/.local/bin/
/home/bin            /home/bin for my server maintenance scripts because fuck you
Home/username        Home/username

/usr/share/bin

# "name" of program/app or similar

/usr/share/name
~/.local/share/name  ~/.local/share/name/.
~/prog/bin           On windows I put them into ~/prog/bin.
/home/MySQL          Things that run under the MySQL login 

# "scripts"

```
~/scripts            % ~/scripts/
~/scripts            A "me" script I'll put in /home/$USER/scripts
~/scripts            I usually have them under /home/username/scripts.
~/scripts
~/scripts

/usr/local/scripts   /usr/local/scripts
/usr/local/scripts   % /usr/local/scripts/
~/Documents/scripts  ~/Documents/scripts.

/scripts             /scripts && chmod 777 /scripts.
/srv/scripts         My backup, setup and maintenance scripts are at /srv/scripts
/support/scripts     /support/scripts
/usr/scripts         /usr/scripts
/opt/scripts         I always use /opt with a dedicated disk and logical volume and then put all scripts in /opt/scripts
/opt/scripts         If the script is actively used as a command in cli it goes in /usr/local/bin. if it's just a script it goes in /opt/scripts
/opt/scripts         On my work systems nothing required for production should reside in users' homedirs so it's either /opt/project/bin or /opt/scripts.

/opt/project/scripts part of a big projet
/opt/project/bin     On my work systems nothing required for production should reside in users' homedirs so it's either /opt/project/bin or /opt/scripts.

/opt                 I always use /opt with a dedicated disk and logical volume and then put all scripts in /opt/scripts

/Scripts             Anything that needs to be run under root I put in a folder called /Scripts
/script              work
/srv/support         /srv/support/, which has bin, sbin, lib, etc., within. It's a project with a git repository. I have Chef pull it from git when building a server and a cron job that does a git pull on it every day to keep it fresh.

/.                   I use containers and just put them in /. Easy to find and inspect when something goes wrong.
~/else               home
~/Desktop            ~/Desktop to be sorted later when I find the time.
```