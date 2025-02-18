# openRedirects

redirection:

the site uses some sort of redirect URL parameter appended to the URL to keep
track of the user’s original location:
https://example.com/login?redirect=https://example.com/dashboard

## referrer based open redirection

referer: an http header. points to the page at which the request was made from.

some sites will redirect to the page’s referer URL automatically after certain
user actions, like login or logout

attacker can have a website with the following code. the user will be
redirected to the login page, then if example.com supports referrer based
redirection, the user's browser would redirect to the attacker's host.

## hunt

check every page and button to see if you are somehow redirected to somewhere.

* look for redirection parameters: `redirect, redir, next`
  and they don't always have straight forward names.

  some pages don't have them in their URL, it's *referrer based*. for these
  look for 3xx response codes.

* google dorking: to find URLs that includes certain keywords.

  `inurl: %3D%2F site: example.com` -> `https://example.com/login?n=/dashboard`
  `inurl: %3Dhttp site: example.com` -> `https://example.com/login?next=https://example.com/dashboard`
  `inurl: redir site: example.com`

* test parameter based: enter a hostname
* test referrer based: redirection happens without URL parameters

  setup a page with this HTML code.
  <html>
    <a href="https://victim_site.com/login">Click here to log in</a>
  </html>

  then click on the link, and find out if you get redirected to your page.

## structure of a URL

`scheme://userinfo@hostname:port/path?query#fragment`

scheme:  http, https, ftp
Userinfo: user:pass
hostname: www.example.com
query: ?search=keyword&sort=asc
fragment: refers to a specific part in the resource; #section1

## bypass protection

* using browser autocorrect: it's there to correct user's typos. helps to
  bypass blocklists

  `https:attacker.com` and `https://attacker.com` are the same.
  `https:\\example.com` and `https://example.com`

* find loopholes in validator logic

  sometimes it looks for the site's domain name in redirect URL. so you can
  create a subdomain with the target's domain name included:
  `?redir=http://attacker.com/example.com`
  `?redir=http://example.com.attacker.com`
  `?redir=https://example.com@attacker.com/example.com`

* data URLs: the scheme portion, are used to embed small files in a URL:
  
  `data:MEDIA_TYPE[;base64],DATA`
  e.g. `data:text/plain,hello!` and `data:text/plain;base64,aGVsbG8h`
  
  which can be used for a redirect URL:

  `data:text/html;base64, PHNjcmlwdD5sb2NhdGlvbj0iaHR0cHM6Ly9leGFtcGxlLmNvbSI8L3NjcmlwdD4=`
  which is the decoded version of this: <script>location="https://example.com"</script>

  at the end this could be used to bypass blocklists:
  `https://example.com/login?redir=data:text/html;base64 PHNjcmlwdD5sb2NhdGlvbj0iaHR0cHM6Ly9leGFtcGxlLmNvbSI8L3NjcmlwdD4=`

* exploiting URL decoding:

  URL decoding: to use non ASCII characters in the URLs.

  using double encoding:

  there might be differences between validator and browser in term of encoding.
  
  for example: `https://example.com%25252f@attacker.com`, if the validator
  decodes this three times, `https://example.com/@attacker.com` will be passed
  because `@attacker` isn't considered the hostname but path.
  but if the browser does it incompletely, it could be `https://example.com%25252f@attacker.com`,
  `example.com%25252f` is considered userinfo part and redirection happens.

  using non-ASCII characters:

  * differences in the way validators and browsers decode.
  * browsers try to find the most similar character, so you can use some
    characters that are fine with validators.

## example

* `<a href="#" onclick="returnUrl = /url=(https?:\/\/.+)/.exec(location); location.href = returnUrl ? returnUrl[1] : "/">Back to Blog</a>`

`/url=(https?:\/\/.+)/`: designed to find and capture a URL that is specified as
a value for the url parameter.

`.exec(location)`:  executes the regular expression against the location object.

`location.href = returnUrl ? returnUrl[1] : "/"` if truthy (i.e.,
a match was found), it redirects to the captured URL, otherwise `/`
