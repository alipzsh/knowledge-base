it helps to find more info on interesting incidents.

there is a graph that shows the timeline of the found results.

`sampling`: set to 1:100, it will show only 1% of the results.

`sourcetype` shows the top 10 sourcetypes (events).
we can select an event like this: `sourcetype="stream:http"`, which will show use `http` traffic.
splunk parses events into [fields](https://docs.splunk.com/Documentation/StreamApp/7.1.2/DeployStreamApp/FileTransfer#HTTP)

to specify hosts in a query, just write them (it will be slow though).

use `NOT` to exclude a keyword.

`| table _time, form_data`: will only show these tables out of the query.
