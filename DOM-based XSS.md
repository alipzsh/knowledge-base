# DOM-based cross-site scripting

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
