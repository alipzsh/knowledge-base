when encountered WAF, checker functions, restrictions, validations and etc, do these to
bypass them.

we have no idea what is happening in the back-end so we fuzz.

looking for an unexpected behaviour in a checker function by using special characters in our
inputs.

input: any kind of input; a parameter, a header and etc.

preferred ranges:
  ispecial characters, meaningful ones in the URL.
  - 0x00, 0x2F
  - 0x3A, 0x40 (ASCII table)
  - 0x5B, 0x60

You should have a list and fuzz everything in it.


use recollapse: `recollapse -p 2 -r 0x00,0x2F https://...@google.com/... | grep -v
"com@google"` so that we only get a part we want.

- `-p`: position to fuzz
  - separators: e.g. `:@/.` are important for us.
- `-r`: HEX or DEC, which we should try one by one.

1. create a list using Recollapse
2. use the list in burp intruder (easier because all the headers and stuff are already
   there)
   - URL encode the characters like `//@`
