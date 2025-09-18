Archive.org

gives you old instances of a website
--> old data on the website that might still be there on the back-end

e.g: there might have been a link to a route that got removed in the newer
instances.

# usage

Read it's API document

- get snapshots of a website:
`https://web.archive.org/cdx/search/cdx?url={web_site}`

- get exact snapshot using timestamps:
`https://web.archive.org/web/<time stamp from previous>if_/http://<website>`

- to get everything on the website:
`https://web.archive.org/cdx/search/cdx?url=.*{web_site}/*`
then look more into the interesting stuff.

- get the `original` column, and to remove identical hashes (based on their column) and return only the unique snapshots
  e.g. we don't want all the robots.txt but only the unique ones.
  (the reason to read the API documents)

  `https://web.archive.org/cdx/search/cdx?url=*.capcut.com/*&fl=timestamp,original&collapse=digest`
  `https://web.archive.org/cdx/search/cdx?url=*.finnair.com/*&fl=timestamp,original&collapse=urlkey`

then you should compare the unique resources to see what have changed e.g. with
robots.txt.

get the timestamp and use to get the exact snapshot.

# wayback and gau tools

```
echo "https://alibaba.com/" | waybackurls > wayback
gau {hostname} --threads 1 --subs --o gau
cat gau wayback | sort -u | uro > sorted_uro
```
