# http

## http status codes

400-499: client error; server is working correctly
    401: unauthorized
    404: not found; maybe wrong url
500-599: server error



http *identity encoding* (default encoding) applies no encodings at all.

in *chunk encoding* each one is prefixed with it's size and end by *zero-byte chunk*.
used when the size of the entire body is not known in advance (dynamically generated).

so if the message contains a content-length leader and the content is encoded, the content
length should be ignored, because the encoding will change the way entity bodies are
represented.

`multipart/byteranges` media type, self-delimits it's own size.

MD5 of the content is calculated after *content encodings* and before *transfer encodings*
(gzip and chunked).

# http encoding

content and transfer encoding both reversible and applied on the entity body.

## content encoding

an encoding might happen because: security or slow connection.

the process of encoding happens in a content encoding-server.

after encoding the content length header shows the length of the encoded body.

expressing the preference using quality: `Accept-Encoding: gzip;q=0.5`


## transfer encoding

for architectural reasons to change the way data is transfer across the network.
to provide safe message transport across the network.

Chunked encoding breaks messages into chunks of known size. Each chunk is sent
one after another, eliminating the need for the size of the full message to be known
before it is sent. is an attribute of the message not the body (multipart-encoding).

in non-persistent connection clients don't need to know the length of the body and the
server can just close it. but in persistent, the length of the body must be known (in
content-length header).

Chunked encodings are used in case of dynamically generated content in persistent
connections, by allowing the servers to send the body in chunks specifying the size of each
chunk (rather than the whole content) which ends with a chunk of length zero.

# headers

`X-Forwarded-For` HTTP header field is a method for identifying the originating
IP address.

`content-length`

`Content-MD5` to send the result of MD5 algorithm on the entity body.

`Content-Type: text/html; charset=iso-8859-4` specifying the mechanism to convert bits from the entity into characters in a text file:

`Content-Encoding` describes the algorithm used in the token.

`Accept-Encoding` request header. If includes `identity`, the client doesn't want any
encoding.

`Transfer-Encodign` tells the client of the performed encoding

`TE` in request to tell the server about the proffered encoding.

`Trailor` lists the headers that will be sent after the end of chunked messages, like MD5.

`location` redirect URL
