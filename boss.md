curl -X POST -d "content=hello" http://challenge.localhost:80/
then a simple get request

it gets the POST `content` header, inserts it to a table `db.execute("INSERT INTO posts VALUES (?)", [content])`

what does this do? `return flask.redirect(flask.request.path)`

I don't really get how the post and get should work together, and how it works in the browser and all. but I guess I understood the code.

to reset stuff: `curl -X POST "http://challenge.localhost:80/reset"`

so by posting, getting and resetting, you can kinda bruteforce stuff, like the previous one. but you should consider more stuff, like '|' added between contents.

```python
import requests
from base64 import b64decode

url = "http://challenge.localhost:80/"

def post(content):
    response = requests.post(url, data={'content': content})

def get():

    response = requests.get(url)
    start = response.text.find("<pre>") + 5
    end = response.text.find("</pre>")
    ci = b64decode(response.text[start:end])
    
    return ci


def reset():
    response = requests.post(url + "reset")
    assert response.status_code == 200



prefix = "AAAAAAAAAAAAAA"
flag = ""
m = 0
n = 16

j = 0

reset()
while True:

    post(prefix)
    ci = get()
    reset()

    for i in range(33, 127):

        bf = (prefix+'|'+flag+chr(i))[-16:]

        post(bf)
        pf = get()
        reset()

        if len(flag) == 30:

            print(bf)
            print(pf)
            print(ci)


        if ci[m:n] == pf[:16]:
            flag += chr(i)
            if len(flag) % 15 == 0:
                m += 16
                n += 16
                prefix = "AAAAAAAAAAAAAAAA"
            break

    prefix = prefix[1:]
    print(flag, len(flag))
```

these are : bf, pf, ci

ctice}pwn.collef
b'\x99,\x055\x95\x05\xe6\x1f\xc7\xc6\\\xfc\x8a\x86\x08b]+\x84\xfa\xf7\x87\xb1\xa9\xdeD\xc3\xa3%3Z\xb4\x8f\xf2\xb3\xeb\x88\xb4\x93eu\xc8\xe1\xf8\x86M\x00\x0bg\xe6\x92\xfcj\x8a\x11\xa3=z\xce{\xaa~\x06^'
b'-\x1f\xa8\xc3\xc1\xe9\xb6\xed\x9f\xab\xbau\xa9\xb8\x85\xd6\xca\xd5\x1a\xf6\xd0>\xf2\xbfeZ\x93\xad\x93\xb3J5\xc9\x9du\x8fU\xb9f\xcf;\x12\xe2\x0f;\x11\x99\x1f\xea)\xa9U\xa9\xab\xc4u\xda\xb2e\x18lu7\x88'
ctice}pwn.colleg
b'\x8f\xf2\xb3\xeb\x88\xb4\x93eu\xc8\xe1\xf8\x86M\x00\x0b]+\x84\xfa\xf7\x87\xb1\xa9\xdeD\xc3\xa3%3Z\xb4\x8f\xf2\xb3\xeb\x88\xb4\x93eu\xc8\xe1\xf8\x86M\x00\x0bg\xe6\x92\xfcj\x8a\x11\xa3=z\xce{\xaa~\x06^'
b'-\x1f\xa8\xc3\xc1\xe9\xb6\xed\x9f\xab\xbau\xa9\xb8\x85\xd6\xca\xd5\x1a\xf6\xd0>\xf2\xbfeZ\x93\xad\x93\xb3J5\xc9\x9du\x8fU\xb9f\xcf;\x12\xe2\x0f;\x11\x99\x1f\xea)\xa9U\xa9\xab\xc4u\xda\xb2e\x18lu7\x88'
ctice}pwn.colleh