# buffer_overflow
* Exploitation: If an attacker can control the content of the overflowed
  data, they may strategically craft malicious input to overwrite
  important information, such as function pointers or return addresses on
  the call stack. This can lead to the execution of arbitrary code
  supplied by the attacker.

* Code Injection: In a buffer overflow attack, an attacker may exploit the
  overflow to inject and execute their own code. By overwriting function
  pointers or return addresses, an attacker can redirect the program's
  execution flow to a location in memory where they have injected
  malicious code.

* Privilege Escalation: Buffer overflow vulnerabilities are often
  exploited to gain unauthorized access or escalate privileges. If an
  attacker can execute arbitrary code in the context of the compromised
  program, they may use this to launch further attacks or take control of
  the system.

* If correctly crafted, it is possible overwrite the return address with
  a user-defined value.
• It is possible to cause a jump to user-defined code (e.g., code that
  invokes a shell).
• The code will be executed with the privileges of the running program.
