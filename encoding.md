showing stuff in some other way.

# html encoding

## using ASCII table

1. HEX: `&#x{HEX}`: a --> &#x61
2. DEC: `&#x{DEC}`: a --> &#x97

## not in the ASCII table

3. character reference:
  showing characters that aren't in the ASCII table: > --> &gt;

# Unicode

specially for stuff that aren't in the ASCII table, like other languages: `\uxxxx` (HEX); a –> `\u0061`

# URL encode

to move data through the network: a –> %61

# in combination

a –> &#x61 –> %26%23x61

1. html encode
2. URL encode to move in the network
\u0061li
you could URL encode x61 too, but the browser doesn't.

- Unicode are decoded in js:  \u0061li --> ali
- html attributes are decoded automatically: <a href="