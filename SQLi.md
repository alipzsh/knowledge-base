# sqlInjection

finding a functionality that at some point interacts with a database; then
trying to get it to do other stuff than intended.

# EXAMINE

https://portswigger.net/web-security/sql-injection/cheat-sheet

send these, and look for errors, differences or other anomalies in the response:

send payloads that trigger different types of SQLi.

* fuzzing: send multiple sqli payloads and  monitor the responses for possible
code injections.

so you will first identify an entry point to the database, then how you could exploit it.
# types:

maybe most different on the feedback method.

if an application is vulnerable to SQL injection, and the results are returned
within the application's responses.

## [[SQLi Error Based]]

triggers error in the database to collect info: `''+OR+1=1--`

## [[SQLi UNION]]

concatenate queries to get data from other tables in the database.

## [[SQLi Blind]]

if nothing is returned

##  stored sqli (second order):

sometimes the payload might be kept in the database and called later.

## stacked queries

In SQL, multiple statements, separated by semicolon (;) can be
  included in one statement string.

```sql
  SELECT Name, Salary, SSN
  FROM employee
  WHERE eid= 'a'; DROP DATABASE dbtest;
```

in sqlite if the code uses `executescript()`, multiple statements via ; are allowed.

# [[bypass blocks]]

# get more info of the database

infer the database version and type based on the payloads that work.

https://portswigger.net/web-security/sql-injection/cheat-sheet

[[SQLi UNION#get *table information* using UNION based attacks| get table information using UNION based attacks]]
# defenses used against SQLi

  * prepared statements: so that the malicious part doesn't compile and
    treated as an string rather than an executable.
  * allow list
  * sanitize and escape user input

# [[SQLi Routed]]


