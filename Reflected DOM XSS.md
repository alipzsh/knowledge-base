# Reflected DOM XSS

a type of DOM that goes to the server and back.

pure DOM XSS is an entirely client-side issue, payload inserted into the page.
reflected XSS is a server-side issue, payload reflected into the HTML.

sources can also get data from the website (not just browser).

website reflect URL parameters in serve's HTML responses (happens in normal XSS)

RDXSS: attack vector is client side, interacts with the server then is inserted
into the DOM:
  
  * server processes the request
  * echoes the data into the response
  * the data might be placed into a *JavaScript string literal* or a *data item
	  in the DOM*
  * a script writes the data into a *sink*

* `eval()` function evaluates JavaScript code represented as a string and
  returns its completion value.

  `'var searchResultsObj = ' + this.responseText`

EXAMINE:

1. see the requests made to the server after submitting the input.

2. the response could be different based on the server's actions.

EX:

if it's a `JSON` object:
`{"results":[],"searchTerm":"<script>alert(1);</script>"}`

payload: `\"}-alert(1) //`

* `\` is there to bypass the `\` the server adds to escape the double quote.
* `\\` is there to  to comment out the rest.

result:

`{"results":[],"searchTerm":"\\"}-alert(1) // {\\""}`