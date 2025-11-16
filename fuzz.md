# fuzz

to find alternative values in different contexts.

A kind of brute forcing by making and sending requests to the target.

fuzz to trigger unexpected behaviour; to get hidden resources: files, parameters, headers.

send malformed requests:  `<a href:{FUZZ}javascript:>`

- hidden resources
  - unlinked dir, files
  - dev or testing environments
  - api endpoints
  - configuration files

[06:05]

## [fuzz by hand](fuzz by hand)
## [magic parameters](magic parameters)
## [fuzz files](fuzz files)
## [fuzz endpoints](fuzz endpoints)
## [fuzz inputs](fuzz inputs)
## [fuzz headers](fuzz headers)
## [fuzz JavaScript scheme](fuzz JS schemes)
## [fuzz html tags](fuzz html tags)
## [fuzz checking phase](fuzz checking phase)
## [fuzz over CDN](fuzz over CDN)

# [wordlists](wordlists)

# attention

- make the "least change" possible while fuzzing. modify the existing value, bit by bit in
  different places, don't insert a whole payload all of a sudden.

  ```
  /...test...js //relfection
  /......jstest //error
  ```

- a 403 means WAAF (or whatever) is sensitive to that payload so it's blocking it, the file
  might not even exist on the server.
- infer what's happening based on the path/function you are on ->
  `.../send-code/...` could mean that it's rate limited  because it's se nding
  code (?).
