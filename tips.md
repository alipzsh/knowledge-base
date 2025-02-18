# tips
# how to learn the target:

read previous write-ups/exploits/docs of previous write-ups about the target.
then check the *patches* they committed.

FYI: Many endpoints just allow you interact with them un-auth by just passing
use rid=1 to the controller. Hope this gives people a hint if they want to find
more bugs :)

# search for whatever unimportant thing you see.

`cif` files, then check for `cif files CVE`; doesn't made sense to me but it should

# don't get deep stupidly

don't try to understand everything about a cif files right away. 

* if something should work but it doesn't, like a payload, investigate how it is supposed to
  work.
