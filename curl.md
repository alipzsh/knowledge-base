# curl

[[html| how to interpret html code to send a request]]

* send a GET request: `curl <IP>`
* `--header`: http header request
* `-i`: to get headers alongside the response
* `-k`: allow connections to ssl sites without certificates.
* `-s`: silent mode, not to show progress or error messages.
* `--max-time 5`: set the maximum time in seconds that you allow the whole operation to
  take.
* `--user-agent`: set the user agent string to identify the client making the request.
* `-f`: can be used to send post requests by adding multiple *form fields* and file uploads.
  (see aragog.md)
* `-OO /{file1,file2}`: to get both files with their names
* `-X`: change the default request method (GET)

```sh
curl -X POST http://10.10.11.38:5000/upload \
-H "Content-Type: multipart/form-data" \
```
* `-w "%{http_code}" "$url$payload$file"`
* `-s -o /dev/null`: Redirects the response body to /dev/null
* `--path-as-is`: not to merge sequences like `../`
* `-L`: follow redirection
* `curl --socks5-hostname 127.0.0.1:8089 http://sightless.htb` to use socks proxy
* `-b`: request cookies

* http basic authentication: `curl -u username=password -b title=data URL`

* login, save the cookies, then GET the page:
```sh
curl -c cookies.txt -X POST -d "username=guest&password=password&submit=on" http://challenge.localhost:80/login
curl -b cookies.txt http://challenge.localhost:80/

```
	
other useful stuff:
`-F` file
`-d` request body
	* login credentials `"username=admin&password=pass&submit=login" "http://challenge.localhost:80/login`