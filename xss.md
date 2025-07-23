# XSS

there are XSS in all
- `JSON` (DOM) --> it might update DOM --> go for the function in JS code --> [[DOM-based
  XSS]]
- `multipart/form-data` (either)
- `x-www-form-urlencoded` (either)


- look for XSS where ever there is a reflection:

# how to look for XSS

Discover XS in [[XSS contexts]]

- input opportunity --> [[Reflected XSS]],[[stored XSS]] --> [[XSS contexts]]
- sources -->  [[DOM-based XSS]]
- post messages captured in DOM invader --> [post messages](post message)

- on adding a payload 403? It's a WAF --> [[bypass xss filters]]

# fuzz

At least in XSS, we are looking for characters that will render the same in browser, so that
they will bypass protections that will look for certain strings, even though they aren't
actually the same.

[fuzz JavaScript scheme](fuzz JS schemes)
[fuzz html tags](fuzz html tags)

# more

[[exploit XSS]]
[[XSS html tags]]
[[HTML attributes]]
[[DOM based manipulation]]: a little more on XSS

# attention

- you don't need to URL encode when inserting in browser.
- hunter --> XSS (self) --> exploit
- if you found a reflection while using a chunk of parameters, take it out and continue with
  the rest.
- no matter the content type on the network, it could be vulnerable to xss.
- if a content type is URL encoded or multipart, it could be DOM XSS or other types.
- if content type is JSON, it could only be DOM (it updates DOM).
- if input is reflected in the source code, it's not DOM.
- if not reflected in the source code, it could have been built with DOM.
-
  - `JSON`: api, when it's explicitly sent by JavaScript
  - `x-www-form-urlencoded`: form data, default in forms
  - `multipart/form-data`: files, when there are

  are MIME types that define how data is formatted in HTTP requests. They tell the server
  how to parse incoming data.

[BLIND XSS](BLIND XSS)
