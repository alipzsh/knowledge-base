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

        if len(flag) == 15:
            bf = flag + chr(i)

            if chr(i) == 'c' :
                print("prefix", prefix)
                print("bf", bf, len(bf))
                print("previous pof", pof)
                print("previous enc", ci)
        else :
            bf = (prefix+'|'+flag+chr(i))[-16:]

        post(bf)
        pof = get()
        reset()
             

        if ci[m:n] == pof[:16]:
            flag += chr(i)
            if len(flag) % 16 == 0:
                m += 16
                n += 16
                prefix = "AAAAAAAAAAAAAAAA"
            break
    j += 1

    prefix = prefix[1:]
    print(flag, len(flag))
```

pwn.college{p 13
pwn.college{pr 14
pwn.college{pra 15
prefix 
bf pwn.college{prac 16
previous pof b'w$\xda?1`Ak\x80\x85*#\xf0\x1a\xc6X\xdbz\n\xc9\x9a\x90\r\xb3\xba\xb4\xed\xc6\xbb\x93\x99\x87\t<\xa2\xe9gq\xd2\xce\xfbDj\x8fX\x8f\x1e\xe7'
previous enc b'\xdbz\n\xc9\x9a\x90\r\xb3\xba\xb4\xed\xc6\xbb\x93\x99\x87\t<\xa2\xe9gq\xd2\xce\xfbDj\x8fX\x8f\x1e\xe7'
pwn.college{pra 15
prefix 
bf pwn.college{prac 16
previous pof b'w$\xda?1`Ak\x80\x85*#\xf0\x1a\xc6X\xdbz\n\xc9\x9a\x90\r\xb3\xba\xb4\xed\xc6\xbb\x93\x99\x87\t<\xa2\xe9gq\xd2\xce\xfbDj\x8fX\x8f\x1e\xe7'
previous enc b'\xdbz\n\xc9\x9a\x90\r\xb3\xba\xb4\xed\xc6\xbb\x93\x99\x87\t<\xa2\xe9gq\xd2\xce\xfbDj\x8fX\x8f\x1e\xe7'
pwn.college{pra 15