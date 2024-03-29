package config;

########Archivos de Configuacion#########
$squidver= "3";
$squidbin = "/usr/sbin/squid";
$squidconf = "/etc/squid/squid.conf";
$sgbf = "/etc/squid/squidGuard.conf";

$squid3bin = "/usr/sbin/squid3";
$squid3conf = "/etc/squid3/squid.conf";
$sgbf3 = "/etc/squid3/squidGuard.conf";

$iptables = "/sbin/iptables";
$iptablesconf = "/home/scripts/00-firewall.sh";
$cssfile = "/css/estilo.css";
$patchdir = "/patchdir";
$scsiroot = "/scsi/scsi/";

##$master = "/etc/squid/master";
##$clientes = "/etc/squid/clientes";
##$internet = "/etc/squid/internet";
##$denegados = "/etc/squid/denegados";

########Parametros de Sistema#########
$cookielife="1d"; ####Este parametro indica el tiempo de vida del cookie
$squid=1;
$squid_guard=1;
$iptables=1;
$ipsystem="localhost";
$hostbase=$ipsystem;
$database="scsi";
$userbase="scsi";
$passbase="scsi";

########Mensajes de Sistema#########
$version="1.0";
$swver ="v$version";
$progmod="Beta";
$title = "SCSI";
$progname = "Sistema de Control de Servicio de Internet";
$progabre = "SCSI";
$bienvenido = "Bienvenido al $progname $progabre Largo el Camino es Servidores administrar debes, estamos dando inicio y con paso fuerte!";

$msg000 = "Menu Principal";
$msg001 = "Aviso Legal";
$msg002 = "Parametros";
$msg003 = "Administración";
$msg004 = "Archivos";
$msg005 = "Verifique los permisos generales:";
$msg006 = "Configuración";
$msg007 = "Herramientas";
$msg008 = "Utilidades";
$msg009 = "";
$msg010 = "";
$msg011 = "";
$msg012 = "";
$msg013 = "";
$msg014 = "";
$msg015 = "";
$msg016 = "";
$msg017 = "";
$msg018 = "";
$msg019 = "";
$msg020 = "Nombre";
$msg021 = "Valor Actual";
$msg022 = "Nuevo Valor";
$msg023 = "Editar";
$msg024 = "Archivo";
$msg025 = "";
$msg026 = "";
$msg027 = "";
$msg028 = "";
$msg029 = "";
$msg030 = "";

return 1;