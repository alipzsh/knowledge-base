# splunk

all devices on your network register logs. the idea is to forward all those into a central
repository.

search head: sql queries to search through server
indexer: server with storage, stores and searches through the data
forwarder: software module. forwards data to the server.

search and reporting: to search log data.

metadata, that indexer assignes to data:
    source: path of input file, network `hostname:port`, script name
    host
    sourcetype
    index

```
sudo /opt/splunk/bin/splunk enable boot-start
sudo /opt/splunk/bin/splunk start
```

you could use splunk to find traffic that went back to the network. that's how reverse
shells happen.

`sourcetype="stream:http" c_ip="192.168.230.1"`

this specify the client IP in the request and the value equals our own server.
so the requests that were made from our server.

* if after adding data, the source type is set to default, you can change it.
* to add a new source type, click save as. [add screenshot].
