# Reflected DOM XSS

- sources can also get data from the website (not just browser).

attack vector is is reflected into the DOM.

  * the data might be placed into a *JavaScript string literal* or a *data item in the DOM*
  * a script writes the data into a *sink*

## EXAMINE:

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
