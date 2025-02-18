# Apache struts

struts uses `FielUploadInterceptor` (configured in `struts-default.xml`) to automatically
map stuff to `upload`, `uploadFileName`, `uploadContentType` variables.

`private File upload;` declares a variable of type File, it's value is null.

a *setter method* that allows struts to inject the uploaded file into `upload` variable.

```java
public void setUpload (File upload) {
       this.upload = upload;
   }
```

```html
<form action="doUpload" method="post" enctype="multipart/form-data">
    <input type="file" name="upload" />
    <input type="submit" value="Upload" />
</form>
```

when an upload form is sent, struts will look for and use this setter method. to set the
variable to the instance variable (`upload` in this case).

[struts value stack](104/README.md)
[OGNL](107/README.md)
