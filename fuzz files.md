1. recognize the architecture of the web server
  - route based
  - document route
  figure these out based on the language and the framework being used.
2. take note of the patterns
  even if the obvious file is safe, the similar ones might not be.
  1. find a hook -> login.php
  2. fuzz -> [FUZZ]User.php -> test based on what it accepts
    - notice the case

EX:

```
/nofify_count.php  //safe
/FUZZ_count.php    //lowercase
/nofify_FUZZ.php
```

# attention

- fuzz for JS files
- fuzz on various status codes
