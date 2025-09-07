1. recognize the architecture of the web server
  - route based
  - document route
  figure these out based on the language and the framework being used.
2. take note of the patterns
  even if the obvious file is safe, the similar ones might not be.
  1. do the checking phase
  2. fuzz for files with ffuf  -w ... -u -mc -fs
  3. search DOM to find the more interesting files

EX:

```
/nofify_count.php  //safe
/FUZZ_count.php    //lowercase
/nofify_FUZZ.php
```

# attention

- fuzz for JS files
- fuzz on various status codes
