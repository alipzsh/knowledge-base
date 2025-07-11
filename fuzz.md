# fuzz

A kind of brute forcing by making and sending requests to the target (again the same?).

- fuzz to trigger unexpected behaviour; to get hidden resources: files,
parameters, headers
  - hidden resources
    - unlinked dir, files
    - dev or testing environments
    - api endpoints
    - configuration files

- send malformed requests:  `<a href:{FUZZ}javascript:>`
- modify the fuzzing process based on the situation (list size, threads).
- make the least change possible while fuzzing.

- different structures require different methods of finding parameters:
  * capcut --> react --> rest api (functions) newer, harder
  * WordPress --> document_root older

## tools

- by hand: trying different combinations
- ffuf
- x8, Arjun
- paramMiner
- ...
[06:05]

## parameters

### [magic parameters](magic parameters)
- fuzz on both GET and POST requests
- parameters could be related conditionally, if one doesn't exist, it gets another:

  ```
  if s; then
  ...
  else
     search_product
  ```

- there are hidden parameters on every page.
- use the same ones on different pages, they might act differently on the other pages.
- the page doesn't even load, it means a parameter is messing something and it might result
  in a vulnerability.
- 403, forbidden => a parameter is messing something, find it, (use sqlmap to find out why
  this is happening).


## [fuzz JavaScript scheme](fuzz JS schemes)
## [fuzz html tags](fuzz html tags)
