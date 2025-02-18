# js
`document.body.children` returns every elements in `body` element.
`childNodes` returns texts too.

# selectors

selectors are patterns used to select the element(s) you want to style.

get an element by it's tag: `document.querySelector('script').innerHTML`

get the element using the method `document.getElementById(id)`
also get it by it's *name* attribute: `document.getElementByName("<name>")`

`let elements = document.querySelectorAll('ul > li:last-child')` returns all
elements inside elem matching the given CSS selector. in this case: all `li`
that are the last child of `ul`.

`elem.querySelector(css)` returns the first element for the given CSS selector.

# modifying  the DOM

The syntax for adding an onload event should not immediately invoke the function. For example, `img.onload = function() { alert('Image loaded!'); };`

another way of setting attributes: `img.setAttribute('src', 'URL');` or `onload` or whatever.

load jQuery then select and change title:
`
let script = document.createElement("script");
script.src = "https://code.jquery.com/jquery-3.6.0.min.js";

script.onload = function() {
    $("title").text("New Title with jQuery!");
};

document.head.appendChild(script);
`

fetch data from an api and show it somewhere in the document
``
fetch('https://dummy.restapiexample.com/api/v1/employee/1')
    .then(response => response.json()) // Step 2: Parse the JSON response
    .then(data => {
        // Step 3: Select a DOM element to show it
        let contentDiv = document.querySelector('h1');

        // Step 4: Update the DOM with data
        contentDiv.innerHTML = `<p>${data.data.id}</p>`;
    })
``

# authentication

look for login.js in sources part of inspect element.

# obfuscation

JavaScript obfuscation is the process of transforming JavaScript code into
a version that is difficult for humans to understand

# All attributes are accessible by using the following methods:

`elem.hasAttribute(name)`, whether standard or not.
`document.body.getAttribute('something')`

# html attributes, DOM properties

html attributes will be parsed into DOM properties:
* The id property is a reflected property for the id attribute:
* the value property doesn't reflect the value attribute. Instead, it's the
  current value of the input.
  `
  <input id="the-input" type="text" value="Name:">
  input.value // returns "John"
  input.getAttribute('value') // returns "Name:"
  `
the href DOM property is always a full URL, even if the attribute contains a relative URL or just a #hash
