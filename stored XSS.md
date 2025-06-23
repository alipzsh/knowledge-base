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
  * exit points: all possible HTTP responses, audit logs
1. locate the links between entry and exit points.
  * submit a value in each and monitor the responses.
1. look for an, appropriate payload based on the [[XSS contexts]]