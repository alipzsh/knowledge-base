
read on [[obfuscating attacks]]

* if you enter `'` in a search field and get it back in the result, it has been
escaped and isn't considered as a special character.

use none obvious inputs.

you can do injection attacks using any user controllable input that is
processed as SQL query.

some websites take input in XML or JSON to query the database.

solution:

these formats may have some ways to bypass the protection against sql attacks.
you could do html hex encode to send a request. (using an XML escape sequence?
what is this?)

obfuscation attacks are useful to bypass WAFs and other defenses.

White space & comment obfuscation: Using `/**/`, `--+`, tabs, etc., to bypass filters.

* the filter looks for keywords: try encoding or escaping characters

`SELECT` => `&#x53;ELECT`