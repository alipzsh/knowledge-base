# ssh

* public key --> encrypt data, shared e.g. `~/.ssh/id_rsa.pub`
* private key --> decrypt it, private e.g. `~/.ssh/id_rsa`

* client/control: key pairs
* server: public keys in `~/.ssh/authorized_keys`

## How to SSH into another computer?

 in `sudo vi /etc/ssh/sshd_config`:
  
  * uncomment and change `port 22` to something else.
  * uncomment and change `PasswordAuthentication` to `no`.
  * uncomment and change `PermitRootLogin` to `no`.
  * reload everything: `sudo systemctl reload ssh`.

  then:
  
  * use `ssh -p port_number user@host_ip`. if your user name matches the host `ssh host_ip`.

## files in .ssh:

 control:
- pub/private keys
- known_hosts
- .config
 nodes: authorized_keys

## SSH public key authentication process:

1. Client connects to the server.
2. Client offers its public key (or keys) to the server.
3. Server checks if that public key is listed in ~/.ssh/authorized_keys of the user’s account.
4. If found, server sends a challenge encrypted with the public key.
5. Client uses its private key to decrypt and respond correctly.
6. If successful, server grants access.

## generate ssh keys

* you can create multiple keys for personal and work:
  ssh-keygen -t rsa -C "name@personal_email.com"
  ssh-keygen -t rsa -C "name@work_email.com"

* .ssh/config: it's important so that ssh knows which private key to use.
  
  ```
  Host pen           # whatever; used like ssh pen
    HostName penvm  # the name associated with the IP in /etc/hosts
    User hunter
    IdentityFile ~/.ssh/id_ed25519_penvm
    Port 26318
  ```
  
`sh-copy-id remote_host`

`ssh-keygen -R <vm-ip-or-hostname>`


[ssh to access the service running on the target](76/README.md##ssh_tunnel)

* ssh over proxy:

`ssh USER@FINAL_DEST -o "ProxyCommand=nc -X connect -x PROXYHOST:PROXYPORT %h %p"`
works on v2ray

`https://stackoverflow.com/questions/19161960/connect-with-ssh-through-a-proxy`
`https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts`


### Example Scenarios:

1. **One Client, One Server**
    
    - Client A has its own private key (`~/.ssh/id_rsa`).
        
    - The public key (`id_rsa.pub`) is added to the server’s `~/.ssh/authorized_keys`.
        
    - Only Client A can log in.
        
2. **Multiple Clients, One Server**
    
    - Client A and Client B each have **separate private keys**.
        
    - Both of their **public keys** are added to the server’s `authorized_keys`.
        
    - Either can log in using their respective private keys.
3. **One Private Key, Multiple Servers**
    
    - A single private key on the client can authenticate with multiple servers if its **public key** is copied to each server.