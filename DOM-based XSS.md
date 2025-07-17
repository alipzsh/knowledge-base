# DOM-based cross-site scripting

the Dom is altered based on user's input.

JavaScript takes an attacker-controllable value, aka *source* and passes it into a
potentially dangerous function, aka a [sink](sink).

the vulnerability exists in client-side code (the browser) and is executed there. (stored
and executed in the browser)

## Discovery

### step 1: [[find sources and sinks]]
### step 2: is it [[vulnerable sinks]]
### step 3: hover over the variable to see it's value. use payloads based on [XSS context](XSS contexts.md).

EX:

- [[XSS_examples#sink: `document.write`, source: `location.search`]]
- [[XSS_examples#sink `innerhtml`, source `location.search`]]
- [[XSS_examples#jQuery sink: `selector` using a `hashchange` event |jQuery sink: `selector` using a `hashchange` event]]
- [[XSS_examples#jQuery anchor sink `href` attribute]]
- [[XSS_examples#AngularJS expression with angle brackets and double quotes HTML-encoded|AngularJS expression with angle brackets and double quotes HTML-encoded]]

#### [[Reflected DOM XSS]]

a type of DOM that goes to the server and back.

#### [[Stored DOM XSS]]
