
we can access the encryption oracle and get any part of the flag.

find encryption for every character, make a mapping of them.
get the encryption of each character of the flag, one by one, look for it in the dictionary. save the key.

```python
from pwn import *

dict = {}
io = process('/challenge/run')
for i in range(33, 127):
    io.sendline(b'1')
    io.sendafter(b'Data?', chr(i).encode() + b'\n')
    dict[chr(i)] = io.recvline().decode().strip().split(" ")[1]

for i in dict:
    print(i, ":", dict[i])

i = 0
flag = ""
while True:

    io.sendline(b'2')
    io.recvuntil(b"Index? ")
    io.sendline(str(i).encode())
    io.recvuntil(b"Length? ")
    io.sendline(b'1')

    enc = io.recvuntil(b"Choose an action?").decode().strip().split("Result: ")[-1].split("\n")[0] 
    for key, value in dict.items():
        if value == enc:
            flag += key

    print(flag)
    i += 1
```