# crypto

## XOR

XOR is commonly used because it's self-inverse it means if we do it twice (enc and dec), we
will get the input back: `5 ^ 9 == 12` and `12 ^ 9 == 5`.

`print(0b1011)` => `11` translates to decimal.
`str(n)` does the same
`hex(n)` translates to hex
`bin(n)` to binary
`int(s, base)` string to base
`int(s, 0)` auto identifies based on prefix
`ord('A')` char to ASCII
`chr(100)` ASCII to char


use `strxor` to xor two strings in python: `strxor(x.encode('utf-8'), y.encode('utf-8'))`
`strxor` works in bytes.

`str.encode()` => returns an object of type bytes.
`b64encode()` works in bytes
`b'string'` and `"string".encode()` are the same.

## HEX

decimal doesn't have clean bit boundaries. A single binary digit (bit) can represent two
values (0 and 1), and so on, which makes translation difficult.

we use hex instead. Unlike decimal, where you'd have to memorize 16 mappings for
4 bits and 256 mappings for 8 bits, with hexadecimal, you only have to memorize
16 mappings for 4 bits and the same amount of mappings for 8 bits.

[use](66/README.md#hex,-binary,-decimals)

## Unicode

is a text encoding standard. each character was represented as a code-point. The
code-points were written as: U+0063.

code points needs to be represented in memory as a set of code units, and code
units are then mapped to 8-bit bytes.

The rules for translating a Unicode string into a sequence of bytes are called a
character encoding, or just an encoding.

in python every string is a Unicode, `chr()` takes a Unicode code point and
returns a Unicode character: `chr(57344) => '\ue000'`

u is a string that contains two Unicode characters. this returns bytes. 

```py
>>> u = chr(40960) + 'abcd' + chr(1972)
>>> u.encode('utf-8')

b'\xea\x80\x80abcd\xde\xb4'
```

this will output ASCII if available, otherwise this hex.

why it's represented in bytes not directly Unicode?

Unicode is an abstract standard; it doesn't define how characters should be
stored in memory or transmitted. Instead, we rely on encodings like UTF-8,
UTF-16, or UTF-32 to actually serialize Unicode into byte sequences that
computers can store and process.

* we encode Latin using ASCII, each character has a code.
* encode Unicode using UTF-8, each character has a code point.

python's `input()` returns Unicode.

## UTF-8

UTF-8 is one of the most commonly used encodings. 8 means that 8-bit values are
used in the encoding and it uses up to 4 bytes.

## Base64

is an encoding scheme that uses 64 distinct characters n the output.

## one-time pad

encryption and decryption by XOR-ing the secret and a key.
it's secure unless the key is exposed.

you simply have to use `strxor`, but be careful that it might have used other encryptions
too (like `b64`).

len of key and plain text should be the same.

## many-time pad

is a vulnerability in one-time pad. if a key is used more than once, you could break the
encryption.

when I could see a message but not another:

M_test ^ key = Cipher_test
Cipher_test ^ M_test = key
key ^ enc_flag = flag

or if I can't `https://thecrowned.org/the-one-time-pad-and-the-many-time-pad-vulnerability`

# AES

symmetric, one key for encryption and decryption.

a block cipher; encrypts one block at a time. Which is 16 in AES.

if the remaining block is shorter than 16 bytes, it should be padded.

if the plaintext is longer that 16 bytes, AES *modes* define the ways these separate blocks are considered in the encryption process.

## ECB

each block is encrypted separately with the same key then concatenated together.

```
cipher= AES.new(b64decode("YrJGzJOtABiGd2lzhHyvKw==".encode()), AES.MODE_ECB)
padded=pad(b64decode(enc.encode()),16)
cipher.decrypt(padded)

==> gwn.college{MH-1K7DQ0y8plf83IgTB_c-tkru.dZzNzMDL1gTMxgzW}\n\x06\x06\x06\x06\x06\x06\xbc\t\xb1}\xdc\xa5\xcfv.\xc5\x1c\x00\x86\x81\x95\xcc
```

* I guess I should have un-padded the cipher text.

and then you should ignore the padded stuff.

a crypto system is considered broken if you could figure out the plaintext from
the cipher text.

ECB is vulnerable to *known plaintext* (the attacker knows part or all of the
plaintext) and *chosen plaintext attack* (attacker can manipulate the
plaintext).

because the key is the same in all blocks, the attacker could observe identical
ciphers across different blocks, then map the plaintext to their ciphers.

This process of planting a known-plaintext was called gardening.
`https://en.wikipedia.org/wiki/Chosen-plaintext_attack#In_practice`

a cipher theoretically "broken" if they can find an attack that takes fewer
steps to perform than bruteforcing the key, even if that attack is practically
infeasible.

Encryption oracle: an oracle is any system which can give some extra information
on a system, which otherwise would not be available.

if there is a jump in cipher text length, it will be the block size. EX: if it
reaches 16, and more, the next block should be padded, which makes the cipher
much longer.

a code to [[find_block_size]].

```
17: b'^.,\x16bZy\x94\x95\x85\xd6\r\xea\x98\xf6<m\x0bY\x9c\xf1\xfb\xa5\xe8\xf5\x99\xec\xeeVR\x03' 32

A 1: b'<m\x0bY\x9c\xf1\xfb\xa5\xe8\xf5\x99\xec\xeeVR\x03' 16
```

here, after adding an 'A' more than 16 bytes, we can detect it in the new block.

```
hello 5: b'=\xc8R\xdd\x8e\xdb\x1c\x05\x05Vi|\xf8\xfa\xa7\xf3' 16
AAAAAAAAAAAAAAAA 16: b'\xaft@\x99\x96\xb5\xe8\xaf\x9eE\xc2\xcc\xd3;\x86\x05' 16
AAAAAAAAAAAAAAAAhello 21: b'\xaft@\x99\x96\xb5\xe8\xaf\x9eE\xc2\xcc\xd3;\x86\x05=\xc8R\xdd\x8e\xdb\x1c\x05\x05Vi|\xf8\xfa\xa7\xf3' 32
```

here we clearly see separate blocks.

[[ECB-CPA]]