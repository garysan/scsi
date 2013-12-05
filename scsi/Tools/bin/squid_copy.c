/*
   Programa para copiar el access.log a la ruta de logs de scsi
*/
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h> 
#include <stdlib.h>

#define SQUID_ACC "/var/log/squid/access.log"
#define SQUID_SGD "/var/log/squid/cache.log"
#define SQUID_CCH "/var/log/squid/squidGuard.log"
#define SQUID_STR "/var/log/squid/store.log"

#define DEST_ACC "/scsi/scsi/logs/access.log"
#define CP "/bin/cp"


int main(int argc, char **argv, char **envp) {
  char *cpprog[] = { CP, SQUID_ACC, DEST_ACC, NULL };

  setuid( 0 ); 

  int ret = execve(cpprog[0], cpprog, envp);

  if (ret == -1 ){
      perror("No se pudo copiar el archivo" );
  }
  return 0;
}
