# logic flaw

logic flaws are cause by the application failing to anticipate unusual application states
that may occur and, consequently, failing to handle them safely.

## why do logic flaws occur?

### Excessive trust in client-side controls

and not performing proper server-side validation.

how to test: intercept the request and change the price.

```http
POST /cart HTTP/2
...
productId=1&redir=PRODUCT&quantity=1&price=0
```

### failing to handle unconventional input

the application might accept any value of certain data type, but in the perfect case the
logic evaluates it based on business prospective; e.g. preventing users from ordering more
units that are currently in stock.

if there isn't a logic in the application for handling an unexpected case, this can lead to
exploitable behaviours.

you should find the right functionality for simple logic flaws.

try inputs in ranges and data types that legitimate users are unlikely to ever enter.

answer the questions based on application responses:
* Are there any limits that are imposed on the data?
* What happens when you reach those limits?
* Is any transformation or normalization being performed on your input?

1. high-level logic flaw

stuff are added to the cart like this:

```http
POST /cart HTTP/2
...

productId=1&redir=PRODUCT&quantity=1
```

if `quantity=-1`, the price will be less than zero --> `Cart total price cannot be less than zero`

exploit: add the intended item as normal but add another items in negative quantities to
reduce the price enough to be able to buy it.

2. low-level logic flaw

Adding a negative value: `productId=2&redir=PRODUCT&quantity=-2` result in the item being
removed from the cart.

`productId=1&quantity=100&redir=CAR` --> `440, badrequest, "Invalid parameter: quantity"`

this gives the idea that the app might react interestingly if we add a large amount of
items. so we brute force adding 99 items and monitoring the behaviour, finally at some point
the price in `/cart` gets less and less.

3. Inconsistent handling of exceptional input

trying to get to `/adimn` --> `Admin interface only available if logged in as a DontWannaCry
user` but I don't have access to that email.

I try to register with my email, but including payloads of longer and longer character,
hoping that something goes wrong:
`§a§%40exploit-0a9600ae045551c78126abde012c0058.exploit-server.net`.

we find out that only the first 255 characters of the email are considered.

exploit: `<238 As>@don'twannacry.com.exploit-server.net`., the email at some point gets
truncated and the first 255 characters remain, so we are considered to have logged in with
`dontwannacry.com`.

This happens because the server validation is inconsistent when handling and storing and
resolving the mail server domain:

  Truncation effect: The server truncates the email to fit within 255 characters, but it
  interprets the local part (A) and the first domain (dontwannacry.com) as the user
  account's email.

  Domain resolution: When sending emails, the last part of the domain (exploit-server.net)
  is used as the mail server (the first part is the subdomain).

  it either had to truncate or not to.

### making flawed assumptions about user behaviours

if business rules and security measures are not applied through the application.
applications assume if a user passed some validations it can be trusted from now on.

4. Inconsistent security control

like 3, but the email doesn't get truncated, though dontwannacry is considered a subdomain of
exploit-server.

but there is a change email function: `POST /my-account/change-email HTTP/2`, which let us
use any email without validation, so `email=test%40dontwannacry.com`

### user's won't supply mandatory inputs

using proxies allows to submit forms without requited inputs or even remove the parameter
entirely.

if multiple functions are implemented in one script, you will get access to more
functionalities by not passing a parameter. the presence or absence of a particular
parameter may determine which code is executed, or expose code paths to the attacker that
are supposed to be out of reach.

When probing for logic flaws, you should try removing one parameter at a time and observe
what effect this has on the response.

try deleting both the name of the parameter and the value, the responses will be different.
Follow multi-stage processes through to the end. Sometimes tampering with a parameter in one
step will have an effect on another step further along in the workflow.

This applies to both URL and POST parameters, and cookies.

5. weak isolation on dual-use endpoint

we would enter something on old-password field on the front-end, then intercepts and remove
it.

```http
POST /my-account/change-password HTTP/2
...
csrf=jF2u1KugQlYvsSpZij1omXmRleC8DG1t&username=administrator&old-password=1&current-password=1&new-password-1=pass&new-password-2=pass
...
```

### users won't follow the workflow

many transactions rely on predefined sequences of steps, which could be manipulated by
proxies.

submit requests in an *unintended sequence* to complete different actions while the
application is in an *unexpected state*. you could try to do steps more than intended or go
back to earlier ones.

Although you often just submit a GET or POST request to a specific URL, sometimes you can
access steps by submitting different sets of parameters to the same URL

try to identify what assumptions the developers have made and where the attack surface lies.
You can then look for ways of violating these assumptions.

as always pay attention to errors.

be sure to do the steps to completion to figure how things really work.
then drop different step of the process to see the effect.

6. insufficient workflow validation

think what the intended order is, then try to do stuff not in the intended way, what comes
to your mind?

we learn that if we try to buy something, after purchase we have `GET
/cart/order-confirmation?order-confirmed=true`, and we figure we could send this to the
server even without actually purchasing it.

7. Lab: Authentication bypass via flawed state machine

we first monitor that there is a two steps authentication process: `/login` -->
`/role-selection`, which doesn't include `administration` for the user we have access to, so
`/admin` isn't available. but if we drop the request to `/role-selection` we will have
`/admin`.

### Domain-specific flaws

there are flaws specific to the purpose of the site. so many logic flaws in the way discount
are applied. 10% coupon is 100 of 1000, so if you could reduce 1000 to 100 and keep the 100
coupon you will be good to go.

pay attention to values adjusted by user actions, like prices. Understand using which
algorithms and under which circumstances these adjustments are made.

how what you do make how much adjustment in the app.

8. flawed enforcement of rules

nothing special, we can get two coupons, which could be used alternatively many times
without error.

so if you have two coupons, try them alternatively.

9. infinite money logic flaw

we notice that we can have a coupon that could be used multiple times, that we could use to
e can use to buy a gift card, and then redeem it and then we have 3+ dollars.

it's not a technical thing, you should just try different stuff to figure it out.

### encryption oracle

when user input is encrypted and shown back to him. then the plan is to find other functions
that accepts the inputs with the same encryption as valid.

10. authentication bypass via encryption oracle

`stay-logged-in=b3PNAOtnxcqo8lN%2fcIkksYnRuQaYDquIJDXT10kGn2M%3d`

found if send a comment with an invalid Email; the response:
on the page: `Invalid email address: t` --> cookie: `notification=QxK657cGocKJOYFFTp4pCETTjqS2koQEnTuCx6xAFP4%3d;;`
or `Invalid email address: appletree` --> `notification=QxK657cGocKJOYFFTp4pCC%2fXDaM%2bqCuZ9dF1HnLujjnhdbrKt30wYl43Nbj16CtP1;`

we can use the Email to encrypt arbitrary values and decrypt stuff by putting them in the
notification cookie.
`stay-logged-in` --> `wiener:1731941017030`, which is in a `username:tiemstamp` format

# tips

essentially the idea is to try weird inputs to make something go wrong.
something seems weird? try more of it; emails on 10
