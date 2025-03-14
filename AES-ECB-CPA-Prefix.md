in this challenge we have the ability to *prepend chosen plaintext to a secret
before it's encrypted*.

find out the block size: the plaintext size will jump.

```python
data="A"
for i in range(1,50):
    io.sendline(b'1')
    io.sendafter(b'Data?', (data).encode() + b'\n')
    enc = io.recvline().decode().strip().split(" ")[1]
    print(i, enc)

    data += "A"
```


flag: G8MTw139J+/J2QpCVQ0OXqnK4dCSdTOH5720meTMasE=
flag[:16] block 1:  pwn.college{prac => G8MTw139J+/J2QpCVQ0OXg==
flag[:-5] block 2: tice} => qcrh0JJ1M4fnvbSZ5MxqwQ==

two issues: the plaintext is 21 characters long, why the enc is 44, instead of 32.
second: why the cipher text can't be splitted into two seperate blocks.

it's base64 encoded: the issues is that I remember trying it, but it wasn't it.
but I did it now (after HOURS of trying) and it was. so there wasn't anything
more to it.


```python
from pwn import *
from base64 import b64decode

io = process('/challenge/run')

flag = ""
prefix = "AAAAAAAAAAAAAAA"

m = 0
n = 16

while True:

    io.sendline(b'2')
    io.recvuntil(b"Data? ")
    io.sendline(prefix.encode())
    enc = io.recvuntil(b"Choose an action?").decode().strip().split("Result: ")[-1].split("\n")[0]
    enc = b64decode(enc)


    for i in range(33, 127):
        io.sendline(b'1')
        bf= (prefix + flag + chr(i))[-16:]
        io.sendafter(b'Data?', bf.encode() + b'\n')
        pof = io.recvline().decode().strip().split(" ")[1]
        pof = b64decode(pof)

        if enc[m:n] == pof:
            flag += chr(i)

            if len(flag) % 16 == 0:
                m += 16
                n += 16
                prefix = "AAAAAAAAAAAAAAAA"
				
            break

    print(flag)
    prefix = prefix[1:]
```