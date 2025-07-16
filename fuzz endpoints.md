endpoint: path to a function.

- flask, node, express, django are route based, there is no document root on the backend.

  meaning that you can't ever download `hostname.com/backup.zip`

- you could use ffuf for normal fuzzing partially.

# how to discover endpoints

- method 1: remove some contents of the request (e.g. cookies) and observe the change in the response.
- method 2: add a character (e.g a) after every separator (/) and observer the changes in
  the response.

  EX:
  `/apassport/web/account/info` // 302, length 0 -> different behaviour than others

# how to fuzz

- partially: least change, one part at a time.

when you encountered: `/api/users/all`
then fuzz for:
- `/api/users/fuzz`
- `/api/fuzz/all`
- `/api/fuzz`
- `/api/users/all/fuzz`

1. hook stuff [[fuzz checking phase]]

# attention
