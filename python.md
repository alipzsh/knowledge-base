[[useful python stuff]]
[[python requests]]

# The Problem with sh -i in os.system:

`os.system`(and perhaps `exec`) tries to execute `sh` in interactive mode (`-i`), but the environment may not
fully support interactivity for a reverse shell this way. Common issues include:

  * Redirection Behavior: The shell redirection syntax `>&` may not be properly parsed or
    supported in your environment.
  * Shell Differences: `os.system()` invokes the default shell of the system (often
    /bin/sh), which might not have the same behavior as /bin/bash.

* when XORing they don't have to be in the same base: `62 ^ 0x5A`

## interacting with shell:

`output = process.communicate()[0]` used to get the output in a while loop.
using `stdin.write()` is done line [this](66/interact_with_shell.py)

when you want to send something, you should send the whole line, not just the answer part.

`pty.spawn()` to bypass validation [this](66/interact_pty.spawn) which didn't work how I wanted.
