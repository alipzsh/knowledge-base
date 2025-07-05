# fuzz

A kind of brute forcing by making and sending requests to the target (again the same?).

- fuzz to trigger unexpected behaviour; to get hidden resources: files,
parameters, headers
  - hidden resources
    - unlinked dir, files
    - dev or testing environments
    - api endpoints
    - configuration files

- send malformed requests:  `<a href:{FUZZ}javascript:>`
- modify the fuzzing process based on the situation (list size, threads).
- make the least change possible while fuzzing.

- different structures require different methods of finding parameters:
  * capcut --> react --> rest api (functions) newer, harder
  * WordPress --> document_root older

## tools

- by hand: trying different combinations
- ffuf
- x8, Arjun
- paramMiner
- ...
[06:05]

## fuzzing for

### parameters

- some parameters are obvious in the code: /?s=something


## XSS

At leas in XSS, we are looking for characters that will render the same in browser, so that
they will bypass protections that will look for certain strings, even though they aren't actually the same.

### JavaScript scheme

To confuse WAF

Originally taken from js for hackers book.

e.g. it's filtering `javascript:`

`javascript\n:` after browser rendering will be the same as `javascript:`

You should fuzz to reach `\n`, then in your payload, you will use the URL encoded of them.
equivalent.

1. `{FUZZ}java{FUZZ}script{FUZZ}:` it could be anywhere.

### html tags

1. `<img src onerror={FUZZ}alert(origin)>`
2. `<img{FUZZ}src\onerror=alert(origin)>`, what else instead of " "
