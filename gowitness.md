
if any issues, see the [end](#issues)

`gowitness scan file -f <file> --timeout 10 --write-stdout -t 1`

then `gowitness report server`
then `google-chrome --proxy-server="socks5://localhost:8089"` and use `0.0.0.0:7171`.
you could use a different port that your ssh tunnel.

I can't get them from my headless server. but can from the local:
`gowitness scan file -f httpx --timeout 10 --write-stdout --chrome-proxy=socks://localhost:8089`

`cat report | grep -Eo 'target=http[s]?://[^ ]* status-code=200'` to get 200.
# issues

## gowitness

to try to fix errors, make it simple:
  * `gowitness scan single --url "http://google.com" --screenshot-fullpage --write-stdout`
  * check if you could do this on the network without issue.
  * it seems `screen-shot=false` is due to network issues.
  * remember to use `-t 1` on the server (or 2?).
  * Screenshoting isn't that reliable or I don't get it, so I'll better move on and try
    things manually in layers.