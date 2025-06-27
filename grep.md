# grep

`grep -r <pattern> path`

* `-i`: ignore case distinctions in the pattern.
* `-a 5`: searches for the line and prints it along with the next 5
  lines (including that line).
* `-E`: ERE
* `-o`: only the matching part, not the whole line
* `head -n 1`: prints only the first line of the output, which
corresponds to the first version number found in the changelog.
* `-v`: !
* `-P`: regex stuff
* extract text in quotes:
  `grep -oP "'.*?'" <file>`
* `-F`: no regex
* `-l` list of the files containing matches
* `-h` no file name
* `-n` line number
* `-q` silent, only exit code




EX:

```
<b>Query:</b> <pre>SELECT 'B' FROM secrets</pre><br>
<b>Results:</b><pre>IxgTUlsGeM+Zfsu7VYyq1A==</pre>
```

* **`(?<=<pre>)`** → A **lookbehind**, ensuring the match happens **after**
	`<pre>` but not including it.

* **`[^<]+`** → Matches **one or more (`+`) characters that are NOT `<`** (stops
	at the next HTML tag
