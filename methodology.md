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

  assuming:
            - the whole process should succeed
            - parameter should be effective

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
  Q4: why testing different payloads lead to different results?
  EX:
    - `javacript:test` -> failed to execute
    - the modified payload -> successfully executed

  ==> you encountered a [checker function](checker function)
  --> [[devtools]] --> [[fuzz by hand]]
    - at this stage you will find out what the vulnerability can be (e.g. XSS or etc)
      input in DOM sinks:
      - XSS -> only in absolute path (URL)
      e.g. if you can bypass the checks to get redirected to lets say `https://google.com`
      - redirection -> relative path (relative URL)
      because it will be added to a base name that's out of our control.
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
  --> use burp, look into the later requests
  e.g. after you pressed sign in, the credentials were sent with a POST request
  e.g. find that user info were somehow POSTed
  - look into it's headers; e.g. origin.
  => by observing the request and the application's behaviour, we can infer
  whether it was handled by http or JS.
  e.g. after multiple requests we get redirected without a 302 code in the requests.

  ==> if it's JavaScript handled; we infer that:

  1. there is a DOM source that takes the redirect-URL as input
  2. there is a sink that takes us to that URL

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
  - bypass the checks

----

- you notice
  `test@yahoo.com` --> "long number"

  1. It's being handled by JS

  Q1: how the application passes data?
  1. values are not plain-text
  2. custom encoding or encryption
     => because the value should be recoverable
  3. a function in JS is doing all these


# authentication test

  - enter email:
  test@gmail.com -> already exists -> fail
  test@gmail.com%0a -> success; then in the server side, you will be redirected
  to the victim's page.

  - email gets encoded (an example of stuff being done in house -> a good
    opportunity to test)
  it's a good opportunity to fuzz -> to get unexpected behaviours


  ==

 forget password page

  - send an email

  Q1: is it rate limited?
  Q2: where is the path to the function that's handling the POST request?
  observe the post (always?) in burp.
  Q3: are there any other parameters that you don't know where they came from?
  type
  next -> infer next (URL)
  mix_mode
  fixed_mix_mode
  Q4: look in the reset password link (in the email)

  e.g
  `https://www.capcut.com/forget-password?aid=348188&code=623778¤t_page=&email=fyoumgk%40gmail.com&enter_from=&language=en&type=4&showType=password`
  - be aware that it's a client side link that sends an http request to the
    server -> any change should happen on the server not the client.
    - how to know this? there is react on this route, network request + response
      coming from the server, and the fact it’s about authentication.

  - what does it contain?
  e.g fiddle around with parameters, change them to get an error and more info.
  - is there any repeated element?
  e.g. it might start with the `forget-password` path.
  a `code` section that perhaps identifies the user.
  Q5: threat modelling (what kind of vulnerabilities to test?)
  e.g `next` -> inspect the url
  e.g (threat model) -> (test cases)
    the `code` section is 6 digits -> brute force
                                 -> what would happen if we use another email
                                 with a valid code?
                                   => test it with an email that belongs to us
  Q6: where is the function that's handling `forget-password`?
  search `forget-password` in DOM.
  Q7: what happens when you click forgetpass -> confirm (send link to email)
  button?
  - intercept with burpsuite -> repeater
  --> notice parameters and request body
  e.g body:

  ```json
  mix_mode=1&email=637c6a7068626e456268646c692b666a68&type=31&next=https%3A%2F%2Fwww.capcut.com%2Fforget-password%3Fenter_from%3Dlog_out%26current_page%3Dwork_space&fixed_mix_mode=1
  ```

  --> link poisoning on next should be tested because it's used to build the reset password URL
  sent to the user:
  `https://www.capcut.com/forget-password?aid=348188&code=567477&current_page=landing_page&email=fyoungk%40gmail.   com&enter_from=page_header&language=en&type=4&showType=password`
  -->  [[fuzz by hand.md]] least change, modify for e.g. `next`
  `...capcut.com...` -> `...acapcut.com...`
  --> observe
  - we notice that even though we changed the URL, we get an email invalid error
  test -> insert your server's address, see if anything comes


  * notice that the email will be parsed differently in html that lets say
    python or curl.
    e.g. `https://www.capcut.com@www.capcut.com/`

  Q8: how are the order of the checker functions and other functionalities
  (e.g sending recovery email, rate limits)?
  * there could also be rate limit before either
  we won't be able to use some tools like recollapse if it's before 1.
  EX: in this case
  1. *checks* the URL
  2. sends the forget pass email

  --> burp intruder -> 1-1000 at the end of the body -> custom concurrent 2-3
  * we want to test the [ratelimit](ratelimit.md) behind the checkerfunction => we should do the
  payload that we somehow get stuck in it
  --> in this case we notice there is a rate limit behind 1

  Q9: what to fuzz by hand?
  - in this case we should bypass [URL_validation](URL_validation.md)
    `https://www.capcut.com@www.capcut.com/forget-password?aid=348188&code=567477&current_page=landing_page&email=fyoungk%40gmail.com&enter_from=page_header&language=en&type=4&showType=password`

    - .com.attacker.com
    - .com@attacker.com
    - .computer

  08:06 26

  --> so we notice that it checks for the valid host
    => it's either regex or URL parsing

  - is it checking for a fixed string?
    hand fuzz and infer:
    - is it accepting string with the fixed part intact?
    - or is it checking the whole thing.
    no.

  %40    -> OK, but not redirected to evil.com (not bypassed)
  %5c%40 -> error
  %23%40 -> error

  --> take the one that worked (e.g email sent) and work more on that:
  e.g add `a`, `%01` to the start:
  - `%01https://....` -> error
  - double url encode:
  `..:pass%25%5c..` -> ok `..:pass%5c@..` but didn't bypass
  - `..:pass%23%5c..`
  - `www.evil.com%40google.com%40www.capcut.com` ->
    `www.evil1.com%2540google.com@www.capcut.com`
    * we notice that it added a %25 to our valid input.
    * this is an example of change after checker function, which is a very
      interesting test opportunity.
  - `www.evil.com%26%23x25%3b%40www.capcut.com` -> fail
    * we expect this to take us to google.com but no it doesn't.
    * &#x23 -> JavaScript is encoded in html attributes (?)

  * test these is jsfiddle.com to see if it's ever going to work:
    `<a href="https://google.com&#x23;@capcut.com">click</a>`


  Q: why are we not getting anywhere even though we did in `jsfiddle.com`?
  it's x-www-form-urlencoded -> the webserver decodes the input before the
  checker function.
  --> the function get `www.evil.com&#23;www.capcut.com`
  --> then drops `www.evil.com&#23;`

  --> also try other email providers

  --> at this point try other payloads

  --> move on to other tests
  url/path

# how to know whether there is a reverse proxy

reverse proxies manage different path's differently

to find them.

e.g /passport/.../.../.../

--> start from the last path, add a character (e.g a)
--> we expect to get permission denied --> handled by reverse proxy (internal
API)
--> if we get not found --> handled by client side (react / vue)

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
