# chemistry

# CVE-2024-23346

`onesFaithfulTransformation.from_transformation_str()` method within the `pymatgen` library
insecurely utilizes `eval()` to process the input. an attacker injecting code into
`transformation_string` could lead to remote code execution.

used
[this](https://github.com/materialsproject/pymatgen/security/advisories/GHSA-vgv8-5cpj-qj2f)
exploit to get a reverse shell.

a database, and a md5 hash to get the password

```
1|admin|2861debaf8d99436a10ed6f75a252abf
2|app|197865e46b878d9e74a0346b6d59886a
3|rosa|63ed86ee9f624c7b14f1d4f43dc251a5
4|robert|02fcf7cfc10adc37959fb21f06c6b467
5|jobert|3dec299e06f7ed187bac06bd3b670ab2
6|carlos|9ad48828b0955513f7cf0f7f6510c8f8
7|peter|6845c17d298d95aa942127bdad2ceb9b
8|victoria|c3601ad2286a4293868ec2a4bc606ba3
9|tania|a4aa55e816205dc0389591c9f82f43bb
10|eusebio|6cad48078d0241cca9a7b322ecd073b3
11|gelacia|4af70c80b68267012ecdac9a7e916d18
12|fabian|4e5d71f53fdd2eabdbabb233113b5dc0
13|axel|9347f9724ca083b17e39555c36fd9007
14|kristel|6896ba7b11a62cacffbdaded457c6d92
15|TEST_!|bef2629065c222a780525fa82ee1c4dc
16|afiliados|098f6bcd4621d373cade4e832627b4f6
17|htb|53cc5f9c06df19a98e73eccd024670ac
18|hello|5d41402abc4b2a76b9719d911017c592
19|ognard|519aa79f2a559c5021fd5d4944eb60e1
20|nadouille|471c75ee6643a10934502bdafee198fb
21|test|81dc9bdb52d04dc20036dbd8313ed055
```

! search for version numbers, find a CVE
! if you can't do something obvious (get revshell), see how the underlying stuff work.


there is a service running on `127.0.0.1:8080`.
`curl --head` => it's vulnerable

# CVE-2024-23334

The root cause of this vulnerability lies in the way aiohttp handles static file serving
when follow_symlinks is enabled.

If an attacker can construct a malicious URL that leverages symlinks, they can potentially
access files or directories that are normally restricted.

## ssh tunnel

so `ssh -L 7000:localhost:8080 rosa@10.10.16.33 -fN`
now `gobuster` => `/assets 403`

then a script to brute force the needed `../`.

! why it took me so long? 1. because I didn't notice the version; was looking for something
more impressive 2. I didn't understand the payload
