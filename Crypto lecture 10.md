
if we are going to break a double encryption we will have to do $2^{112}$ multiplications.

Q: could we find $K_L$ and $K_R$ separately? then we would have $2^{57}$

## meet in the middle attack

**phase 1**: search through all $K_1$

in the first index, $K_L$ is all zero and the last one is all one.

we will need $2^{56}$ encryption and $2^{56}$ storage locations.

**phase 2**: decrypt from the other side and go to the middle.

![[Pasted image 20250312042720.png]]

$y_i$ is the ciphertext.

![[Pasted image 20250312043007.png]]

we are looking for matching values. to see if the result of the right
computation is in the table (if it's a collision):

![[Pasted image 20250312050228.png]]

then these keys could be ($K_L$, $K_R$).