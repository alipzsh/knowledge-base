# SUID
SUID and SGID are special permissions because they allow for
additional permissions over the standard user, group, world bits.

`-rw-r--r--. 1 root root 2934 Jul  9 01:12 /etc/passwd`
* `-` indicates file, `l` link, `d` directory
* `root root` file owner group owner

special permissions: SUID (user), SGID (group), sticky(world)
`-rwxrwxrwx` changes to `-rwsrwsrwt` with these permissions on.

## SUID (Set User ID upon execution)

runs executables as the use who *owns* the binary.  it's like running
`sudo <command>`

## DGID 

we become member of the group that has ownership of the file when it is
executed.

If root is the group owner of a binary that has the SGID bit set, we
effectively execute that binary as root – just like with SUID.

## sticky

can only be set on a directory and restricts file deletion. only the
owner of a file (and root) can remove the file within that directory.
e.g /temp directory.
