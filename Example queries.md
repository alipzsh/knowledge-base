
`index=main sourcetype="access_combined_wcookie" action=purchase status=200`

all web application events with a successful purchase.

`index=main sourcetype=access_combined_wcookie action=purchase status=200 file=success.do | fields action, JSESSIONID, status`

select only couple of fields, or using `table`:

you can also change the order of the fields.

`index=main sourcetype=access_combined_wcookie action=purchase status=200 file=success.do | table JSESSIONID, action, status`

rename fields:

`index=main sourcetype="access_combined_wcookie" action=purchase status=200 file=success.do | table JSESSIONID,action, status | rename JSESSIONID as UserSession`

using `dedup` at the end will have different results:

`index=main sourcetype=access_combined_wcookie action=purchase status=200 file=success.do | dedup JSESSIONID | table JSESSIONID, action, status | rename JSESSIONID as UserSessions`