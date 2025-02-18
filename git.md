# git
* setup git:
  `
  git config --global user.name “[firstname lastname]”
  git config --global user.email “[valid-email]”
  git config --global color.ui auto
  `

  then `git init`

* setup GitHub using ssh:
  `
  ssh-keygen -t ed25519 -C "ali_pzk@yahoo.com"
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519
  `

* change password for an existing key
  `ssh-keygen -p -f ~/.ssh/id_ed25519`


* add the remote repo as alias:
`git remote add notes "ssh url"`

* to put stuff in GitHub:
`
git add .
git commit -m "message"
git push -u <alias|ssh url> master
`
* it should be `git push -u <alias|ssh url> master` the first time and
  then just git push origin

* update the local repo:

  `git pull origin master`

  if there are some changes, you could commit or stash them: `git stash`
  if you want to get the stashed stuff back: `git stash pop`

# to add and change a branch

not the right way, but I created a branch in gui, then changed the default into it, git
init, then git pulled, merged , then removed the old files, and pushed.
