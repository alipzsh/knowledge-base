# stored

app receives data, stores it in the database and and unsafely includes it in
it's *later* HTTP response.

EX:

1. if this payload is embedded in a comment, victim just have to visit the page.

`<script>alert('hacked');</script>`

or it could be in a request:
`postId=3&comment=This+post+was+extremely+helpful.&name=Carlos+Montoya&email=carlos%40normal-user.net`

2. if there is an XSS payload in the title of a video or article in the front page of the site, it would effect people visiting it.

EXAMINE:

1. test all relevant *entry points* and all *exit points*
  * Entry points:
    * Parameters or other data within the URL query string and message body.
    * The URL file path.
    * HTTP request headers
    * out-of-band routes via which an attacker can deliver data into the application:
      * emails into a webmail app

  * exit points:
    * all possible HTTP responses (to any kind of application user in any situation)
    * audit logs (visible to some application user)

2. locate the links between entry and exit points.
  * work through entry points, submit a specific value into each one, and monitor the apps
    responses where the submitted values appears.

    Determine if the observed value is stored in different request or simply reflected.

3. test for a vulnerability:
  * determine the context within the response where the stored data appears and test
 * look for an, appropriate payload.

  with the same methodology as reflected XSS.

EX:

* `<input><script>alert(1);</script></input`

html tag attribute context:
* [[XSS_examples#Stored XSS into anchor `href` attribute with double quotes HTML-encoded| `javascript:alert(1)`]]
- [[XSS_examples#Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped| into onclick event with <>" htmlencoded and '\ escaped]]