* double quotes escaped:
  * [[Reflected DOM XSS |adding a \ to escape the added \]]
* angle brackets  and double quotes encoded
  * [[XSS_examples#AngularJS expression with angle brackets and double quotes HTML-encoded|exploiting $eval.constructor]]

figure allowed tags and attributes by brute-forcing. 400 vs 200
  * [`GET /?search=<body%20$=1> HTTP/2`](Reflected XSS into HTML context with most tags and attributes blocked.md) 