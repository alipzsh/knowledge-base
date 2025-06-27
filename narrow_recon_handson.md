- perhaps add only one target to the scope
- to make it more abstracted, look into the requests, remove the complicated ones:
  - get the request URI, add it to target/exclude/File (if it's a file?)
  - after sometime, you will know what requests are uselessly repeated, and are better be
    excluded.

# start answering the questions

- at this point you could figure out if it's a single page web app (lots of JS are loaded
  to build the page) or otherwise.
- technologies?
- authentication class (if this is related to what the remaining page is), e.g.:
  - OAuth: continue with tiktok/google/mobile 
  - pc app: qrcode login, sign in with tiktok/apple/facebook/google
  - credentials
  (each one might be vulnerable and should be tested)
