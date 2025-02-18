# lab_setup

# the ideal situation:

* having multiple VMs, on a server host. at least one attack VM and
  multiple practice VMs (vulnerable or not).

# now

* I can't have two machines, but because I have a separate pc, I use the
  host as the attack machine.

* but if I'm trying things in a more realistic situation, like
  hackerone, even though I still could use the host, but a VM would be
  much more reusable.

# should I ssh to the host or the VM

* I don't see a reason not to directly ssh to the attack VM.
  * I won't need to transfer anything back to the local host (but could
    use ssh if I need to).

* there should be much more I can do. firewall things can get so
  complicated (and fun).
  * when firewall is on dell: incomings from ASUS, and host only in
    virtualbox are allowed.

* this is good enough, I should do and learn instead of overthinking, or
  the burnout would be here.
