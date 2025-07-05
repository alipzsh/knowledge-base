# find vulnerable sinks

it's a dangerous sink if it get's user input, but not necessarily vulnerable.

use the debugger to add break point and the console to trigger it. you can run that part of
the source code in you own lab/ compare it to the website to get more info on it's internal
workings. then you can workout if it's vulnerable.

- `url = window.location.href;`
if the value is passed to a variable but not used in a dangerous way or is out of the
js function, it's not dangerous.

- `window.location = redirectParam;`
in this case you should find the value that is being passed, if it's user controllable,
that's a hit.
