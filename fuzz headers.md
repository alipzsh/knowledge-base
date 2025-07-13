similar to parameters, using fuff or the burp extension paramminer.

- use param-miner wordlists on GitHub.

- param-miner gives you multiple tabs in the result of suspicious/interesting responses.
- ffuf: `ffuf -w {path to param-miner/headers} -u {hostname} -H "FUZZ: test" -mc all -fs
  406`
  - `-mc`: match all status codes
  - `-fs`: filter response size because it's harder to miss something compared to let say
    filtering a hole status code.
  - gradually filter stuff
