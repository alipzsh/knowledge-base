# HTML context

<tag inside>outside</tag>

## [XSS out of tags](XSS out of tags)
## [into html tags](into html tags)
## [javascript context](javascript context)

- get available event handlers in the browser console: `Object.keys(window).filter(k => !k.indexOf('on'))`

also look into [[bypass xss filters]]

# attention

- some obvious reflections (many parameters are all reflected) might not look useful and are
  ignored by automated tools, but could still have something in them, so test them a little,
  but not too much.

06 06, last 5 mins.
