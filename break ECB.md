
based on pwn.college


using a codebook mapping:

we can access the encryption oracle and get any part of the flag.

first: find encryption for every character, make a mapping for them
	   get the encryption of each character of the flag, one by one, look for it in the dictionary. save the key.