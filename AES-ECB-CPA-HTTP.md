

read the source code and how to get the flag.

If `<query>` is a valid column name in the secrets table, it retrieves the value from that column and encrypts it.

so I have no Idea how these are happening:

```python
import requests
import re

dict = {}
for i in range(33, 127):

    r = requests.get(f"http://challenge.localhost/?query='{chr(i)}'")

    match = re.search(r'(?<=<b>Results:</b><pre>)[^<]+',r.text)
    if match:
        dict[chr(i)] = match.group()

i = 0
flag = ""
while True:
    r = requests.get(f"http://challenge.localhost/?query=SUBSTR(flag, {i}, 1)")
    
    sub = re.search(r'(?<=<b>Results:</b><pre>)[^<]+',r.text).group()
    for key, value in dict.items():
        if value == sub:
            flag += key

    print(flag)
    i += 1
```