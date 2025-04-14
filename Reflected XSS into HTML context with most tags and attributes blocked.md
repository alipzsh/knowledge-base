
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
