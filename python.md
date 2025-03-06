# python

Normalize the response and target string by collapsing multiple spaces, tabs, and newlines into a single space:

```py
normalized_response = ' '.join(response.text.split())
target_string = "<div>Welcome back!</div><p>|</p>"
normalized_target = ' '.join(target_string.split())
```

Check if the normalized target string is in the normalized response text:

`if normalized_target in normalized_response:
    print("Match found!")`
Baser encode:

```py
encoded = base64.b64encode(result.stdout).decode("utf-8")
```

`base64.b64encode()`: This function returns a bytes object, not a string.

# requests

`https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request`

## get

	`r = requests.get('https://api.github.com/user', auth=('user', 'pass')), cookies=cookies)`
look in `sql/*.py`

## add headers

```py
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

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
