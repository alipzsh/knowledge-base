To confuse WAF

Originally taken from js for hackers book.

e.g. it's filtering `javascript:`

`javascript\n:` after browser rendering will be the same as `javascript:`

You should fuzz to reach `\n`, then in your payload, you will use the URL encoded of them.
equivalent.

1. `{FUZZ}java{FUZZ}script{FUZZ}:` it could be anywhere.
