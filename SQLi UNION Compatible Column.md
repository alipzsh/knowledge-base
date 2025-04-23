
Which columns returned from the original query are of a suitable data type
to hold the results from the injected query.

in each column the datatypes must be the same between the original and injected queries => use `NULL` if / because you don't know the type.

try stuff until you find the correct one.

EX:

- compatible with strings:

`'+UNION+SELECT+'abcdef',NULL,NULL--`, replace it with each NULL in turn.

in oracle, even if you are querying `NULL`, you must specify a valid table:`' UNION SELECT 'a','b' FROM dual--`

* in MySQL the `--` must be followed by a space.

you can get the version like this:`'+UNION+SELECT+BANNER,+NULL+FROM+v$version--`