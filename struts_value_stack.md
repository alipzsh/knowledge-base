# struts value stack

stores application data. allows access to the data across requests. Objects are stored and
access by struts components and are accessible using JSP ( embedding java codes into html,
to create dynamically web pages).

[action object](106/README.md) is on top of the stack then other scopes like requests, session and application.

use `top` to access the top element of the value stack (`action` obj), then `toString()` to
inspect the contents.
