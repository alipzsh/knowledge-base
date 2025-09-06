when you send a post message, an object will be created (e.g e) and captured by an event
listener, you can breakpoint it and get the details on e.

important properties:

- e.source
- e.origin
- e.data (the only attacker controlled)

- a post message is between browsers, but an HTTP post request is client ->
  server

[[using debugger]]

# how to know that we should be working Post messages

[post message discovery](post message discovery)

# how to know if it's not going to work

1. after you Discovered the Post Message
2. get a unique value/word from the post message Data in DOM invader
3. search it in the whole source
4. visually look into all the results
5. one by one, put a breakpoint, send the data in the DOM invader, if it's stopped by it,
  that's it, it's our target function.
6. check if it's actually vulnerable:
  --> look into the conditions
  if there are things like `e.source`, it's probably safe.

- the vulnerability shouldn't have a requirement, the user shouldn't have to click
somewhere


05-03

# attention

- in a post message you can request to a page from any origin, the developer should check
  `if (e.origin === location.origin)`.
- `e.origin` and `source.origin` are the protections, we can't forge them, so if these are being checked, it won't work.
- `e.data` is the attacker controllable data.
- WAF doesn't work on Post messages.

EX:

`window.location = t.goto;`
then `window.postMessage('{"goto":"javascript:alert(origin)"}', "*"})`
