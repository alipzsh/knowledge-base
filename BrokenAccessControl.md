# BrokenAccessControl

# Access control vulnerabilities and privilege escalation

access control is dependent on authentication and session management:
    * authentication: the user is who they say they are
    * session management: which http request are by the same user
    * access control: if the user can do the action.

vertical access control:

restrict access to sensitive functionality to specific types of users. 

different types of users have access to different application functions, e.g.
admin vs regular user.

Horizontal:

restrict access to resources to specific users. users can use functionalities
but on the resources that they access.

Context-dependent access controls:

Restricts what users can do based on the state of the application. if they are doing something, they can't do something else.


## vertical [privilege escalation](36/README.md)

if you can access to functionality that you are not allowed e.g. getting root
access.

### unprotected functionality:

e.g.: if you can access an admin page/functionality by reaching a URL:
`https://insecure-website.com/admin`

this URL might not be easily discoverable, but it could be somewhere in the page source.

### Parameter-based access control methods

access rights are stored in a user-controllable location:
    * a cookie
    * a hidden filed
    * a query string parameter

e.g.

`https://insecure-website.com/login/home.jsp?admin=true
https://insecure-website.com/login/home.jsp?role=1`

you can modify a changing email request to change other stuff in the database.

### Broken access control resulting from platform misconfiguration

1.

apps give access based on user's role:

`DENY: POST, /admin/deleteUser, managers`

denies access to the `POST` method on `/admin/deleteUser` for users in managers group.


solution:

if the `access denied` response is very plain, it may originate from a front-end system.

you might be able to add a header so that the URL would be overwritten:
`X-Original-URL: /admin/deleteUser`

2. you have access to a function in account A, but not from the account B:

replace the session in the As, request with B.

didn't work? this means account B isn't authorized for that function, but that might work for another HTTP method.

### Broken access control resulting from URL-matching discrepancies

e.g. `/admin/deleteUser` and `/admin/deleteUser/` are treated as distinct
endpoints, so you might be able to bypass access control by appending a `/`.


## Horizontal privilege escalation

gaining access to resources belonging to another user, instead of their own
resources of that type. e.g. An employee can access other employees info too.


1. you could do this by changing URL parameters: `GET /my-account?id=carlos HTTP/2`.

2. what if the parameter values aren't predictable? e.g. they use globally
   unique identifiers (GUIDs) to identify users?

   those might be visible in some other part of the website, e.g. a message. 

3. sometimes when unauthorized, the returned data contains useful info.

## Horizontal to vertical privilege escalation

if a Horizontal escalation compromises a more privileged user. e.g. if an
attacker gain access to the administrator, they can get administrative access
and though vertical privileges.

## Insecure direct object references

a subcategory of access control vulnerabilities. IDORs occur if an application
uses user-supplied input to access objects directly and an attacker can modify
the input to obtain unauthorized access.

mostly horizontal privilege escalation.

e.g. when sensitive resources are located in static files on the server-side filesystem.
`https://insecure-website.com/static/12144.txt`

## Access control vulnerabilities in multi-step processes

websites implement important functions over a series of steps.
   
   * A variety of inputs or options need to be captured.
   * The user needs to review and confirm details before the action is performed.

how to:

multi step processes with a flawed step leads to an exploit.

the website assumes the user will reach at that step after the previous ones
which are properly controlled, but if the attacker can skip those.

## Referrer-based access control

access determined based on referrer header.

e.g. accessing the sub-pages such as `/admin/deleteUser` is allowed only if it came from the `/admin` page.

this could be bypassed by forging requests with the required Referrer header.

