# DOM

Document object model, is the method browsers use to render a web page;
  * which elements should be where
  * elements have their own properties
  * stuff are manipulated with JS.

```js
var search = document.getElementById('search').value;
var results = document.getElementById('results');
results.innerHTML = 'You searched for: ' + search;
```

- the Elements tab in Chrome DevTools shows the live DOM after the page’s JavaScript has run
  and modified the HTML, while View Page Source shows the original HTML as received from the
  server.


# DOM repetition

a function being called in time intervals
e.g. get the input every 2s

# some DOM Objects

`window.location`: to access the URL.
`location.search`
`document.referrer`
`document.cookie`
