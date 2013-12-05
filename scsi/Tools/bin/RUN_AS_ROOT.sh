#!/bin/sh
### PARAMETROS ###
PATH=/usr/sbin:/sbin:/bin:/usr/bin
gcc iptables_executor.c -o iptables_executor
gcc squid_copy.c -o squid_copy
gcc squid_delete.c -o squid_delete
gcc squid_executor.c -o squid_executor
gcc squid_perm.c -o squid_perm
chown root:root iptables_executor
chown root:root squid_copy
chown root:root squid_delete
chown root:root squid_executor
chown root:root squid_perm
chmod +s iptables_executor
chmod +s squid_copy
chmod +s squid_delete
chmod +s squid_executor
chmod +s squid_perm
