# netcat

listens at some port, can then serve stuff maybe piped from echo.
* `-lvpn`: listen, verbose, to this port and skip dns resolution.
* `-s`: `nc -lnvp 9000 -s 127.0.0.1`
* `<ip> <port>`
* `-z`: to check if the port is available.
* send an http request: `echo -e 'GET / HTTP/1.1\r\nHost 8c743f9e89f895bee8ebb8818067b21b\r\n\r\n' | nc localhost 80`
