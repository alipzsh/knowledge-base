# django
django project structure:

   * X/urls.py -> this file will contain all the API routes for functionality
     X.
   * X/views.py-> this file will contain all the Controllers that the routes of
     functionality X map to.
   * X/views -> templates that dynamically generate HTML of the page.
   * X/static -> static files and other bs. …

these contain the logic for authentication and other stuff.

```py
command = 'ls -la %s' % (self.data['completePath'])
result = ProcessUtilities.outputExecutioner(command, website.externalApp)
```

this code is vulnerable to command injection  via `completePath` via
`ProcessUtilities.outputExecutioner()` sink.


```py
if request.method == 'POST':
                try:

                    # logging.writeToFile(request.body)
                    data = json.loads(request.body)
                    ...
```

it does the command injection checks only if the request method is POST,
however, if you look at our upgrademysqlstatus() route the POST data is loaded
via json.loads(request.body).

docs for the `body` property in Django we can see the following:

    The raw HTTP request body as a bytestring. This is useful for processing data in different ways than conventional HTML forms: binary images, XML payload etc. For processing conventional form data, use HttpRequest.POST.

Can you notice the differential here? The body will be sent irregardless of the HTTP method/verb in question.

Which means, that we can just do an OPTIONS/PUT/PATCH
