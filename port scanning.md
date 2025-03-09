active scanning: directly sending requests to the target machine, using
nmap.

slow scan on top 100 ports: `nmap -A -v -F -T1 <target>`

passive scanning: using third-party resources to stay hidden; shodan,
census, project sonar.