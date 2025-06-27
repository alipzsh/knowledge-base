# sink

potentially dangerous functions. e.g. not all `innerHTML`s are vulnerable.

most common sinks:
  - window.open
  - window.location
  - window.location.href

  and their variations.

## find dangerous sinks:

it's a dangerous sink if it get's user input

- `url = window.location.href;`
if the value is passed to a variable but not used in a dangerous way or is out of the
js function, it's not dangerous.

- `window.location = redirectParam;`
in this case you should find the value that is being passed, if it's user controllable,
that's a hit.
