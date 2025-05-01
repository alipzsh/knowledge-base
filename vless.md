### How to parse vless URLs into 

1. `curl -O https://sublink/vless.txt | base64 -d > decodec_vless.txt'
2. parse it into proper configuration json.
	- it seems only the ones with reality work, but I should test them all anyways.

just copy the default configs from nekoray.

# TODO

1. modify the incorrect stuff: no security is needed, fingerprint and something else should be in a new part, uTLS.
2. add the parsed url, outbound, to the default config