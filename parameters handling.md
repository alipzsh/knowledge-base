(perhaps better to be in the main narrow recon under parameters?)
(well it's not fuzzing, it's information gathering or something)

intercept it -> if it returns status code, no JS in the response --> not JS

1. whats the status code
2. Observe the application behaviour
  - is it acting based on the status code?
  e.g. redirected --> 302? --> HTTP handled (not 100%)
  - if not -> JS

- `.../?came_from=test.comhttps://.../acount` 302 --> test.comhttps://.../account/
- `.../?came_from=javascripthttps://...a/acount` 302 --> https://... // get's removed
because it's handled by HTTP status code


