all devices on a network register logs. the idea is to forward all those into a central repository.

search head: SQL queries to search through server
indexer: server with storage, stores and searches through the data
forwarder: software module. forwards data to the server.

search and reporting: to search log data.

metadata, that indexer assigns to data:
    source: path of input file, network `hostname:port`, script name
    host
    sourcetype
    index

```
sudo /opt/splunk/bin/splunk enable boot-start
sudo /opt/splunk/bin/splunk start
```

* if after adding data, the source type is set to default, you can change it.
* to add a new source type, click save as.

![[Screenshot from 2025-02-18 12-14-33.png]]

looking for rare values of fields makes more sense because more popular stuff are probably automated system programs.

lookup: are ways to add additional data that isn't in the original data.
EX: your data might just have product IDs, not product name or description.

[[Splunk Search & Reporting]]
[[botsv1]]
[[Example queries]]

[definition of differrent splunk fileds](https://docs.splunk.com/Documentation/StreamApp/7.1.2/DeployStreamApp/FileTransfer#HTTP)
