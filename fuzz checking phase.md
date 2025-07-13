[[answer these questions#how-does-the-application-pass-data]]

to make sure the output is reliable.

# find a hook

hook: the file we are sure it exists.

1. find files to test on:
  - search for the extension e.g. `.php` or even more obvious `.css`  - browse the app.
3. curl the file `pixiv.net/upload.php`, take note of the status code (e.g 302).
4. check the status code given another filename? e.g. `pixiv.net/test.php`
   - if it's the same --> this file is not a good checking basis.
   - otherwise if it returns another (like 404) --> the app behaves differently given a non
     existent file.
5. find another file from anywhere on the webpage that doesn't give you 302.

at the end:

- upload.php --> 302
- info.php   --> 200
- test.php   --> 404 // wrong files
- 60         --> 302 // ha?

# verify the fuzzing using that hook.

07:02

we expect to find the file we are sure exists.
we should see a difference between the real and arbitrary files.

[wlist-maker.sh](wlist-maker.sh)

1. `wlist-maker upload` makes a list that contains the hook.
2. then use `ffuf ...FUZZ.php -w {thelist} -mc all`, applying the appropriate filter with
   the idea to isolate the hook.

- what if you get a repetitive error? like 302 size 0? (read below) then we will miss even
  the file that we are sure exists.
- only the .php extension returns expected results. when we inspect the headers, the real
  file, redirects us to some real path. but 60, redirects us to /60/ which is bs.  so we
  infer that it takes the files with .php extension.

  - then how to find other extension types? try them first like this one by one.

# attention

- files should be on the same domain.
- it might need to be repeated several times.
