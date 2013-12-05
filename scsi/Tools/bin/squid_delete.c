/*
   Programa para copiar el access.log a la ruta de logs de scsi
*/
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h> 
#include <stdlib.h>

#define SQUID_ACC "/var/log/squid/access.log"

#define DEST_ACC "/scsi/scsi/logs/access.log"
#define MV "/bin/rm"


int main(int argc, char **argv, char **envp) {
  char *cpprog[] = { MV, DEST_ACC, NULL };

  setuid( 0 ); 

  int ret = execve(cpprog[0], cpprog, envp);
  
  if (ret == -1 ){
      perror("error al borrar" );
  }
  
  return 0;
}
