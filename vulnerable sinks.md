# vulnerable sink

## first, is it a dangerous sink?

dangerous: if value is passed to a variable.
vulnerable; if you can manipulate the value.

use the debugger to add break point and the console to trigger it. you can run that part of
the source code in you own lab/ compare it to the website to get more info on it's internal
workings.

- even if the checker functions are safe and you can't get a malicious code into a dangerous
  sink to test it, you can change values at runtime to do that, so if you encountered it
  later, you could skip it or otherwise try to exploit it.


- `url = window.location.href;`
if the value is passed to a variable but not used in a dangerous way or is out of the
js function, it's not dangerous.

- `window.location = redirectParam;`
in this case you should find the value that is being passed, if it's user controllable,
that's a hit.
