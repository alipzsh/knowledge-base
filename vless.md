### How to parse vless URLs into 

1. `curl -O https://sublink/vless.txt | base64 -d > decodec_vless.txt'
2. parse it into proper configuration json.
	- it seems only the ones with reality work, but I should test them all anyways.

just copy the default configs from nekoray.

# TODO


1. add a delay test for each config, and maybe remove things that don't work?
 
2. statistics based on the protocols (reality or otherwise, ws or grpc), so
 that you won't waste time on them later.

3. later on, think of how you could update stuff and not repeat the whole process (should keep track of stuff)
	
4. should I just save it as a list or before splliting it (curl "link" | base64 -d) then diff it?

5. how to make testing faster? use multiple ports? to do them in parallel and perhaps a much better way to store them is not to store the static parts?

6. I will also need to test the working ones every once in a while.

7. save the hash of stuff that wouldn't work? save the hash of everything? to check for update?

8. sort based on delay

9. someway to keep track of stuff, remove them or otherwise if they didn't work.

10. later on, update stuff.