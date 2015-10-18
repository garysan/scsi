/*
   Programa para ejecutar el script de iptables
*/
#include <stdio.h>

#include <errno.h>
#include <sys/types.h> 
#include <stdlib.h>
#include <sys/stat.h>

#define IPTABLES "/home/scripts/00-firewall.sh"
#define SH "/bin/sh"

int main(int argc, char **argv, char **envp) {
  char *iptables[] = { SH,IPTABLES, NULL };
  setuid( 0 ); 
 
  int ret = execve(iptables[0], iptables, envp);

  if (ret == -1 )
      perror("No se pudo ejecutar el script requerido" );
  return 0;
}
