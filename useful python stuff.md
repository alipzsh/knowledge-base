`.split(" ")` method, splits whenever " ".


Normalize the response and target string by collapsing multiple spaces, tabs, and newlines into a single space:

```py
normalized_response = ' '.join(response.text.split())
target_string = "<div>Welcome back!</div><p>|</p>"
normalized_target = ' '.join(target_string.split())
```

Check if the normalized target string is in the normalized response text:

`if normalized_target in normalized_response:
    print("Match found!")`
Baser encode:

```py
encoded = base64.b64encode(result.stdout).decode("utf-8")
```

`base64.b64encode()`: This function returns a bytes object, not a string.


a set of characters: `charset = string.ascii_lowercase`

- use beautifulsoup to get stuff like this: `soup.find_all('form')`