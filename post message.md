WAF doesn't work on Post messages
[[narrow_recon]]

# discovery

Does it even exist?, how to know that we should look for it?

## manually

Read the source code, look for *event listeners*.

- e.g. search `addEventListener("me` (the ones that are listening on a message) and visually find it
- read the code, look for dangerous sinks. Look into called functions and whether you can bypass conditions.
- can you control the input? (use the debugger) --> if it's a [[vulnerable sinks]]
- add breakpoints
- trigger it with `window.postMessage("stuff")`
- look into DOM invader hoping for a response
- DOM invader --> spoof --> send
- you should then be able to send the payload as POC from another origin, to show that it's
  exploitable (use Dom invader POC).

  For more 04

## use extensions

Issue: what if we can't visually find it? Or even if you did how could you invoke that particular
function?

Solution: DOM invader will capture sent messages. So we wouldn't have to look manually for
so many `eventlisteners` and triggering them.

- browse the pages, wait for it to capture messages
- you should be looking into each message one by one
  - abstract the details look into stuff from a high level
  - when looking to understand what a parameter does, notice the most simple explanations,
    try to exploit them based on what they are doing.
- if you succeeded there was a dangerous sink (and it will only be DOM). We can definitely
  control the input.
- DOM invader --> spoof --> send; then it will also be a vulnerability.
- you should then be able to send the payload as POC from another origin, to show that it's
  exploitable (use Dom invader POC, get rid of iframe (look into 05-02)).

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

# note

- in a post message you can request to a page from any origin, the developer should check
  `if (e.origin === location.origin)`.
-  `e.origin` and `source.origin` are the protections, we can't forge them, so if these are being checked, it won't work.
- `e.data` is the attacker controllable data.

EX:

`window.location = t.goto;`
then `window.postMessage('{"goto":"javascript:alert(origin)"}', "*"})`
