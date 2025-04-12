# find some HTTP APIs


# find API's verbs:

`curl -i -X OPTIONS https://api.mega-bank.com/users/1234`

=> 

```http
200 OK
Allow: HEAD, GET, PUT, DELETE, OPTIONS
```


# how to find the expected shape by an API:

this is the next step if you know an endpoint exists.

* analyze the structure of known requests (sent via the browser).
* make educated guesses and test them manually.

start with common endpoints: sign in/up, password reset or similar because authentication design is similar between applications. 

## common shapes
### find out the authentication scheme:

applications authenticate your session differently. It’s important to know what
type of authentication scheme you are working with because many modern
applications send authentication tokens with every request. if we can reverse
engineer the type of authentication used and understand how the token is being
attached to requests, it will be easier to analyze other API endpoints that rely
on an authenticated user token.

so next time, we are examining an endpoint but not getting anything for an empty
payload, we should try adding an authorization header to see if there will be
any difference.

### educated guessing

there are public specifications on authentication schemes.

## application specific shapes

recon techniques to slowly learn about the endpoint by trial and error.

* error messages, e.g. `auth_toke not supplied`
* make an account and try it there.
* if you know the variable, brute-force the value, find as many rules about it as possible, e.g. it's length, encoding.

	note: Rather than searching for valid solutions, you may also want to try
	searching for invalid solutions. These may help you reduce the solutions space
	and potentially even uncover bugs in the application code.