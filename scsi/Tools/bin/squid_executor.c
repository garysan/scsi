/*
   Programa para forzar al reinicio de squid -k (reconfiguracion de parametros)
*/
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h> 
#include <stdlib.h>

#define SQUID_BINARY "/usr/sbin/squid"

int main(int argc, char **argv, char **envp) {
  char *squidprog[] = { SQUID_BINARY, "-k", "reconfigure", NULL };

  setuid( 0 ); 
/*
  system(SQUID_BINARY" -k reconfigure");
*/
  int ret = execve(squidprog[0], squidprog, envp);

  if (ret == -1 )
      perror("No se pudo reconfigurar Squid" );
  return 0;
}
