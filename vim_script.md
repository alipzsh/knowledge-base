# vim script

`silent` suppresses the Press ENTER prompt.
`redraw!` refreshes the screen and simulates pressing ENTER.

`system()` runs the shell command and captures its output.
    it waits for the command to finish to give the output.
    to bypass this issue, I could use `job_start()` or somehow save the state of the
    function and call the script again.


`:terminal` opens a new terminal buffer and runs the command inside it.

    works fine: `terminal ./k -s "sql"` but it's just a new terminal not a newbuffer. it
    will be opened in a new vim session

the last two seem to be the better ones.

`if &modified`: Checks if the current buffer has unsaved changes.
`write`: Saves the current buffer before switching.


`normal! T[`: Moves the cursor backwards to just before the `[` character.
`normal! df]`: Deletes from the cursor position up to and including the `]` character.

in my experience this left `[` and `normal! da[` is a better one.


if you want to use a file path

```
let file_path = readfile('pipe1')
execute 'edit' file_path[0]
```

`readfile()` returns a list of lines from a file.
`echo "${matches[0]}"` get the first element of an array in bash.
`winwidth('%')` get the columns length of the window.

`let lines = split(output, "\n")`, now the output is in an array. each line as an element:
csql['51/README.md:# sqlInjection', '79/README.md:# sqlite']` with `len(lines)`=2
