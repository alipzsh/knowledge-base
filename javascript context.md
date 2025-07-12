1. close the `<script>` --> [[XSS out of tags]]
2. break the context, fix the rest: e.g. `'-alert()-'` in `..&userid=name"-alert()-""..`

EX:
- [[XSS_examples#Reflected XSS into a JavaScript string with angle brackets HTML encoded| angle brackets encoded]]
- [[XSS_examples#Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped| single quotes escaped]]
- [[XSS_examples#Reflected XSS in a javascript URL with some characters blocked| some characters blocked]]
- [[XSS_examples#Reflected XSS into a JavaScript template literals, with `<>'" ` unicode escaped| '"<> and backtick escaped, js template literals]]
