# encoding

different ways of showing stuff.

to understand/make payloads, bypass WAF, transferring characters to the server.

# html encoding

## using ASCII table

1. HEX: &#x{HEX}: a --> &#x61
2. DEC: &#x{DEC}: a --> &#x97

## not in the ASCII table

3. character reference:

  showing characters that aren't in the ASCII table: > --> &gt;

- html attributes are decoded automatically in the browser: <a href="&#x61" ... --> ... href="a" ...
  (this is perhaps because characters with special meaning need to be encoded in the
  document so they need to be escaped)
- character references get decoded automatically (at least in html attribute)

# Unicode

specially for stuff that aren't in the ASCII table, like other languages: \uxxxx (HEX); a –> \u0061

- Unicode encoded characters are decoded in JS:  \u0061li --> ali

# URL encode

to move data through the network: %{HEX}: a –> %61

`a –> &#x61 –> %26%23x61`

1. html encode
2. URL encode to move in through network
  - you could URL encode `x61` too, but the browser doesn't.

# attention

- to see them you should see the source code of the page, it won't be shown in the dev tools.
