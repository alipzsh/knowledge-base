
* [[bash get first characters of a string]]

* Print n characters: `printf '=%.0s' {1..100}`

* get length of a string: `echo ${#a}`

* to check if a command returns true:

```bash
if tmux ls &>/dev/null; then
    echo "tmux session exists"
else
    echo "no tmux session"
```

- instead of tr:

tab seperated into comma seperated: `paste -sd, bgp`