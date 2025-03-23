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

        if ci[m:n] == pf[:16]:
            flag += chr(i)
            if len(flag) % 14 == 0:
                m += 16
                n += 16
                prefix = 'A' * abs(n - (len(flag) + 2))
                break
            prefix = prefix[1:]
            break

    print(flag, len(flag))
```

got stuck for a long time over realizing I have to more precisely count the prefix for later blocks.