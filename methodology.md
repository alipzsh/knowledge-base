# methodology

Methodology is where to test, what to test.

- determine a workflow of finding bugs.
- learn enough of new things to be able to have a basic setup of them --> then fiddle and
  explore.
- The hunting process: [[bug_bounty]]

- xss
  --> trying payloads
  --> observe app's behaviours in removing characters
    - if you found it out, on the client-side, try that part of code in the console 04:03
      (end).
  --> [[bypass xss filters]]

- WAF --> [[WAF confusion#html-encoding-to-bypass-the-waf]]

- reflection --> [[xss]]
- reflection --> search and not in the source --> is made by DOM
  e.g:
  - in JSON content type --> reflected --> not in source --> made by DOM
  - x-url-encoded --> reflected --> in source --> NOT DOM

- domain
  --> [[narrow_recon]]
  --> [[magic parameters]]
  --> unfurl: extract the interesting params (keys)
  --> get URLs with those params

  > reflection?
    --> manual fuzz (least change)
    --> even if safe
    --> similar parameters
    --> XSS

  > [[parameters handling]]
    - JS: go for it and analyze the DOM --> could turn into DOM XSS
    - HTTP status code --> idor , if out of scope, keep and combine

- [[fuzz checking phase]]
  --> [[fuzz files]]
  --> search the founded ones in DOM of multiple pages (dev tools)
  --> the ones that exits there are less interesting
  --> use x8 to find interesting params
  --> found one? maybe SQLi or XSS?

- if `.../?came_from=https://...@google.com/acount` 302
  --> `https://...` (whatever after the @ gets removed)
  --> [[checker function]]
  --> [[fuzz inputs]]

      Q: where could we fuzz to bypass the function?

      in this example before/after the `@`; use [[fuzz inputs]] to fuzz the part inside
      `?came_from`

      in the results of our fuzzing we want to be looking for the results when we are not in
      the else block of our assumption.  which in this case is done through: grep extract ->
      extract from regex -> fetch response and select the `Location: ....` header -> sort
      using the top headers.

      then we can check the ones that match what we were looking for (not redirected the
      main page but google.com).

- fuzz file?
- [[answer these questions]] what is the architecture?
  -->
      `/passport/web/account/info` //200 Data
      `/passport/web/`            // 200 length 164 (not found)
      `/passport/web/account/`   //200 length 164 (not found)

      so it's route based
      otherwise if the app was folder based (?), you could fuzz (?) deeper step by step:

      ```
      /folder1 -> 200
      /folder1/folder2 -> 200
      ```
  --> info would be our hook, look into [[fuzz endpoints]]

- `?errors=<img>`
  --> reflection
  --> payload development
      (look into devtools to see what is going on):
      `<img src>`              -> we notice that it's removing the space between img and src.
      `<img%0Asrc>`            -> this works, and sends to the next line
      `<img%0Asrc%0Aonxxx=>`   -> works
      `<img%0Asrc%0Aonerror>`  -> OK
      `<img%0Asrc%0Aonerror=>` -> WAF
  ==>
      - `<img%0Asrc%0Aonerror{FUZZ}={FUZZ}>`
      - fuzz onerror
      - try <script> or <a> tags instead
      [[XSS out of tags]]

  --> `/?lang=<a/href="aaa">test</a>`        -> OK
      `/?lang=<a/href="javascript">test</a>` -> WAF
      `/?lang=<a/href="Javascript">test</a>` -> WAF

      - so in [[fuzz JS schemes]] we can't use the ones that javascript keyword is intact.

  --> `/?lang=<a/href="avascript">test</a>` -> OK
     - [[encoding]]: html attributes are decoded automatically
     - j --> &#x4A; (html encoded) --> %26%23x4A%3b (url encoded)
  ==> `/?lang=<a/href="a%26%23x4A%3bvascript">test</a>` -> WAF
      - so WAF detects html encoding
      [[fuzz JS schemes]] in the middle: %0a, %0b, %09

  ==> `/?lang=<a/href="javas%09cript">test</a>` -> OK
  ==> `/?lang=<a/href="javas%09cript:test">test</a>` -> OK
      - looking in the console => test is undefined -> JS is being executed

- a parameter
  (e.g. ?redirecturi=num)

  Q1: is the parameter in the game?
  --> [[fuzz by hand]]
  least change
  the most basic payloads
  - e.g if it's a number, add some numbers
  - e.g `javascript:test`:
    - did you get an error in the console indicating test isn't defined? you
      would if it was executed
    - 403? => it was executed => try different payloads
  --> observer the effects
  e.g continue the login process, is the modified parameter still there?
  --> if it is => it's doing something and it's being evaluated
  Q4: why one payload might execute and the other not?
  EX:
    - `javacript:test` -> failed to execute
    - the modified payload -> successfully executed

  ==> you encountered a [checker function](checker function)
  --> [[devtools]] --> [[fuzz by hand]]
    - at this stage you will find out what the vulnerability can be (e.g. XSS or etc)
      - XSS -> only in absolute path (URL)
      e.g. if you can bypass the checks to get redirected to e.g. `https://google.com`
      - redirection -> relative path (relative URL)
      e.g `.../redirecturi?=javascript:test` -> in the code block
      `w='https://URLjavascript:test'` and `H(w)=true`.
  --> [[fuzz by hand]]
  e.g
    ```
    https://URL.com.attacker.com
    https://URL.com@attacker.com
    https://URL.computer
    ```
    and try each in `H(w)`

  1. go deeper and read `H()`
  --> you could try [[fuzz JS schemes]]
  Q5: would fuzz be useful?

  Q6: is the sink even vulnerable?
  - use [[devtools]], directly value the variable. if worked:

  ==> if you can reach that function, you will get a bug

  Q2: how is the parameter being handled?
  [[parameters handling]]
  --> use burp, look into the later request
  e.g. after you pressed sign in, the credentials were sent with a POST request
  e.g. find that user info were somehow POSTed
  - look into it's headers; e.g. origin.
  => by observing the request and the application's behaviour, we can infer
  whether it was handled by http or JS.
  e.g. after multiple requests we get redirected without a 302 code in the requests.

  Q3: does the parameter work even if the condition is true?
  e.g. will there be a redirection even if you are already logged in?

  ==> if it's JavaScript handled; we infer that:

  1. this is an interesting parameter;
  2. there is a DOM source that takes the redirect-URL as input
  3. there is a sink that takes us to that URL

  EX1:
  source -> token
  sink   -> xhr request

  EX2:
  source -> username
  sink   -> print in HTML

  --> [[find sources and sinks]]
  --> [[DOM-based XSS]]
  --> [[XSS contexts]]
  --> understand more of what's going on in the background
  --> [[devtools]] --> [[fuzz by hand]]


  ==> if it's http handled:
  - try to find a reflection.
  - bypass the checks

- you notice
  `test@yahoo.com` --> "long number"

  1. It's being handled by JS

  Q1: how the application passes data?
  1. values are not plain-text
  2. custom encoding or encryption
     => because the value should be recoverable
  3. a function in JS is doing all these


  ----

# attention

- working on a request? google unknown headers.
- sometimes you could add a parameter to get into a JavaScript block.
- you should figure out what to test on an endpoint based on the signs it gives you (e.g.
  errors).
- ask yourself what would you do while reading write-ups.
- add interesting parameters from the write-ups to your wordlists.
- more layers in a functionality --> lower ratio of security mechanisms to layers
- you should choose where you want to work on an app based on whether you think it's going
  to worth your time or not. e.g. Somewhere with lots of user posts is very messy or obvious
  stuff.
- the types of vulnerabilities you should focus on will vary on different application.
