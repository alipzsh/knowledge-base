# strutted

## Dockerfile:

* `openjdk:17-jdk-alpine`, meaning it's an openjdk image based on alpine.
* `FROM` to use a base image
* [Apache maven](98/README.md)

  ```xml
  < dependency > < groupId > org.apache.struts </ groupId > < artifactId > struts2-core </ artifactId > < version > 6.3.0 </ version > </ dependency >
  ```

  * `Apacheh struts` is used as an mvc framework
* Apache tomcat
  a webserver
  port 8080

CMD ["catalina.sh", "run"]

configuring Apache tomcat and maven.

## tomcat-users.xml

```xml
<?xml version='1.0' encoding='utf-8'?>

<tomcat-users>
    <role rolename="manager-gui"/>
    <role rolename="admin-gui"/>
    <user username="admin" password="skqKY6360z!Y" roles="manager-gui,admin-gui"/>
</tomcat-users>
```

it's an image that runs a server.

## JSP (Jakarta Server Pages; formerly JavaServer Pages)

is a collection of technologies that helps software developers create dynamically generated
web pages based on HTML, XML, SOAP, or other document types.

## codes

[Apache struts](103/README.md):
  * [UploadsAction](96/UploadsAction.java)
  * [UploadAction](96/UploadAction.java)


`CVE-2024-53677`

[in the similar vulnerability in struts](`https://y4tacker.github.io/2023/12/09/year/2023/12/Apache-Struts2-%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E5%88%86%E6%9E%90-S2-066/)

An attacker can manipulate file upload parameters to enable *paths traversal* and under some
circumstances this can lead to uploading a malicious file which can be used to perform
Remote Code Execution

the POST request triggers file upload with multiple form-data contents. `filename` parameter
is a key point of injection.

the idea is to use the *OGNL parameter abuse* to change the name of the file to a JSP file
which will let us trigger our payloads.

## how to access the value stack

# learned

* research path: you are examining an app, research what are the important files in that
  language, or type of application. in the next step, go for searching stuff in a file. and
  check for example every version you can find.

  * tomcat:

    => java => important java files
    => webserver => important server files

    * make the search narrower, in this case, maven project structure.
    * to learn more you could even write something in these.
    * many POCs have instructions to repeat the process.
