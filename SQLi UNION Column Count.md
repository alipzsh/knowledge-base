
a 500 response code indicates that there are more columns of data in the
original query => add more `NULL` columns.

1. using `ORDER BY` clause, incrementing the column index until encountering errors, indicating
there is no more.

`' ORDER BY 1--` ,2,3 and ....

2. using `union select null --` and adding more. if the number of NULLs doesn't
match the number of columns, error occurs.

so we append this to the previous request: `'+UNION+SELECT+NULL,NULL--`
