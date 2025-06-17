# methodology

* maybe one of the best ways to think/implement methodologies is by coding it. somehow it
  seems alot more obvious.

* look at the target and think what type of bug makes sense given the application's
  functionality.

* learn what you could do in the app in-depth.


we used a combination of public records and network scripts to dis‐
cover undocumented API endpoints.

## first looks

Glance over everything, learn new techs, understand what is happening, but don't get too
deep.

use burp and look more.

## find a target

not too popular
not too advanced/ big

# [[bug_bounty_recon]]

## take notes of

technology used:

* List of [[API endpoints by HTTP verb]]
* List of [[API endpoints shape]]
* Functionality included in the web application (e.g., comments, auth,
notifications, etc.)
* Domains used by the web application
* Configurations found (e.g., Content Security Policy [CSP])
* Authentication/session management systems

the architecture of an application and the architecture of the modules/dependencies
within that application are fantastic markers of weak points from which vulnerabili‐
ties may arise.

## which functionalities to look for

When testing web applications, you want to look for functionality in an
application that makes use of a few security mechanisms or requires a
significant number of layers (hence likely to have a lower ratio of secu‐ rity
mechanisms to layers). If you can isolate and determine what functionality meets
this criteria, it should be prioritized over the rest when looking for
vulnerabilities; it is more likely to be exploitable.

## automate chained requests

export multiple requests in burp as xml.
use python to parse them.
use python to manipulate and send requests.


---

methodology tells you where to test, what to test.

# ideas

- look for bugs where things aren't how they should be, e.g. "something has a different usage somewhere".