# reflected:

immediate reflection of user's data (from http request to the response).

processed in the server, returned to the user without being stored in the
database.

EX:

1. the page relies on the user input to construct the page, e.g. on displaying
search results.

`https://example.com/search?q=<script>alert('hacked');</script>`

2. `https://insecure-website.com/status?message=All+is+well`
results `<p>Status: All is well.</p>`

EXPLOIT:

* send a malicious link and somehow send it to the victim (via email, or ad for example)
* placing links on a website controlled by attacker.

EXAMINE:

1. look for every entry point/ input opportunity within http requests:
  * message body
  * headers
  * URL :
    * fragments
    * parameters
    * query string
    * file path
  * you might be able to edit the *request* parameters, even if there there isn't an input
    method on the website.

2. submit random values:
  * determine if it's reflected in the response
  * it should be short and only alphanumeric to survive input validations

1. determine the reflection context (where is it reflected):
  * between html tags
  * within a quoted tag attribute
  * a JavaScript string
  or ...

4. insert a payload:
  * send a combination of characters `abc ' " } < > ; // # - ()` to see how they are
    handled.
  * try html tags, look in the documentation for available attributes.
  * Take note of which ones the application escapes and which get rendered directly.
  * based on the context
  * close existing tags.
  * to trigger JavaScript execution
  * keep the random value, then insert the payload before or after it, so you can find it by
    searching the random value in the page source.
  * `<script>alert(1)</script>abc123xyz`, `abc123xyz<script>alert(1)</script>`

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