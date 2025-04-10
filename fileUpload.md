when allowing users to upload files into a file system the web app should
validate things like name, type, contents or size.

if it fails to do it, an attacker could upload a payload and trigger it's
execution or if he is lucky just uploading it will be enough.

## what could happen

file upload vulnerability depends on:
  * Which aspect of the file the website fails to validate properly, whether
    that be its size, type, contents, and so on.
  * What restrictions are imposed on the file once it has been successfully
    uploaded.

if different parts aren't validated:

* file type : uploading executable, e.g. `.php`
* file name: overwrite critical files by uploading a file with the same name
  combined with *directory traversal* attacker can upload file to different
  locations.
* file size: the attacker could fill the available disk

## how it happens:

there are always implemented restrictions but, they could be flawed:

* they could miss to validate for *parsing discrepancies*:

  * double extensions: `file.jpg.php`
  * whitespaces and encoding: `file.jpg%00`
  * MIME type mismatch: legitimate type, harmful inside

* they might not detect less common or obscure extensions in a blacklist

* Properties used to verify, could be manipulated by proxies

even though some parts might be robustly validated, this might not be
consistent across the network of hosts and directories of the website.

## how static file requests are handled

server figured out the *file extension* based on the requested path.
it then determines the *file type* based on a preconfigured mapping of extensions to MIME types.

if:

  * non-executable: the server sends the file's contents to the client.
  * executable and the server is configured to execute this type: it will
    assign variables based on the request headers before executing it.
  * executable and NOT configured to execute it: it might leak the information
    or content of the file

`Content-Type` header is informative

### how the server is configured:

in `/etc/apache2/apache2.conf`:

```
LoadModule php_module /usr/lib/apache2/modules/libphp.so
    AddType application/x-httpd-php .php
```

this let's the server execute PHP.

*directory specific* configuration in `.htacess` file, if present.

on IIS servers using a `web.config` file. this one allows JSON files to be
served to users:

```
<staticContent>
    <mimeMap fileExtension=".json" mimeType="application/json" />
    </staticContent>
```

## how to execute files on the server

when a website allows you to upload server-side scripts, such as PHP, Java, or Python files, and is also configured to execute them as code

Web shell: A web shell is a malicious script that enables an attacker to execute
arbitrary commands on a remote web server simply by sending HTTP requests to
the right endpoint.

```php
<?php echo file_get_contents('/path/to/target/file'); ?>
```

in this case, you will request this file.

## website's flawed preventions

a [validation in Apache struts](44/struts_validation.java) that checks mime type, magic
bytes and prevents JSP file uploads

to pybass it, we should add `ÿØÿà` on top of whatever text our payload is (which is replaced
the actual image contents in the request, using burp).

### flawed file type validation

`POST` method's `Content-Type`:

* `application/x-www-form-url-encoded`: for sending simple text like username.
* `multipart/form-data`: for large files, an image or a pdf document.

the request after submitting an upload form:

```http
POST /images HTTP/1.1
    Host: normal-website.com
    Content-Length: 12345
    Content-Type: multipart/form-data; boundary=---------------------------012345678901234567890123456

    ---------------------------012345678901234567890123456
    Content-Disposition: form-data; name="image"; filename="example.jpg"
    Content-Type: image/jpeg

    [...binary content of example.jpg...]

    ---------------------------012345678901234567890123456
    Content-Disposition: form-data; name="description"

    This is an interesting description of my image.

    ---------------------------012345678901234567890123456
    Content-Disposition: form-data; name="username"

    wiener
    ---------------------------012345678901234567890123456--
```

one part for each form's input, containing `Content-Disposition` header.

when uploading something that isn't the same as MIME type, chaining it's
`Content-Type` might fool the server, (what the server expects).

### flawed file execution Prevention  in user-accessible directories

the second line of defense is to stop the server from executing any scripts
that do slip through the net.

other directories might not have that much strict controls.

so the file isn't executed and it's contents are returned:
`<?php echo file_get_contents('/home/carlos/secret'); ?>`

we try *path traversal* and it works, but has to be URL encoded:
`../image.php` --> `%2e%2e%2fimage.php`

### flawed *blacklisting*: bypass by overriding server configuration

it's difficult to block every possible file extension that could be used to
execute code.

lesser known, alternative file extensions that may still be executable: `.php5`, `.shtml`.

you're not normally allowed to access server's config files using HTTP
requests.

but if you could somehow upload a config file, you might trick the server into mapping a custom file extension to an executable MIME type, even though it is blacklisted.

```
AddType application/x-httpd-php .hph
```

tried `application/x-php` but it didn't work. so it seems you should try different ones.

also portswigger solution changed `Content-Type` to `text/plain`

### flawed *blacklisting*: bypass by obfuscating file extensions

if the validation isn't triggered by `.pHp` but the MIME type mapping consider
it as `.php`.

works well even on good blacklists.

obfuscation techniques:

* multiple extensions: `exploit.php.jpg` could be interpreted as either
  extensions.
* trailing characters: `exploit.php.`; dots, trailing whitspaces might be
  ignored (ha?)
* URL encoding (or double URL encoding): `exploit%2Ephp` for dots, forward
  slashes, and backward slashes.

  helpful when the values aren't decode while validating but are later.

* semicolons or null byte characters (encoded): `exploit.asp;.jpg` or `exploit.asp%00.jpg`

  these work if the underlying server process uses C/C++, so these are treated as end of the string.

* multibyte unicode characters: which may be converted to null bytes and dots
  after unicode conversion or normalization. Sequences like xC0 x2E, xC4 xAE or
  xC0 xAE may be translated to x2E if the filename parsed as a UTF-8 string,
  but then converted to ASCII characters before being used in a path. 

* if stripping or replacing isn't done recursively: `exploit.p.phphp`

for this lab I just used `image.php%00.png` and then GET `image.php`.


### flawed validation of the file's contents

more secure server's check file's contents rather than just `Content-Type`.

they check the features exits in their desired file, like image dimensions.

files header or footer are checked for sequence of bytes that are like a fingerprint of file types. JPEG: `FF D8 FF`

there is something like this in natas13 that didn't work here.

you should make polyglot `PHP/JPG file` using:

```sh
exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" <YOUR-INPUT-IMAGE>.jpg -o polyglot.php
```

adds the payload to image's comment section.

### Exploiting file upload race conditions

new frameworks don't upload files directly to the file system.

they upload it to a temporary sandboxed directory first and randomize the name to avoid overwriting existing file.

then perform validation on this temporary file.

sometimes the developers implement another processing of file uploads independently of the framework. this is complex and could lead to race condition.

even if a file is on the server for milliseconds before it is removed, it can be executed.


## Exploiting file upload vulnerabilities without remote code execution

read on portswigger
