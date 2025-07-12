Archive.org
`web.archive.org/cdx/search/cdx?url={web_site}`

Read it's API document

old instances of a website --> old data on the website that might still be there on the
back-end

- to get the exact snapshot:
`web.archive.org/web/<time stamp from previous>if_/http://<website>`

- to get everything about the website:
`web.archive.org/cdx/search/cdx?url=.*{web_site}/*`
then look more into the interesting stuff.

- to get URLs:
`https://web.archive.org/cdx/search/cdx?url=*.capcut.com/*&fl=original&collapse=digest`
to get `original` column, and to remove identical hashes (based on
their column).

use waybackurls and  gau:

```
echo "https://alibaba.com/" | waybackurls > wayback
gau {hostname} --threads 1 --subs --o gau
cat gau wayback | sort -u | uro > sorted_uro
```


