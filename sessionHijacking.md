# sessionHijacking
Session support consists of a way to preserve certain data across subsequent accesses.

session id: users are assigned a unique id when vesting the website.

it is stored in a cookie on the user side or in the URL.

in PHP the data between sessions are is stored in `$_SESSION` array.


# hunt

check how session ids are created and if they are predictable, if so, you can bruteforce it.
