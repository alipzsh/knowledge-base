- no http request sent to the target
- depends on the existing sources of data

- google dorks and wayback machine give you hidden URLs.

## Dorking

Search engine --> URL --> vuln
Search engine --> URL --> data --> helps to find vuln

use keywords and operators ; google, bing, etc, to get:

### sensitive info

### interesting paths

you will get some paths, that could have functions behind them,
`../certificate/:username/:data`, take note of those, then exclude them to get to other
results by removing the noise.  `-certificate`

improve your dorks step by step

```
site:
inurl:& // URLs with parameters
ext:php | ext:aspx
```

## wayback machine

Archive.org
`web.archive.org/cdx/search/cdx?url={web_site}`

Read [it](it)'s API document

- old instances of website --> old data on the website that might still
  be there on the backend

  - to get the exact snapshot:
  `web.archive.org/web/<time stamp from previous>if_/http://<website>`

  - to get everything with about the website
  `web.archive.org/cdx/search/cdx?url=.*{web_site}/*`
  then look more into the interesting stuff.

  - to get urls
  `https://web.archive.org/cdx/search/cdx?url=*.capcut.com/*&fl=original&collapse=digest`
  to get `original` column, and to remove identical hashes (based on
  their column).


## katana

Most useful in automation.

- Good for website that the source code is almost similar to the DOM.
- Not suitable for everything, e.g. apps written in [react](react); DOM.
- Change it based on configuration, e.g. reduce the thread if WAF/CDN.

## javascript

A JS code to run in the console and get URls after loading the DOM.

Consider each result; search for it in inspect, then read the related code.
