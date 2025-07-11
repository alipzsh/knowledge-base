# HTML context

## out of tags

### use a `<script>` tag
### open a tag + event handler

e.g. `<img/src/onerror=alert(origin)>`

### `<a>` tag  + js scheme

e.g. `<a href=javascripot:alert(origin)>test</a>`

- plus it's HTML encoded variations (get's decoded because it's inside an html attribute).
- combined with character reference. : --> &colon;
- plus Unicode encoded variations only inside js URI.  `<a
  href={htmlencoded}avascripot{character reference}{Unicoded}lert(origin)>test</a>`

### non-executable tags

EX:

[[XSS_examples#Reflected XSS into HTML context with most tags and attributes blocked| most tags and attr blocked]]
[[XSS_examples#Reflected XSS just custom tags allowed| only custom tags allowed]]
[[XSS_examples#Reflected XSS event handlers and `href` attributes blocked| SVG and <animate> allowed]]
[[XSS_examples#Reflected XSS with some SVG markup allowed| SVG markup allowed]]

## into html tags:

if you can close:

1. both attribute and the tag --> [[#out of tags]]
2. the attribute --> use event handlers
3. neither attribute nor tag --> the attribute might be vulnerable, e.g.:
    • `<a href="{}"></a>`
    • `src` in `<iframe>`


EX:

[[XSS_examples#Stored XSS into anchor `href` attribute with double quotes HTML-encoded| `javascript:alert(1)`]]
[[XSS_examples#Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped| into onclick event with <>" htmlencoded and '\ escaped]]
[[XSS_examples#angle brackets encoded| angle brackets encoded]]
[[XSS_examples#Reflected XSS in canonical link tag| canonical link tag]]
 `<>` encoded --> add a new attribute that creates a scriptable context: `" autofocus onfocus=alert(document.domain) x="`
 with angle brackets encoded: `"onmouseover="alert(1)`

## javascript context:

1. close the `<script>` --> [[#out of tags]]
2. break the context, fix the rest: e.g. `'-alert()-'` in `..&userid=name"-alert()-""..`

	closes the `"`, add `alert`, closes the ending `"`, the `-` is mathematical minus.

EX:

[[XSS_examples#Reflected XSS into a JavaScript string with angle brackets HTML encoded| angle brackets encoded]]
[[XSS_examples#Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped| single quotes escaped]]
[[XSS_examples#Reflected XSS in a javascript URL with some characters blocked| some characters blocked]]
[[XSS_examples#Reflected XSS into a JavaScript template literals, with `<>'" ` unicode escaped| '"<> and backtick escaped, js template literals]]


- get event handlers: `Object.keys(window).filter(k => !k.indexOf('on'))`

# an Example

- ignore (abstract away- or atleast don't waste much time on) reflections that are way too
  obvious (everything reflects) and you can't break out.
- if you found a reflection while fuzzing for parameters, get it out and continiue with the
  rest.

then send ", if encoded, send the encoded to see if it get's decoded. if not, got to the
next param by removing it, another one might get reflected.  do the above again.  e.g. you
could also try ?s=something<encodedstuff>test, and see if test gets out of the tag (which
then you should continue based on js contexts).

while doing this so many things could happen, you should resolve them
step by step.

EX:

- if the tag gets removed: you can try other ones, or add one inside it:
<im<img>g>: the idea is that it might remove the first image.
- if you are already inside a tag, try adding an attribute.

06 06, last 5 mins.
