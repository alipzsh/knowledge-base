# (threat model) -> (test cases)

- the `code` section is 6 digits -> brute force

  --> what would happen if we use another email
  with a valid code?
    => test it with an email that belongs to us

- link/url in a request -> ssrf, link poisoning

  --> if the link is used in a way that some important info would be redirected
  to it, then try to modify the link so that it send those info to attacker
  controlled site.

  --> even if the link isn't obvious it must be somewhere in DOM
  --> find it
  --> can you value it by adding a parameter in body?
  (find the parameter in DOM, or fuzz it)

  Q2: what if you remove the parameter?

  - it might read from another parameter
