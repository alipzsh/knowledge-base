# methodology

Methodology is where to test, what to test.

- the types of vulnerabilities you should focus on will vary on different application.
- to abstract irrelevant details, understand/ manipulate every part of the code (fiddle around with
  it) so that you can find the most important ones.
- learn enough of new things to be able to have a basic setup of them --> then fiddle and explore.
- you should choose where you want to work on an app based on whether you think it's going
  to worth your time or not. e.g. somewhere with lots of user posts is very messy or obvious
  stuff.

- The hunting process: [[bug_bounty]]

# add to narrow recon

* Functionality included in the web application (e.g., comments, auth, notifications, etc.)
* Authentication/session management systems

## which functionalities to look for

When testing web applications, you want to look for functionality in an application that
makes use of a few security mechanisms or requires a significant number of layers (hence
likely to have a lower ratio of security mechanisms to layers). If you can isolate and
determine what functionality meets this criteria, it should be prioritized over the rest
when looking for vulnerabilities; it is more likely to be exploitable.
