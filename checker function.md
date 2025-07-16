- checker-function --> valid regex --> 302
- else --> a default value (front page maybe)

EX:

`/came_from=https://.../acount{a}`
- `.../?came_from=https://.../acount` 302 --> https://.../account/
- `.../?came_from=https://.../acounta` 302 --> https://.../acounta/
- `.../?came_from=test.comhttps://...a/acount` 302 --> `test.comhttps://...`
- `.../?came_from=https://...a/acount` 302 --> https://...
in the last instance we encountered a checker function for url validation.
