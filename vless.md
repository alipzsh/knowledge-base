### How to parse vless URLs into 

1. `curl -O https://sublink/vless.txt | base64 -d > decodec_vless.txt'
2. parse it into proper configuration json.
	- it seems only the ones with reality work, but I should test them all anyways.

just copy the default configs from nekoray.

# TODO

## needed functionalities

test the subscription:
	1. how to save outbounds without repeated names.
	2. sort based on delay
	3. use multiple ports on parallel.
	4. remove old tested configs

#TODO: sort based on dealy, add IPs. maybe don't save them in
                    # seperate files? save them in a list? also save a time, so you
                    # know the newer ones.
                    # also you can't just save based on the index, it could be repeated


#TODO: add multiple modes of working: 
			1. input sublink
			2. directly getting a link to test
			3. getting a list of working subs. (ordered based on delay and last tested)
			4. testing the previously working subs again.


- to make it more efficient; while testing, I will pipe the configuration to stdin. also I will have to do this when retesting configurations anyways because I will only keep outbound. (but even if I didn't, there would be much less working configurations to read anyways.)