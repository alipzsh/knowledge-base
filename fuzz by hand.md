follow the least change, don't remove the default values or encode anything (at least at
first).


- `?redirect_url=numbers` --> `?redirect_url=numbers1111` extend the existing payload the way it is
- `?redirect_url=javascript:test`  test the similar but more interesting ones

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

# attention

- always use the least suspicious payloads at first, so you won't get caught by WAF or etc.
  e.g `?redirect=javascript:test` not alert() --> look into devtools for reflection 08:03
