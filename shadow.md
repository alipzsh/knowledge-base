# /etc/shadow

stores the hashed passphrase (or “hash”) format for Linux user account with additional
properties related to the user password.

`username:password:lastchanged:min:max:warn:inactive:expire`

password format is set to `$id$salt$hashed`

The `$id` is the algorithm prefix used On GNU/Linux as follows:

  `$1$`is MD5
  `$2a$` is Blowfish
  `$2y$` is Blowfish
  `$5$`is SHA-256
  `$6$`is SHA-512
  `$y$`is yescryp

EX: `node:!:19053:0:99999:7:::`
`!`: No password is set, so login is not allowed.

# vs /etc/passwd

/etc/passwd could be read by other applications, to make stuff more secure, hashed passwords
are kept in /etc/shadow

* /etc/passwd now has an x for the password field.
* /etc/shadow only shares the first field (the key-field / the user name).
* /etc/shadow has been expanded to contain other password management fields.

