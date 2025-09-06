easy
interact with the application
make a codebook like before
you will get multiple character from the end, add the previous one too and encrypt both using the first number.
so each time, you will need a new code book.

```python
from pwn import *

dict = {}
flag = ""
io = process('/challenge/run')

j = 1
while True:

    io.sendline(b'2')
    io.recvuntil(b"Length? ")
    io.sendline(str(j).encode())

    enc = io.recvuntil(b"Choose an action?").decode().strip().split("Result: ")[-1].split("\n")[0] 

    for i in range(33, 127):
        io.sendline(b'1')
        io.sendafter(b'Data?', (chr(i) + flag).encode() + b'\n')
        piece_of_flag = io.recvline().decode().strip().split(" ")[1]

        if enc == piece_of_flag:
            flag = chr(i) + flag
            print(flag)

    j += 1
```
