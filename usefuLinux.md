# usefuLinux


# vim

search and replace: `%s/<search-phrase>/<replace-phrase>`
* whole file: `:%s/search_pattern/replace_pattern/g`
* multi line: `:{start_line},{end_line}s/search_pattern/replace_pattern/g`

	* ```vi:.,$s/foo/bar/``` ., current line,  $ last line

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

## mirrors

in ubuntu: /etc/apt/sources.list.d, and use https://launchpad.net/ubuntu/+archivemirrors
