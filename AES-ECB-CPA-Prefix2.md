
for the previous challenges, I expected the cipher length to jump on 16 as it does when I tried it myself. but it didn't and it does now.

so the solution is simple, just compare the first 16 bytes of the brueforced thingy:
`if enc[m:n] == pof[:16]`