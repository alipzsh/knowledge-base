- perhaps add only one target to the scope
- to make it more abstracted, look into the requests, remove the complicated ones:
  - get the request URI, add it to target/exclude/File (if it's a file?)
  - after sometime, you will know what requests are uselessly repeated, and are better be
    excluded.

# start answering the questions

- at this point you could figure out if it's a single page web app (lots of JS are loaded
  to build the page) or otherwise.
- technologies?
  - VueJS
  - websocket
- authentication class (if this is related to what the remaining page is), e.g.:
  (install all the available apps)
  - web OAuth: continue with tiktok/google/mobile 
  - pc app: qrcode login, sign in with tiktok/apple/facebook/google
  - credentials
  - forget password
    - rate limit
    - there could be a random code/email/aid/type it the URL
    don't test for query strings in the URL, it could become a rabbit hole soon
    or if there were not and it was just a long toke, it could be md5 of it or something
  (each one might be vulnerable and should be tested)
- is the user profile public?
  - you could view it publicly
  - you could edit the profile
  - the profile could be publicly shared; it has a link that has:
    - random string
    - reflection
  - themes
  - settings
    - account info
      - non-editable properties
      - delete account (real interesting)
    - spaces
      - settings
      - create
      - edit
      you should follow this and go deeper
- look for things that might be interesting and you could do a small research on it; e.g.
  websocket
    - it's domain e.g. frontier-sg.capcut.com
    - it's path e.g. /ws/v2
