# authentication

# intro

Most vulnerabilities in authentication mechanisms occur in one of two ways:
* applications fail to protect against brute-force attacks.
* Logic flaws or poor coding in the implementation allow authentication bypass. (also known
  as broken authentication).

authentication could give you access to important data in high privileged accounts or just
more attack surface in regular ones.

there are three scenarios to test:
1. password-based login
2. Multi-factor authentication
3. other authentication mechanism

# password-based login

if user account is associated with a unique name and a secret password. account security is
compromised if an attacker is able to get login credentials:

## Brute force attacks

guess valid user credentials. fine-tune brute-force attacks to make more educated guesses.

### Brute-forcing usernames

if they are in a *pattern*, such as email address: `firstname.lastname@somecompany.com`

Sometimes accounts use *predictable* usernames like admin or administrator.

check if you can get *disclosed* usernames; e.g. through user profiles, or
disclosed emails in responses or GitHub pages.

### Brute-forcing passwords

high entropy password can be cracked using the knowledge of human behaviours that
users introduce to the system.

brute force attacks can be more effective with the knowledge of likely
credentials and predictable patterns.

### username enumeration

being able to observe changes in website's behaviour to identify whether a given username is
valid.

on the login page (valid username and incorrect password or on a registration
form (username already taken).

Differences to look for (use exact regex, `diff` and `grep`):

* status code: different ones could indicate something interesting.
* error messages: different depending whether both or just password was
  incorrect.
* response time: something different could be happening and cause difference in
  *response time* whether the password was correct; e.g. an extra step to check
  if the account isn't expired. longer password takes longer to handle.

#### via different responses

checking a list of usernames, then passwords.

the correct username had "incorrect password" in it's response.

#### via subtly different responses

start like the previous one:
a tiny typo could make a difference; a trailing space instead of a dot: `<p class=is-warning>Invalid username or password </p>`

use diff and grep to analyze these.

#### Username enumeration via response timing

the idea here is that for a correct username, the password will be checked, so the longer the password the longer the delay.

use a really long password and the correct username will take much longer to process.

for the password do as before and look for a 302 response code.

### flawed brute-force protection

brute force *protection* is to make it tricky for the attacker to automate the process, slowing down the rate at which he can log in:

* locking the account after too many failed login attempts.
* blocking the attacker's IP address after too many login attempts.

sometimes you are able to prevent your IP being blocked by logging to your
account after every few login attempts.

in this case we will send a correct request after two logins.

### account locking

after suspicious events (failed login attempts).

idea: after trying username dictionary with a dummy password the account didn't get
locked and nothing interesting happened either.
next we try to brute force each username multiple times.

if the attacker just want to access any random account, locking the accounts
could be bypassed.

  * get a list of candidate usernames: user enumeration or dictionaries.
  * list of passwords based on the allowed login attempts.
  * you need a username and one of the three password combination to be true to
    access an account.

### User rate limiting

blocked IP after too many login requests in a short time.

how it get's unblocked:

  * Automatically after a certain period of time has elapsed
  * Manually by an administrator
  * Manually by the user after successfully completing a CAPTCHA

and `x-forwarded-ip` doesn't work.
but we might be able to insert multiple password into one request.

if the request is in JSON format, we can:
`{"username":"carlos","password":["123456",...}`

# multi-factor authentication

some websites might require users to do multiple authentication factors rather than just a username, like 2FA.

## simple 2FA bypass

when a user enters a password and is prompted  for a 2FA code, he could already
be in a logged in state.

so you could try to access the "logged in only" pages after the first step, before even
letting the application send a 2FA code.

first get to know those pages by going thought the app by your own account.

## Flawed two-factor verification logic

after the first step, the website doesn't verify that the same user is
completing the second step:

* first step login `username=carlos&password=qwerty`
* user is assigned a cookie before doing the second step: `Cookie:
  account=carlos`

* which is then used to determine the account the user is trying to login in
  the next step:

  `Cookie: account=carlos 
  ...
  verification-code=123456`

* attacker logs in using their own credential but changes the cookie's value to
  the victim's username and then can brute-force the verification code.

  in this case he doesn't even need to know the victim's credentials. can change to it in the second step.

  you should make sure the user's 2FA had been triggered, before brute forcing it.
  in this case sending a GET request with victim's cookie instead of user's.

  ```http
  GET /login2 HTTP/2
  ...
  Cookie: verify=wiener;
  ```

## Brute-forcing 2FA verification codes

2FA is a short simple code that could be brute forced.

website might *log the user out* if incorrect attempts.

in this case, I was logged out after two attempts.
so we need to automatically log in again.

if I attempt it without logging in again: `"Invalid CSRF token (session does not
contain a CSRF token)"`

HOW it works:

1. *GET `\login`*, is accessible without `csrf` and session cookies
2. Then you have to get the `csrf` and session form previous response and pass it to *POST `\login`*
3. get session and pass it to *GET `\login2`*
4. get session and corf and pass it to *POST `\login2`*

at the end I wrote my own script, got the session Id (of the latest response to
post `\login2`) and set it like this: (after so many attempts, that I figured where I should send it to)

```
GET /my-account?id=carlos HTTP/2

Host: 0afd003c0474a39f8077ad5c002900dd.web-security-academy.net

Cookie: session=iEwNEvwg13UzeXFYDt89A1IjoPWRP9wz
```

# vulnerabilities in other authentication mechanisms

Websites make their login page robust, but they might overlook other related functionalities.
if you can create an account, you can study those like changing password.


## keeping users logged in

When user chooses to stay logged in after closing a browser session, by selecting a checkbox: `remember me` or `keep me logged in`.

Implemented by generating a `remember me` token which is stored in a persistent cookie.

having this cookie allows you to bypass login.

websites generate this cookie in a predictable way, the attacker can make an
account and study it.

it could be incorrectly encoded or the attacker could find the algorithm in case it is hashed.

there might be limits to login attempts but no limits on cookie guesses.

`Cookie: stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw;`

in this case I had to first hash my dictionary, add it like `user:pass` and
base64 encode it.

## offline password cracking

stealing a "remember me cookie" (using XSS or whatever) is the next option if the attacker can't have an account.
the cookie could be studied to find how it's made.

if the website is made using open-source frameworks, cookie's construction details of could be publicly documented.

getting a user's hashed password is a win, it might be available online in a list of well known passwords.

## resetting user passwords

when user's don't know their password's, they can't do password-based
authentication, but there must be a way for them to reset their passwords.

password reset functionality is dangerous by nature.

couple of ways that this is implemented:

### sending password by email

a website might generate a password and send it to user's email.

password sent this way should have an expiration time or the user change it again immediately otherwise this approach is susceptible to man in the middle attack.

### resetting passwords using a URL

more robust but not like this:

`http://vulnerable-website.com/reset-password?user=victim-user`

`?user` could be changed to refer to any username. and will be redirected to the password reset page.

or to make a hard to guess token:
`http://vulnerable-website.com/reset-password?token=a0ba0d1cb3b63d13822572fcff1a241895d893f659164d4cc550b421ebdd48a8`

when going to the URL; the system checks if the token exists on the backed. then it will be deleted after the password reset.

LAB:

the token becomes invalid after password reset.
but we can intercept the request and change the `username` in the body to the desired username.
the rest of the request should be how it should originally be. we shouldn't change the token.

### password reset poisoning

might happen if the *URL is generated dynamically*.

`Host` header could be used to generate a reset password link. Which is not very secure.

check if `X-Forwarded-Host` is supported: you could make it to froward stuff to your server.
this header is supposed to show the original host the request was sent from.
because the `Host` header could be changed along the way, between routers and proxies.

how it helps us?

the `X-Forwarded-Host` has higher chance of being used by the server and if we change it to point to our exploit server, the URL generated that exists in the server's Email, will point to this instead of the actual server.

so; we can change the forgot password request that sends us back the email, to send Carlos an email that contains a URL that is garnered with (pointing to) our evil server.

## chaining user passwords

users enter their current password and then the new password.

these pages use the same functionality to verify users as the regular logins; so they are vulnerable to the same techniques.

if you can access it without being logged in, it gets even more dangerous.

if the username is provided in a hidden field, an attacker might be able to edit this value in the request to target arbitrary users. This could be exploited to enumerate usernames and brute-force passwords.

You should examine the functionality carefully; in this case if the two new password match your account will be locked after two incorrect current passwords. on the other hand if the new passwords don't match you wont and the current password will still be validated.

if you enter two different new passwords, an error message simply states Current password is incorrect. If you enter a valid current password, but two different new passwords, the message says New passwords do not match.

# tips

it's useful if verbose replies in authentication, informs the user of which info was
invalid.
