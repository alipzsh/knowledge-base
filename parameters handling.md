07 04

intercept it -> if it returns status code, no JS in the response --> not JS

1. whats the status code
2. by observing the request and the application's behaviour, we can infer
   whether it was handled by http or JS.

  - is it acting based on the status code?
  e.g. redirected --> 302? --> HTTP handled (not 100%)
  - if not -> JS => [[DOM based manipulation.md]]

- `.../?came_from=test.comhttps://.../acount` 302 --> test.comhttps://.../account/

- added 'a' at some points

  `.../?came_from=javascripthttps://...a/acount` 302
  --> https://... // get's removed => there is a checker function
  because it's handled by HTTP status code

- if for example you enter an email but a cryptic something is sent, it's
  definitely being controlled by JS.
  => credentials are not plain text

# attention

- JS redirection might happen through UUID, not parameters. look into dev-tools
  network section for fetch, xhr .etc.

  redirection is handled server-side by Cloudflare after JWT verification

  EX:

  - Fetch request: Your browser sends that fetch with the JWT (meta) and cookies.
  at some point I see: `meta.nerdwallet.io?kid=…&redirect_url=…&meta=…` — kid
  identifies the key for JWT verification, redirect_url is where it wants to
  send you after auth, meta carries a signed JWT with session info.

  and then immediately a 302 request.
  - and then I can take the response, save it to a files and load it as much as
    I want to inspect it.

  - this didn't show easily in burp's chromium.
  - I can think of it as: JavaScript embedded in the response that sets window.location to the target URL, or similar
