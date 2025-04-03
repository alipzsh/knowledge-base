# ssh

* public key is used to encrypt data.
* private key is to decrypt it.
* the public key can be shared but the private key shouldn't.

- **Private key (`~/.ssh/id_rsa`)** – Stays on the client machine.
- **Public key (`~/.ssh/id_rsa.pub`)** – Added to the remote server.

* client: key pairs
* server: public keys on ~/.ssh/authorized_keys
* ssh authentication process:
  * client connects to the host, tells the server which public key to
    use.
  * server then checks its authorized_keys file for the public key.
* known_hosts: on the client, list of all SSH server host public keys
  that you have determined are accurate.
  * If there is a change in the public key of the remote server, your
    system will note this change.
* not having passphrase for ssh key pairs will allow anyone who gains
  control of your private key to log in to your servers.
  * does it matter if that's a pentest vm and I don't care about it?
  * does it somehow makes the client host vulnerable?
* create ssh key pairs useing: ssh-keygen (use `-b 4096`) for a stronger
  one.
  * name them different things to use for different purposes.
* you can create multiple keys for personal and work:
  ssh-keygen -t rsa -C "name@personal_email.com"
  ssh-keygen -t rsa -C "name@work_email.com"
* .ssh/config ftw:
  it's important so that ssh knows which private key to use.
  `
  Host pen          # whatever
    HostName penvm  # the name associated with the IP in /etc/hosts
    User hunter
    IdentityFile ~/.ssh/id_ed25519_penvm
    Port 26318
  `
  * then: `ssh penvm`

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