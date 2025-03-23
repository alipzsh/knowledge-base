
`https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request`

## get

`r = requests.get('https://api.github.com/user', auth=('user', 'pass')), cookies=cookies)`

look in `sql/*.py`
### add headers

```py
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

## Post

`requests.post(url, data={'content': content})`


URL encoding/ decoding:

```python
from urllib.parse import unquote
```



`requests.Session()` creates a session object that persists parameters like
cookies, headers, and authentication across multiple requests.

```python
s = requests.Session()
url = "http://natas28.natas.labs.overthewire.org/index.php"
s.auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')
r = s.post(url, data={"query": sample})
```