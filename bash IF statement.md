
`[ string1 = string2 ]` is POSIX compliant, works in python's subprocess, `[[ == ]]` doesn't.

# Flow Control with `if`

to evaluate the exit status of a command, like grep:

`if true; then <...> else <...> fi`


* test:
  test expression
  [ expression ]

`if [ $(grep -c "Baeldung" /projects) -eq 1 ]`

  returns: 0,1

* file expressions: to evaluate the status of files.

```bash
if [ -x "$FILE" ]; then
  echo "$FILE is executable/searchable."
elif [] ;then
else

fi
```

* string expressions

* integer expressions

```bash
  if [ $((INT % 2)) -eq 0 ]; then
    echo "INT is even."
  else
    echo "INT is odd."
  fi
```

* `if [ $? -eq 0 ]; then` checks the exit status of the previous command

* `$$` contains the current process's ID.

This is useful when you need to create temporary files for the script. If you
have multiple instances of the same script or program running at the same
time, each might need its own temporary files. In this case, you can create
temporary files named `/tmp/script_name_$$` for every one of them.

* one liner: `if [ a == a ]; then echo "t"; else echo "f"; fi`
