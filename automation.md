# XSS

- opportunities of data entry:
	- POST body
	- request headers
	- url query strings

## stored

- look for exit points:
	- all possible http responses (any kind of user, with any privilege)
	- audit logs
	 
- find the links between entry and exit points.