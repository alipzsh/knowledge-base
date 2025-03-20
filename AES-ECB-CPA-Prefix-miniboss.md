build the codebook using the preifx: use the first 15 characters and brueforce the rest.

we can append stuff to the flag.
we will isolate a character at a time, then brute-forcing a single block, comparing these two.


```python
from pwn import *
from base64 import b64decode, b64encode


io = process('/challenge/run')

prefix = 'AAAAAAAAAAAAAAA'
flag = ""
m = 0
n = 16

io.recvuntil(b"Data? ")

while True:

    io.sendline(b64encode(prefix.encode()))
    enc = b64decode(io.recvuntil(b"Data? ").decode().strip().split("Ciphertext: ")[-1].split("\n")[0])

    for i in range(33, 127):
        bf = (prefix+flag+chr(i))[-16:]
        io.sendline(b64encode(bf.encode()))
        pof = b64decode(io.recvuntil(b"Data? ").decode().strip().split("Ciphertext: ")[-1].split("\n")[0])

        if enc[m:n] == pof[:16]:
            flag += chr(i)
            if len(flag) % 16 == 0:
                m += 16
                n += 16
                prefix = "AAAAAAAAAAAAAAAA"
            break

    prefix = prefix[1:]
    print(flag, len(flag))
```