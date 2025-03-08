
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

what are the top 3 usernames for each category (x_webcat_code_full):
`index=network sourcetype=cisco_wsa_squid | top cs_username by x_webcat_code_full limit=3`

top 3 best selling products:
`index=main sourcetype=access_combined_wcookie file=success.do status=200 | top limit=3 productId`


find the files accessed the least:
`index=main sourcetype=access_combined_wcookie method=GET status=200| rare file by date_month | sort date_month count`

how many items were added to a cart versus being purchased:
`index=main sourcetype=access_combined_wcookie file=cart.do OR file=success.do status=200 | stats count  as Transaction by productId, file | sort productId | rename file as Function`

the number of times distinct sessions were created for users, separated by IP:
`index=main sourcetype=access_combined_wcookie | stats dc(JSESSIONID) as Logins by clientip | sort -Logins`

the total bytes used for the application:
`index=main sourcetype=access_combined_wcookie status=200 | stats sum(bytes) as TotalBytes by file | sort TotalBytes`

the average time for each database query being run:
`index=main sourcetype="db_audit" | stats avg(Duration) as "time to compelete" by Command | sort -"time to compelete"`

what browsers are being used to access the application:
`index=main sourcetype=access_combined_wcookie | stats values(useragent) as "Agents used" count(useragent) as "TImes used" by useragent | table "Agents used", "Times used"`

for each `hostname`, sum of `sc_bytes` field:
`| stats sum(sc_bytes) as Bandwidth by s_hostname`