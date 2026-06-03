# 📚 alipzsh — Knowledge Base

> A personal security & development knowledge base built with Obsidian, tracked in Git.
> 186 commits · Python & Shell · [View on GitHub](https://github.com/alipzsh/knowledge-base)

---

## What I've Learned

This knowledge base documents a focused journey into **web application security and ethical hacking**, built from the ground up across several interconnected disciplines:

- **Web vulnerability research** — deep, practical coverage of every major OWASP category: XSS in all its forms (reflected, stored, DOM-based, blind), SQL injection (UNION, blind boolean, blind time-delay, error-based, routed), SSRF, XXE, NoSQL injection, IDOR, and broken access control.
- **WAF evasion** — dedicated study of how to bypass Web Application Firewalls, including filter confusion, HTML tag tricks, JavaScript execution blocks, and XSS filter bypass techniques.
- **Cryptography** — well beyond typical web security learners: AES/AES-ECB, chosen-plaintext attacks with prefix, suffix, and HTTP variants, HMAC, JWT, and OAuth. Lecture notes indicate structured coursework, not just ad-hoc reading.
- **Recon & bug bounty methodology** — a complete recon workflow: subdomain and directory enumeration, active crawling, dorking, Wayback Machine, and attack surface expansion. Includes both current and archived methodologies.
- **Linux & systems** — privilege escalation, SUID exploitation, Linux storage, QEMU, LXC containers, FreeBSD and OpenBSD, and AWS EC2.
- **Networking** — HTTP, DNS, IP, subnetting, transport layer, tcpdump, nslookup, and netcat at a practical level.
- **Programming for security** — Python (including the `requests` library for custom tooling), JavaScript, React, Golang, and shell scripting — all oriented toward building security tools and automation.
- **SIEM / log analysis** — Splunk search & reporting, BOTSv1 CTF scenario, practical query writing.
- **Hands-on labs** — Hack The Box, Root-Me, Natas wargames, with writeups demonstrating applied learning.

---

## 🔐 Web Vulnerabilities

### XSS
| Topic | Link |
|---|---|
| XSS overview | [xss.md](https://github.com/alipzsh/knowledge-base/blob/master/xss.md) |
| Reflected XSS | [Reflected XSS.md](https://github.com/alipzsh/knowledge-base/blob/master/Reflected%20XSS.md) |
| Reflected XSS — custom tags only | [Reflected XSS just custom tags allowed.md](https://github.com/alipzsh/knowledge-base/blob/master/Reflected%20XSS%20just%20custom%20tags%20allowed.md) |
| Stored XSS | [Stored XSS.md](https://github.com/alipzsh/knowledge-base/blob/master/Stored%20XSS.md) |
| DOM-based XSS | [DOM-based XSS.md](https://github.com/alipzsh/knowledge-base/blob/master/DOM-based%20XSS.md) |
| Stored DOM XSS | [Stored DOM XSS.md](https://github.com/alipzsh/knowledge-base/blob/master/Stored%20DOM%20XSS.md) |
| Reflected DOM XSS | [Reflected DOM XSS.md](https://github.com/alipzsh/knowledge-base/blob/master/Reflected%20DOM%20XSS.md) |
| Blind XSS | [BLIND XSS.md](https://github.com/alipzsh/knowledge-base/blob/master/BLIND%20XSS.md) |
| XSS contexts | [XSS contexts.md](https://github.com/alipzsh/knowledge-base/blob/master/XSS%20contexts.md) |
| XSS in HTML tags | [XSS html tags.md](https://github.com/alipzsh/knowledge-base/blob/master/XSS%20html%20tags.md) |
| XSS out of tags | [XSS out of tags.md](https://github.com/alipzsh/knowledge-base/blob/master/XSS%20out%20of%20tags.md) |
| XSS examples | [XSS_examples.md](https://github.com/alipzsh/knowledge-base/blob/master/XSS_examples.md) |
| DOM-based manipulation | [DOM based manipulation.md](https://github.com/alipzsh/knowledge-base/blob/master/DOM%20based%20manipulation.md) |

### SQL Injection
| Topic | Link |
|---|---|
| SQL injection overview | [SQLi.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi.md) |
| UNION attack | [SQLi UNION.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20UNION.md) |
| UNION — column count | [SQLi UNION Column Count.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20UNION%20Column%20Count.md) |
| UNION — compatible columns | [SQLi UNION Compatible Column.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20UNION%20Compatible%20Column.md) |
| Blind SQLi | [SQLi Blind.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20Blind.md) |
| Blind — boolean-based | [SQLi Blind boolean.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20Blind%20boolean.md) |
| Blind — time delays | [SQLi Blind Time Delays.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20Blind%20Time%20Delays.md) |
| Blind — error-based | [SQLi Blind Error Based.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20Blind%20Error%20Based.md) |
| Error-based SQLi | [SQLi Error Based.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20Error%20Based.md) |
| Routed SQLi | [SQLi Routed.md](https://github.com/alipzsh/knowledge-base/blob/master/SQLi%20Routed.md) |
| NoSQL injection | [NoSQLI.md](https://github.com/alipzsh/knowledge-base/blob/master/NoSQLI.md) |

### Access Control
| Topic | Link |
|---|---|
| Broken access control | [BrokenAccessControl.md](https://github.com/alipzsh/knowledge-base/blob/master/BrokenAccessControl.md) |
| IDOR | [IDOR.md](https://github.com/alipzsh/knowledge-base/blob/master/IDOR.md) |

### Server-Side Attacks
| Topic | Link |
|---|---|
| SSRF | [SSRF.md](https://github.com/alipzsh/knowledge-base/blob/master/SSRF.md) |
| XXE | [xxe.md](https://github.com/alipzsh/knowledge-base/blob/master/xxe.md) |
| OGNL injection (Apache Struts) | [OGNL.md](https://github.com/alipzsh/knowledge-base/blob/master/OGNL.md) |
| Buffer overflow | [buffer_overflow.md](https://github.com/alipzsh/knowledge-base/blob/master/buffer_overflow.md) |

### Authentication & Miscellaneous
| Topic | Link |
|---|---|
| Authentication | [authentication.md](https://github.com/alipzsh/knowledge-base/blob/master/authentication.md) |
| 403 bypass | [403_bypass.md](https://github.com/alipzsh/knowledge-base/blob/master/403_bypass.md) |
| Critical areas to test | [Critical areas to test.md](https://github.com/alipzsh/knowledge-base/blob/master/Critical%20areas%20to%20test.md) |

---

## 🔓 WAF & Filter Evasion

| Topic | Link |
|---|---|
| Bypass WAF | [bypass WAF.md](https://github.com/alipzsh/knowledge-base/blob/master/bypass%20WAF.md) |
| Bypass blocks | [bypass blocks.md](https://github.com/alipzsh/knowledge-base/blob/master/bypass%20blocks.md) |
| Bypass XSS filters | [bypass xss filters.md](https://github.com/alipzsh/knowledge-base/blob/master/bypass%20xss%20filters.md) |
| WAF confusion | [WAF confusion.md](https://github.com/alipzsh/knowledge-base/blob/master/WAF%20confusion.md) |
| WAF blocks in HTML tags | [WAF blocks in HTML tags.md](https://github.com/alipzsh/knowledge-base/blob/master/WAF%20blocks%20in%20HTML%20tags.md) |
| WAF blocks during JS execution | [WAF blocks while JS execution.md](https://github.com/alipzsh/knowledge-base/blob/master/WAF%20blocks%20while%20JS%20execution.md) |
| URL validation bypass | [URL_validation.md](https://github.com/alipzsh/knowledge-base/blob/master/URL_validation.md) |

---

## 🔑 Cryptography & Auth

| Topic | Link |
|---|---|
| AES overview | [AES.md](https://github.com/alipzsh/knowledge-base/blob/master/AES.md) |
| AES-ECB chosen-plaintext attack | [AES-ECB-CPA.md](https://github.com/alipzsh/knowledge-base/blob/master/AES-ECB-CPA.md) |
| AES-ECB CPA — prefix | [AES-ECB-CPA-Prefix.md](https://github.com/alipzsh/knowledge-base/blob/master/AES-ECB-CPA-Prefix.md) |
| AES-ECB CPA — prefix 2 | [AES-ECB-CPA-Prefix2.md](https://github.com/alipzsh/knowledge-base/blob/master/AES-ECB-CPA-Prefix2.md) |
| AES-ECB CPA — prefix miniboss | [AES-ECB-CPA-Prefix-miniboss.md](https://github.com/alipzsh/knowledge-base/blob/master/AES-ECB-CPA-Prefix-miniboss.md) |
| AES-ECB CPA — suffix | [AES-ECB-CPA-suffix.md](https://github.com/alipzsh/knowledge-base/blob/master/AES-ECB-CPA-suffix.md) |
| AES-ECB CPA — HTTP | [AES-ECB-CPA-HTTP.md](https://github.com/alipzsh/knowledge-base/blob/master/AES-ECB-CPA-HTTP.md) |
| HMAC | [HMAC.md](https://github.com/alipzsh/knowledge-base/blob/master/HMAC.md) |
| JWT | [JWT.md](https://github.com/alipzsh/knowledge-base/blob/master/JWT.md) |
| OAuth | [OAuth.md](https://github.com/alipzsh/knowledge-base/blob/master/OAuth.md) |
| Crypto lecture 10 | [Crypto lecture 10.md](https://github.com/alipzsh/knowledge-base/blob/master/Crypto%20lecture%2010.md) |

---

## 🌐 Web Fundamentals

| Topic | Link |
|---|---|
| HTTP | [http.md](https://github.com/alipzsh/knowledge-base/blob/master/http.md) |
| HTML | [html.md](https://github.com/alipzsh/knowledge-base/blob/master/html.md) |
| HTML attributes | [HTML attributes.md](https://github.com/alipzsh/knowledge-base/blob/master/HTML%20attributes.md) |
| DOM | [DOM.md](https://github.com/alipzsh/knowledge-base/blob/master/DOM.md) |
| JSON | [JSON.md](https://github.com/alipzsh/knowledge-base/blob/master/JSON.md) |
| XML | [XML.md](https://github.com/alipzsh/knowledge-base/blob/master/XML.md) |
| API overview | [API.md](https://github.com/alipzsh/knowledge-base/blob/master/API.md) |
| API analysis | [API analysis.md](https://github.com/alipzsh/knowledge-base/blob/master/API%20analysis.md) |
| API endpoints | [API endpoints.md](https://github.com/alipzsh/knowledge-base/blob/master/API%20endpoints.md) |
| API endpoints by HTTP verb | [API endpoints by HTTP verb.md](https://github.com/alipzsh/knowledge-base/blob/master/API%20endpoints%20by%20HTTP%20verb.md) |
| API endpoint shape | [API endpoints shape.md](https://github.com/alipzsh/knowledge-base/blob/master/API%20endpoints%20shape.md) |

---

## 🔍 Recon & Bug Bounty

| Topic | Link |
|---|---|
| Recon overview | [recon.md](https://github.com/alipzsh/knowledge-base/blob/master/recon.md) |
| Subdomain enumeration | [subdomain enumeration.md](https://github.com/alipzsh/knowledge-base/blob/master/subdomain%20enumeration.md) |
| Directory enumeration | [directory enumeration.md](https://github.com/alipzsh/knowledge-base/blob/master/directory%20enumeration.md) |
| Active crawling | [active crawling.md](https://github.com/alipzsh/knowledge-base/blob/master/active%20crawling.md) |
| Wayback machine | [wayback machine.md](https://github.com/alipzsh/knowledge-base/blob/master/wayback%20machine.md) |
| Dorking | [Dorking.md](https://github.com/alipzsh/knowledge-base/blob/master/Dorking.md) |
| Increase attack surface | [Increase the attack surface.md](https://github.com/alipzsh/knowledge-base/blob/master/Increase%20the%20attack%20surface.md) |
| Bug bounty methodology | [bug_bounty.md](https://github.com/alipzsh/knowledge-base/blob/master/bug_bounty.md) |
| Bug bounty recon (archived) | [bug_bounty_recon_old.md](https://github.com/alipzsh/knowledge-base/blob/master/bug_bounty_recon_old.md) |
| Example queries | [Example queries.md](https://github.com/alipzsh/knowledge-base/blob/master/Example%20queries.md) |

---

## 🌍 Networking

| Topic | Link |
|---|---|
| Networking overview | [networking.md](https://github.com/alipzsh/knowledge-base/blob/master/networking.md) |
| Transport layer | [transport_layer.md](https://github.com/alipzsh/knowledge-base/blob/master/transport_layer.md) |
| IP | [ip.md](https://github.com/alipzsh/knowledge-base/blob/master/ip.md) |
| Subnetting | [subnet.md](https://github.com/alipzsh/knowledge-base/blob/master/subnet.md) |
| DNS | [DNS.md](https://github.com/alipzsh/knowledge-base/blob/master/DNS.md) |
| Hosts file | [hosts.md](https://github.com/alipzsh/knowledge-base/blob/master/hosts.md) |
| nslookup | [nslookup.md](https://github.com/alipzsh/knowledge-base/blob/master/nslookup.md) |
| Bridge networking | [bridge.md](https://github.com/alipzsh/knowledge-base/blob/master/bridge.md) |

---

## 🐧 Linux & Systems

| Topic | Link |
|---|---|
| Privilege escalation | [privilege_Escalation.md](https://github.com/alipzsh/knowledge-base/blob/master/privilege_Escalation.md) |
| SUID | [SUID.md](https://github.com/alipzsh/knowledge-base/blob/master/SUID.md) |
| Linux storage | [Linux storage.md](https://github.com/alipzsh/knowledge-base/blob/master/Linux%20storage.md) |
| BIOS | [bios.md](https://github.com/alipzsh/knowledge-base/blob/master/bios.md) |
| QEMU | [qemu.md](https://github.com/alipzsh/knowledge-base/blob/master/qemu.md) |
| LXC | [lxc.md](https://github.com/alipzsh/knowledge-base/blob/master/lxc.md) |
| FreeBSD | [FreeBSD.md](https://github.com/alipzsh/knowledge-base/blob/master/FreeBSD.md) |
| OpenBSD | [OpenBSD.md](https://github.com/alipzsh/knowledge-base/blob/master/OpenBSD.md) |
| EC2 (AWS) | [EC2.md](https://github.com/alipzsh/knowledge-base/blob/master/EC2.md) |
| TLCL (The Linux Command Line) | [TLCL.md](https://github.com/alipzsh/knowledge-base/blob/master/TLCL.md) |

---

## 💻 Programming

| Topic | Link |
|---|---|
| Python | [python.md](https://github.com/alipzsh/knowledge-base/blob/master/python.md) |
| Python requests | [python requests.md](https://github.com/alipzsh/knowledge-base/blob/master/python%20requests.md) |
| JavaScript | [js.md](https://github.com/alipzsh/knowledge-base/blob/master/js.md) |
| JS APIs | [js APIs.md](https://github.com/alipzsh/knowledge-base/blob/master/js%20APIs.md) |
| React | [react.md](https://github.com/alipzsh/knowledge-base/blob/master/react.md) |
| Golang | [golang.md](https://github.com/alipzsh/knowledge-base/blob/master/golang.md) |
| Bash — IF statements | [bash IF statement.md](https://github.com/alipzsh/knowledge-base/blob/master/bash%20IF%20statement.md) |
| Bash — string manipulation | [bash: get first characters of a string.md](https://github.com/alipzsh/knowledge-base/blob/master/bash%3A%20get%20first%20characters%20of%20a%20string.md) |
| Automation | [automation.md](https://github.com/alipzsh/knowledge-base/blob/master/automation.md) |
| Automate node management | [automate node management.md](https://github.com/alipzsh/knowledge-base/blob/master/automate%20node%20management.md) |
| Action object pattern | [action_object.md](https://github.com/alipzsh/knowledge-base/blob/master/action_object.md) |
| Checker function pattern | [checker function.md](https://github.com/alipzsh/knowledge-base/blob/master/checker%20function.md) |

---

## 🛠️ Tools

| Topic | Link |
|---|---|
| curl | [curl.md](https://github.com/alipzsh/knowledge-base/blob/master/curl.md) |
| netcat | [netcat.md](https://github.com/alipzsh/knowledge-base/blob/master/netcat.md) |
| tcpdump | [tcpdump.md](https://github.com/alipzsh/knowledge-base/blob/master/tcpdump.md) |
| SSH | [ssh.md](https://github.com/alipzsh/knowledge-base/blob/master/ssh.md) |
| git | [git.md](https://github.com/alipzsh/knowledge-base/blob/master/git.md) |
| Apache | [Apache.md](https://github.com/alipzsh/knowledge-base/blob/master/Apache.md) |
| Apache Maven | [Apache_maven.md](https://github.com/alipzsh/knowledge-base/blob/master/Apache_maven.md) |
| Apache Struts | [Apache_struts.md](https://github.com/alipzsh/knowledge-base/blob/master/Apache_struts.md) |
| Splunk | [Splunk.md](https://github.com/alipzsh/knowledge-base/blob/master/Splunk.md) |
| Splunk search & reporting | [Splunk Search & Reporting.md](https://github.com/alipzsh/knowledge-base/blob/master/Splunk%20Search%20%26%20Reporting.md) |

---

## 🧪 Labs & Practice

| Topic | Link |
|---|---|
| Hack The Box | [hack the box.md](https://github.com/alipzsh/knowledge-base/blob/master/hack%20the%20box.md) |
| Root-Me | [Root-Me.md](https://github.com/alipzsh/knowledge-base/blob/master/Root-Me.md) |
| Natas wargame | [natas.md](https://github.com/alipzsh/knowledge-base/blob/master/natas.md) |
| Writeups | [writeups.md](https://github.com/alipzsh/knowledge-base/blob/master/writeups.md) |
| BOTSv1 (Splunk CTF) | [botsv1.md](https://github.com/alipzsh/knowledge-base/blob/master/botsv1.md) |
| Boss (CTF) | [boss.md](https://github.com/alipzsh/knowledge-base/blob/master/boss.md) |
| Answer these questions | [answer these questions.md](https://github.com/alipzsh/knowledge-base/blob/master/answer%20these%20questions.md) |

---

## 📖 Reference & Notes

| Topic | Link |
|---|---|
| Books reading list | [books.md](https://github.com/alipzsh/knowledge-base/blob/master/books.md) |
| Bios / about | [bios.md](https://github.com/alipzsh/knowledge-base/blob/master/bios.md) |

---

*Generated from [alipzsh/knowledge-base](https://github.com/alipzsh/knowledge-base) · 186 commits*
