
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

```js
function escapeHTML(html) {
        return html.replace('<', '&lt;').replace('>', '&gt;');
    }`
```