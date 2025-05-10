automation methods:

fuzzing and payload injection:

- have a list of all the payloads
- use headless browsers: selenium, puppeteer or playwright (specially for DOMs)
- optionally use ffuf, nuclei
# XSS

- look for points of data entry:
	- https requests
        - headers
        - different parts of the URL (query, params, frags, ...)
	- url query strings

- look for exit points:
	- all possible http responses (any kind of user, with any privilege)
	- audit logs

- find the links between entry and exit points.

- enter random values to entry points and check the exit points, immediate http response for
  reflections or if the value is stored and reflected somewhere else.

then revise and automate the exploitation part.

# DOM based

1.

- look for html sources.
- insert a random string and see where the string is reflected.

2.

- if the string isn't reflected in the DOM, look into JS codes for possibility of a sure
  value is passed to a sink.

# reflected and stored DOM XSS
