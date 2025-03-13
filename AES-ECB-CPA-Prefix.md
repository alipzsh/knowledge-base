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

prefix = "AAAAAAAAAAAAAAA"
flag = ""

while True:

    io.sendline(b'2')
    io.recvuntil(b"Data? ")
    io.sendline(prefix.encode())
    enc = io.recvuntil(b"Choose an action?").decode().strip().split("Result: ")[-1].split("\n")[0]
    enc = b64decode(enc)


    for i in range(33, 123):
        io.sendline(b'1')
        bf= prefix + flag + chr(i)
        io.sendafter(b'Data?', bf.encode() + b'\n')
        pof = io.recvline().decode().strip().split(" ")[1]
        pof = b64decode(pof)

        if enc[:16] == pof[:16]:
            flag += chr(i)
            break

    print(flag)
    prefix = prefix[1:]
```

pwn.colleg 10 16 0
prefix:AAAAA 5 b'n-\xd5^\x050F\x16\x1e6\x93\x0c/\x9f\x97h' 32
pwn.college 11 16 0
prefix:AAAA 4 b'i\x19\xdb\xe2*\x82\x13koGL\xfb\xa7n\xa7t' 32
pwn.college 11 16 0
prefix:AAA 3 b'\x98\xa2\xc0^2d>\x15;\xd4\x0c\xf8\xd5\xc8t\xcf' 32
pwn.college 11 15 15
prefix:AA 2 b'\ni6\x9b\xd2\t[9\x10\x99\x80\x8e\xa3\xa3\xe9q' 32
pwn.college 11 14 14
prefix:A 1 b'\x1a\xa1U\xe0\xbe\x9e\xce\nbX\x82\xd7\xcb\xab`W' 32
pwn.college 11 13 13

after somepoint len bf reduces which it shouldn't and we won't go further.