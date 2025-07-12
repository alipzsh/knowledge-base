Does it even exist?, how to know that we should look for it?

# manually

Read the source code, look for *event listeners*.

- for instance search for `addEventListener("me` (the ones that are listening on a message) and visually find it
- read the code, look for dangerous sinks. Look into called functions, check whether you can bypass conditions.
- can you control the input? (use the debugger) check if it's a [[vulnerable sinks]]
- add breakpoints
- trigger it with `window.postMessage("stuff")`
- look into DOM invader hoping for a response
- DOM invader --> spoof --> send
- you should then be able to send the payload as POC from another origin, to show that it's
  exploitable (use Dom invader POC).

  For more 04

# using extensions

Issue from previous method: you won't always be able to visually find it? Or can't invoke
that particular function?

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
  exploitable (use Dom invader POC but get rid of iframe).

  05:02
