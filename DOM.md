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

# DOM Objects

`window.location`: to access the URL.
`location.search`
`document.referrer`
`document.cookie`
