# AES

each round consists of 4 layers:

1. ByteSub      --> confusion
2. ShiftRow     --> diffusion
3. MixCol       --> diffusion, except the last round
4. Key addition

everything in AES is in chunks of 8 bits (1 byte) and 16 * 8 = 128.

one round consists of 128 bytes.

## ByteSub

1. splits bytes into 4 bytes chunks => A_0 to A_15.
2. each byte is sent into an s-box, which also returns a byte (the initial 8 bits are
   replaced with other values).
3. again, bytes are split into 4 bytes chunks => B_0 to B_15.

## ShiftRow

it's a byte permutation, you will be reordering the byte.

diffusion: if we have x_1 = 000...0 and x_2 = 100...0 (we changed just one bit), we don't
want y_2 to look similar to y_1.

so when you change on byte in the s-box, we want it to spread to other bytes.

I bit flipped in a byte of A_1, translate to 32 filliped bites(?).

## MixCol

bitwise xor with K_i,1 through K_i,16 for each byte.

# byte substitution later (S-Box layer)

$S(A_i) = B_i$

all 16 S-Boxes are *identical*.

based on [table 4.3] if the input is `CZ = 1100 0010` you will get this byte `0010 0101 =
25` out.

but until now we have an S-Box with a nice mathematical description because it could lead to
an attack.
