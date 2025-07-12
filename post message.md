# [post message discovery](post message discovery)

# how to know if it's not going to work

- get a unique value/word in the post message
- search it in the whole source
- visually look into all the results
- one by one, put a breakpoint, send the data in the DOM invader, if it's stopped by it,
  that's it, it's the vulnerable code.

# source code reading

reading the parameter sent in the message could helps you in hunting couple of categories.

e.g. by modifying the URL parameter, so that it points to your own server, it might send you something
valuable.

- use log stack trace in DOM invader to find the related JS code.
  - EX, post a message `window.postMessage("stuff")`
  - look into DOM invader, click on log stack trace
  - go back to console, click on the link
  - it could get ugly on the target, so you should look for it manually

# attention

- WAF doesn't work on Post messages.
- in a post message you can request to a page from any origin, the developer should check
  `if (e.origin === location.origin)`.
- `e.origin` and `source.origin` are the protections, we can't forge them, so if these are being checked, it won't work.
- `e.data` is the attacker controllable data.

EX:

`window.location = t.goto;`
then `window.postMessage('{"goto":"javascript:alert(origin)"}', "*"})`
