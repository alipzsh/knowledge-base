# stored

delayed reflection of user data.
data is stored, reflected in later HTTP response.

EX:

1. if this payload is embedded in a comment, title:
`<script>alert('hacked');</script>`

2. or it could be in a request:
`postId=3&comment=This+post+was+extremely+helpful.&name=Carlos+Montoya&email=carlos%40normal-user.net`

## EXAMINE

1. test all relevant *entry points* and all *exit points*, e.g.:
  * entry: message body, URL, headers
  * exit points:
    * all possible HTTP responses (to any kind/role of application user in any situation)
    * audit logs (visible to some application user)

2. locate the links between entry and exit points.
  * work through entry points, submit a specific value into each one, and monitor the apps
    responses where the submitted values appears.

    Determine if the observed value is stored in different request or simply reflected.

3. test for a vulnerability:
  * look for an, appropriate payload based on the context of the reflected stored data.

[[XSS contexts]]

EX:

* `<input><script>alert(1);</script></input`

html tag attribute context:
* [[XSS_examples#Stored XSS into anchor `href` attribute with double quotes HTML-encoded| `javascript:alert(1)`]]
- [[XSS_examples#Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped| into onclick event with <>" htmlencoded and '\ escaped]]