# reflected:

immediate reflection of user's data (from http request to the response).

processed in the server, returned to the user without being stored in the
database.

EX:

the page relies on the user input to construct the page, e.g. on displaying
search results. `https://example.com/search?q=<script>alert('hacked');</script>`

## EXAMINE

1. look for every entry point/ input opportunity within http requests:
  * entry: message body, URL, headers

1. submit random values and look for reflection

2. look for a payload based on the [[XSS contexts]]