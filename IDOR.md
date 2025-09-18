
insecure direct object reference: directly referencing the private stuff.
`https://example.com/messages?user_id=1231`

it's essentially a missing access control.
attacker accessing stuff that do not belong to them.

Different IDORs:

* reading other user's information.
* changing data on another user's behalf, like user password.
* when applications reference a system file directly.

**hunt**

* create two accounts on different access levels. one for attack and other the
  victim.

* discover available features.

  pay attention to functionalities that have something to do with user data
  (returning or editing).

* when discovering, capture requests: look for user related data.

* change the IDs in the sensitive requests and check if the information
  returned also changes

## where to look

look for IDORs in password reset, password change, and account recovery
features

look for functionalities that handle the sensitive information in the
application. For example, look for functionalities that handle direct messages,
personal information, and private content. Consider which application
functionalities make use of this information and look for IDORs accordingly.

## example

* `GET /download-transcript/1.txt HTTP/2` so you might do `GET /download-transcript/2.txt HTTP/2`

## bypassing protection

* encoded and hashed IDs:

  the strings might not be random, but encoded, so your payload should be
  encoded too.

  if they are random, create different accounts to find a pattern.

* there might be leaked IDs somewhere in the app.

* force the ID:

  this is how it works for you: `GET /api_v1/messages`
  maybe you could do this for another user: `GET /api_v1/messages?user_id=ANOTHER_USERS_ID`

* Blind IDORs: they might not be direct but elsewhere.

* try different request methods: the protection might not be the same.

* try file types: maybe different authorization.
