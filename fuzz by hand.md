follow the least change, don't remove the default values or encode anything (at least at
first).

EX:

- how to work on a URL in the parameter:
  add these and observe the response code and length.

  - `a` after it, before or after the `/`
  - javascript to the start
  - test.com to the start

  EX:
  `/came_from=https://.../acount{a}`
  - `.../?came_from=https://.../acount` 302 --> https://.../account/
  - `.../?came_from=https://.../acounta` 302 --> https://.../acounta/
  - `.../?came_from=test.comhttps://...a/acount` 302 --> `test.comhttps://...`
  - `.../?came_from=https://...a/acount` 302 --> https://...
  in the last instance we encountered a checker function for url validation.
