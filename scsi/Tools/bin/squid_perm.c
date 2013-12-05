/*
   Programa para cambiar el permiso del access.log a la ruta de logs de scsi
*/
#include <stdio.h>
#include <errno.h>
#include <sys/types.h> 
#include <stdlib.h>
#include <sys/stat.h>
#define SQUID_ACC "/var/log/squid/access.log"
#define SQUID_DIR "/var/log/squid/"

int main(int argc, char **argv, char **envp) {
  setuid( 0 ); 
  int ret= chmod(SQUID_ACC, S_IRWXU|S_IRWXG|S_IRWXO);
  int dir= chmod(SQUID_DIR, S_IRWXU|S_IRWXG|S_IRWXO);
  if (ret == -1 )
      perror("No se pudo cambiar los permisos de forma correcta" );
  if (dir == -1 )
      perror("No se pudo cambiar los permisos de forma correcta" );
  return 0;
}
