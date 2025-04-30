- basic chance reflected XSS:

angle brackets are encoded:

bruteforce for allowed stuff.
it's inside a `<div>` tag.

```http
&troopName=<script>123;<script>&otherName=
```

everything after `;` won't get HTML encoded:

```html
<div class="built-by-text">
	&nbsp;&lt;script&gt;123
</div>
```

- something like this that chooses stuff and counts the steps

```http
answerStepId=4&questionId=5&currentStep=4
```

can't directly inject anything but maybe get's stored somewhere? or an sql query to the server?

- &currentStep=9';-- => 500

### 🧠 What it means:

- **`currentStep` is not sanitized** properly.
    
- Your input `'--` **likely reached a SQL query** on the server.
    
- The server **did not expect** this — and crashed instead of handling it cleanly.
    
- **Very likely SQL injection.**

- &currentStep=-2 => HTTP/2 302 Found
Date: Tue, 29 Apr 2025 01:25:59 GMT
Content-Type: text/html; charset=utf-8
Location: http://cookieplanner.littlebrowniebakers.com/planner/result/50723/?council=%3C/div%3E%3Cscript%3E123%3C/script%3E
Server: nginx
Vary: Cookie
Set-Cookie: sessionid=nbpyvqb3kla1fzyjoo49zsy7f51w013w; expires=Tue, 13-May-2025 01:25:59 GMT; httponly; Max-Age=1209600; Path=/
X-Ua-Compatible: IE=Edge
Cache-Control: no-transform

- also in the last step: GET /planner/result/50725/?council=%3C/div%3E%3Cscript%3E123%3C/script%3E HTTP/2
but will get 403, but works if it's something like "d"

but most of the times changing it won't change it in the code: it will still be like the code above: ...123...

`GET /planner/result/50725/?council=<script>` => 403

- interesting javascript context: in the final page it will also be here:

```html
		<script>
		  dataLayer = [{
		    'pageCategory': 'results',
		    'councilName': '&lt;/div&gt;&lt;script&gt;123&lt;/script&gt;',
		  }];
		</script>
```

- while I was trying to automate the stuff, the page is removed and I get
redirected to /. there might have been stuff that could cause bugs.

from now on, I should automate it before doing anything.

- `https://www.nutella.com/fr/sites/nutella20_fr/files/../../etc/passwd` => <snip>...file/etc/passwd

you're hitting a **cloud storage-backed asset system**, likely an **AWS S3 bucket or similar** behind a CDN.

You **cannot break out** of this structure — the system doesn’t interpret `../`
or `/etc/passwd` as a file path on the server. It simply maps to nonexistent
object keys. so no directory traversal

- used dalfox on `https://blog.littlebrowniebakers.com/?route=%2F` and we have been ratelimited.