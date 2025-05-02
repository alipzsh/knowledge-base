### How to parse vless URLs into 

1. `curl -O https://sublink/vless.txt | base64 -d > decodec_vless.txt'
2. parse it into proper configuration json.
	- it seems only the ones with reality work, but I should test them all anyways.

just copy the default configs from nekoray.

# TODO

## needed functionalities

test the subscription:
	1. keep the ones that work
	2. sort based on delay
	3. save the working ones somewhere
	4. will need to test them later, so load and test them so:
		1. don't test them immediately after parsing and save them/ load them first?
	5. keep the static parts separate, so when testing, you could use multiple ports in parallel, also easier save and load.
		

update a subscription:
	1. only parse/ test new configurations, not the ones that are already tested (removed or not)