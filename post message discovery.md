Does it even exist?, how to know that we should look for it?

05:01

# read the source code

Reading the source code, looking for *listeners* (e.g. event
listeners) --> might lead to XSS, ATO, CSRF

find --> read --> test if it's vulnerable (it takes a message) --> Dom invader

EX:

1. search for `addeventlistener("me` (the ones that are listening
   on a message) and visually find it --> for XSS, look for DOM sinks in the
   function
2. read the code
   --> look for dangerous sinks (Look into called functions)
   --> try to bypass conditions.
3. [[DOM-based XSS#discovery]]
4. add breakpoints --> trigger it with sth like `window.postMessage("stuff",
   "*")`
   - example payload: `window.postMessage('{"goto":"javascript:alert()"}', "*")`
   - can we somehow give this payload to someone else and it works.  --> send
     the payload, look into DOM invader hoping for a response 05:02 --> DOM
     invader captured --> spoof origin --> send --> if XSS worked
     --> send the payload as POC from
     another origin, to show that it's exploitable (use Dom invader POC).
     (so you'll be able to XSS another browser from your machine)

     - there will be two POCs in the exploit given. window.open and iframe
       (which is mostly blocked, so you can remove it from the POC).

05:02

# using extensions

Issue from previous method: you won't always be able to visually find it? Or
can't invoke that particular function (so it won't be captured in DOM invader?

Solution: DOM invader will capture sent messages. So we wouldn't have to look
manually for so many `eventlisteners` and triggering them.

1. browse the pages, wait for it to capture messages
2. you should be looking into each message one by one
  - abstract the details look into stuff from a high level
  - when looking to understand what a parameter does, notice the most simple
    explanations, try to exploit them based on what they are doing.
3. use log stack trace in DOM invader to find the related JS code.
  - EX, post a message `window.postMessage("stuff")`
  - look into DOM invader, click on log stack trace
  - go back to console, click on the link
  - it could get ugly on the target, so you should look for it manually
4. if you succeeded there was a dangerous sink (and it will only be DOM). We can
definitely control the input.  --> DOM invader captured --> spoof origin -->
send --> send the payload as POC from another origin, to show that it's
exploitable (use Dom invader POC).

  05:02-03
