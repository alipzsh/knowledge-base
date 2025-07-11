# magic parameters

Most useful in finding XSS and DOM XSS.

## the *exact* parameter could be found on the application.

- where to look?
  - http requests (in URLs)
  - html form names and ids, etc
  - javascript varialbe names (in a page code).
  - json object's keys. var variable = {key: value}; both variable and
    key are parameters.

- get params from either passive recon, x8, GAP, then test them manually in burp repeater.

query string parameters can be increased as long as the server handles the request => you
can test more than one parameters in an HTTP request.

### tools

- GAP
- fallparams
- `x8 -w wordlist.txt  -u https://stuff.org`
- arken
- passive recon; then extract parameters and use them on any page.
- unfurl: extract stuff from the URL: `echo {URL} | unfurl keys`
  `cat .passive | unfurl keys | sort -u | grep -v "/"`
- parammaker; to make a long string of parameters from a list.

```bash
param_maker () {
    filename="$1"
    value="$2"
    counter=0
    query_string="?"
    while IFS= read -r keyword
    do
        if [ -n "$keyword" ]
        then
            counter=$((counter+1))
            query_string="${query_string}${keyword}=${value}${counter}&"
        fi
        if [ $counter -eq 25 ]
        then
            echo "${query_string%?}"
            query_string="?"
            counter=0
        fi
    done < "$filename"
    if [ $counter -gt 0 ]
    then
        echo "${query_string%?}"
    fi
}
```

## *similar* ones could be found on the application:

By seeing this  `yahoo_home_ui` you might guess `yahoo_home_redirect`

## completely *new* name

### tools

- top 25 parameters for XSS wordlist.
