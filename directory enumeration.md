
`ffuf -u <url/FUZZ> -w wordlist.txt` and `-fc <status_code>` to exclude
##### cleanup:

`cat * | grep -E 'Status: (2[0-9]{2}|3[0-9]{2})' | awk '{print $1$2$3}' | sort | uniq > final`