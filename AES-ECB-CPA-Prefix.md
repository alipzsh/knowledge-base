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

add to the flag until it's length equals to the length of one block, 16.
then go for the second block by