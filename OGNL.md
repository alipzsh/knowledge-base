# OGNL

OGNL (Object-Graph Navigation Language) is used for binding data between JSP and action
class.

1. when JSP elements are rendered, it reads data from the value stack. EX: `<s:textfield
name="username"/>` OGNL searched for `username` in value stack.

2. maps requests parameters to [action (obj?)](106/README.md) properties.
EX:

```xml
<s:form action="user">
    <s:textfield name="username" label="Enter Name"/>
    <s:submit value="Submit"/>
</s:form>
```

* When the form is submitted, Struts 2 automatically sets the `username` property in
  `UserAction` (`setUsername()` is called).
* When rendering, `<s:textfield name="username"/>` retrieves the value using
  `getUsername()`.
