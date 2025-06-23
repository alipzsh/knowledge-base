# XSS

taking advantage of web application executing scripts on user's browsers.

finding the functionalities where user changes some part of the applications
code that is then executed (dynamic scripts) and changing it.

# XSS types:

* [[Reflected XSS]]: the malicious script originates from the current HTTP request reflected by a
  server. (in request and reflected by server)
* [[stored XSS]]: the malicious script is first stored in the website's database, then executed. (in
  database)
* [[DOM-based XSS]]: the vulnerability exists in client-side code (the browser) and is executed
  there. (stored and executed in the browser)

[[exploit XSS]]
[[XSS html tags]]
[[bypass xss filters]]
[[HTML attributes]]
[[DOM based manipulation]]: a little more on XSS

# BLIND XSS:

try making the victim’s browser generate a request to a server you own:
`<script src='http://YOUR_SERVER_IP/xss'></script>`
If you see a request to the path /xss, a blind XSS has been triggered!