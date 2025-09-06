# magic parameters

Most useful in finding XSS and DOM XSS.

- on a specific url or subdomain?

## the *exact* parameter could be found on the application.

look into:
  - http requests (in URLs)
  - html form names and ids, etc
  - JavaScript variable names (in a page code).
  - JSON object's keys. `var variable = {key: value}`; both variable and key are parameters.

find parameters:
  - GAP, fallparams
    `fallparams -u url`
  - passive recon --> unfurl
    `cat .passive | unfurl keys | sort -u | grep -v "/"`

- test them in chunks
  [param_maker.sh](param_maker.sh); to make a long string of parameters from a list.
  - after getting params with GAP (or others) and turning them into a chunk
    either in GAP or the script, test them considering the proper chunk size (
    25-40).
  -> if it get's reflected, work on it [[fuzz by hand]] and e.g [[bypass xss filters]]
  -> if didn't get anywhere, remove it and look for another.
    06 06 last 10 mins

## *similar* ones could be found on the application

some params aren't visible, reflected or ... but you can infer them by noticing others.

EX:
- By seeing this `yahoo_home_ui` you might guess `yahoo_home_redirect`
- the `use_local_engine` parameter is reflected in `engine` block. so if there is a
  `frontend` block, we should check for a `use_local_frontend` param.

## completely *new* name

fuzz for parameters that aren't visible, reflected or ....

Use the top 25 parameter (based on a GitHub repo), pick one based on the vulnerability.
then try them like before, e.g. using x8 look for XSS.

[top25_XSS.txt](top25_XSS.txt)
`x8 -w wordlist.txt  -u https://stuff.org`

# attention

- fuzz on different status codes not just 200; don't skip 3XX, 4XX, 5XX, even on
  40#4 (but the one that is created by the web app not the web server.)
- query string parameters can be increased as long as the server handles the
  request => you can test more than one parameters in an HTTP request.
- different structures require different methods of finding parameters:
  * capcut --> react --> rest api (functions) newer, harder
  * WordPress --> document_root older
- modify the fuzzing process based on the situation (list size, threads).
- fuzz on both GET and POST requests
- parameters could be related conditionally, if one doesn't exist, it looks for
  another.
- there are hidden parameters on every page.
- use the same ones on different pages, they might act differently on the other
  pages.
- the page doesn't even load, it means a parameter is messing something and it
  might result in a vulnerability.
- when applying a chunk --> if  403, forbidden => a parameter is messing
  something, find it, (use sqlmap to find out why this is happening).
    - find it --> in a loop, split the parameter in half, try to find and
      exclude the problematic parameter (and possibly exploring the issue
      later).
