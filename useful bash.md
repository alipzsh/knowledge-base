
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
 
- `${asns:+-asn $asns}`
conditionally add a string (in this case, -asn $asns) to the command if the variable asns is non-empty.

- `tail -n +2` means:
"Start printing from line 3 onward."

- auto answer prompts:
  - `printf '%s\n' y n n y y n...` 
  - `printf 'y\n' | ssh-keygen -t ed25519 -f "$NAME" -N ""`
  - `yes | ssh-keygen -t ed25519 -f "$NAME" -N ""`
  - `ssh-keygen -t ed25519 -f "$NAME" -N "" <<< y`

- some kind of exeption handling
	- trap
	- functions return certain stuff; and do according to them:
	
	```sh
	create_image() {
	  || return 1
	}
	create_image || { cleanup; exit 1; }
	```