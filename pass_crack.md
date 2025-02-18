# pass crack

* ssh2john: convert the key-file into txt that would be suitable for
  john to crack by comparing hashes.

# john (the ripper):

* path to wordlist should be absolute.
`john file.hash --wrodlist=/usr/share/wordlists/rockyou.txt`

crack a `/etc/shadow` hash: [see](80/README.md#pass_crack)

you could use `hashcat`

* hydra: `hydra -L username.txt -P passwords.txt ssh://mercury:22`
  * shouldn't be in quotations.

* use `cyberchef`

* use `https://hashes.com/en/decrypt/hash` to crack and check for known hash algorithms.
