# methodology

Methodology is where to test, what to test.

- determine a workflow of finding bugs.
- learn enough of new things to be able to have a basic setup of them --> then fiddle and
  explore.
- The hunting process: [[bug_bounty]]

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

- parameter
  (e.g. ?redirecturi=num)
  --> [[parameters handling]]
  > DOM
  --> [[find sources and sinks]]
  --> [[DOM-based XSS]]

- a parameter
  --> [[fuzz by hand]]
  --> something out of usual
  --> you encountered a [checker function](checker function)
    - DOM (client-side) -> read the source
    - server-side -> [[fuzz inputs]]
  > DOM
  --> [[find sources and sinks]]
  <--> if it's a [[vulnerable sinks]]
  <--> [[read the DOM]]
    - in this stage you will find out what the vulnerability can be (e.g. XSS or etc)
    - XSS -> only in absolute path (URL)
    - redirection -> relative path (relative URL)
  --> [[fuzz by hand]], try different inputs
  --> [[fuzz JS schemes]]

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
