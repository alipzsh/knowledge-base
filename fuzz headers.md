similar to parameters, using fuff or the burp extension paramminer.
#rs 07 01 => paramminer usage

- use param-miner wordlists on GitHub.

- param-miner gives you multiple tabs in the result of suspicious/interesting responses.
- ffuf: `ffuf -w {path to param-miner/headers} -u {hostname} -H "FUZZ: test" -mc all -fs
  406`
  - `-mc`: match all status codes
  - `-fs`: filter response size because it's harder to miss something compared to let say
    filtering a hole status code.

  - the first time, stop it after a second or two, observer the log
    - filter stuff considering which one gives you the least false negative.
    e.g. status-code 200 -> not good; size 406 -> good
  - gradually filter stuff

# attention

- https didn't give me anything, but http did.
