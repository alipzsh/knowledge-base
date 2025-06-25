# fuzz

fuzzing, is a kind of brute forcing like directory enumeration which is
a kind of directory brute forcing, which is done by making and sending
requests to the target (again the same?).

## XSS

at leas in XSS, we are looking for characters that will render the same in browser, so that
they will bypass protections that will look for certain strings, even though they aren't actually the same.

### JavaScript scheme

to confuse WAF

originally taken from js for hackers book.

e.g. it's filtering `javascript:`

`javascript\n:` after browser rendering will be the same as `javascript:`

you should fuzz to reach `\n`, then in your payload, you will use the URL encoded of them.
equivalent.

1. `{FUZZ}java{FUZZ}script{FUZZ}:` it could be anywhere.

### html tags

1. `<img src onerror={FUZZ}alert(origin)>`
2. `<img{FUZZ}src\onerror=alert(origin)>`, what else instead of " "
