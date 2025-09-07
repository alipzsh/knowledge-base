07 04

intercept it -> if it returns status code, no JS in the response --> not JS

1. whats the status code
2. Observe the application behaviour
  - is it acting based on the status code?
  e.g. redirected --> 302? --> HTTP handled (not 100%)
  - if not -> JS

- `.../?came_from=test.comhttps://.../acount` 302 --> test.comhttps://.../account/

- added 'a' at some points

  `.../?came_from=javascripthttps://...a/acount` 302
  --> https://... // get's removed => there is a checker function
  because it's handled by HTTP status code
