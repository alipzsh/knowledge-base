- ftp-authentication: `tshark -r ch1.pcap | grep -i pass`
- telnet-authentication:

`wireshark -> right click -> follow -> tcpstream`
`tcpflow -r ch2.pcap -C0`
`shark -r ch2.pcap -q -z "follow,tcp,ascii,0"`

- Ethernet-frame:

```
cat ch12.txt | xxd -r -p
echo "Y29uZmk6ZGVudGlhbA==" | base64 -d
```
