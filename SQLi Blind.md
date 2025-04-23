# blind SQLi

at this point there is an SQLi but we can't extract info directly because the
application's HTTP responses don't return the result of SQL quires or database
errors.

Examine:

send payloads to trigger conditional responses and observe the behavior:

  * time based:

  focusing on response time difference of different payloads by triggering a time delay.
  if the delay occurs means the query worked.

  - trigger an out of band network interaction

Exploit:

based on conditional responses: boolean, time delays, errors.
## [[SQLi Blind boolean| boolean based]]

injecting test conditions that return either true or false;slowly inferring the
structure of the database.

1. `TrackingId=EGsveqHgcMpxwCB8' AND '1'='1;`
2. `xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm`
3. `' AND (SELECT 'a' FROM users LIMIT 1) = 'a'--` 
4. `SELECT SUBSTRING(password,{index},1) FROM users WHERE USERNAME='administrator') = '{c}' --` to brute-force char by char

## [[SQLi Blind Error Based| Error based]]

## [[SQLi Blind Time Delays| Time Delays]]

## using out-of-band techniques

an app could carry out an SQL query *asynchronously*.

it uses the original thread to process the user's *request* and another to execute the query using the tracking cookie.

the app doesn't wait for the SQL query to return, it's response to user doesn't depend on it, be it an error or the delay.

the query could be vulnerable, but how do we know?

triggering the server to send DNS lookup query to our server.

## exfiltration:

store info somewhere on the local machine:

`SELECT Password FROM Users WHERE Username='admin' INTO OUTFILE '/var/www/html/output.txt'`

then request the file: `https://example.com/output.txt`