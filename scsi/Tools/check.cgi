#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

my $usuario = &validate;

######### config Area #########
if ($config::squidver eq "2"){
    $squidconf = $config::squidconf;
    $squidbin = $config::squidbin;
    $sgbf = $config::sgbf;
}

if ($config::squidver eq "3"){
    $squidconf = $config::squid3conf;
    $squidbin = $config::squid3bin;
    $sgbf = $config::sgbf3;
}

$cssfile = $config::cssfile;
$patchdir = $config::patchdir;
######################################

$exists = "<font color=green>Existe</font>";
$doesnotexist = "<font color=red>No existe</font>";
$readable = ", <font color=green>Legible</font>";
$notreadable = ", <font color=red>No Legible</font>";
$writable = ", <font color=green>Escritura permitida</font>";
$notwritable = ", <font color=red>No se permite escritura</font>";
$executable = ", <font color=green>Ejecutable</font>";
$notexecutable = ", <font color=red>No Ejecutable</font>";


$name = getpwuid($>);

$msg = " $config::title Corre bajo el nombre de usuario <i>$name</i><br><br>";

# Verificar archivo de configuracion Squid
$msg .= "<b>Archivo de configuracion Squid</b><br>\n";
if (-e $squidconf) {
	$msg .= $exists;

	if (-r $squidconf) {
		$msg .= $readable;
                
	} else { $msg .= $notreadable }
	if (-w $squidconf) {
		$msg .= $writable;
	} else { $msg .= $notwritable }
} else { 
	$msg .=$doesnotexist;
}
$msg .= "<br><br>\n";

#Verificar estado del Binario Squid
$msg .= "<b>Binario de Squid</b><br>\n";
if (-e $squidbin) {
        $msg .= $exists;
        if (-x $squidbin) {
                $msg .= $executable;
        } else { $msg .= $notexecutable }
	} else {
	        $msg .=$doesnotexist;
}
$msg .= "<br><br>\n";

#Verificar estado de IPTables
$msg .= "<b>Binario de IPTables</b><br>\n";
if (-e $iptables) {
        $msg .= e$xists;
        if (-x $iptables) {
                $msg .= $executable;
        } else { $msg .= $notexecutable }
	} else {
	        $msg .=$doesnotexist;
}
$msg .= "<br><br>\n";

#Verificar config.pm
$msg .= "<b>Archivo maestro de Configuracion</b><br>\n";
if (-e "../Config/config.pm") {
	$msg .= $exists;
	if (-r "config.pm") {
		$msg .= $readable;
	} else { $msg .= $notreadable }
	if (-w "config.pm") {
		$msg .= $writable;
	} else { $msg .= $notwritable }
} else { 
	$msg .=$doesnotexist;
}
$msg .= "<br><br>\n";

#Verificaar Squidguard!
if ($sgbf ne "") {
	$msg .= "<b>SquidGuard</b><br>\n";
		if (-e $sgbf) {
			$msg .= $exists;
			if (-r $sgbf) {
				$msg .= $readable;
			} else { $msg .= $notreadable }
			if (-w $sgbf) {
				$msg .= $writable;
			} else { $msg .= $notwritable }
		} else { 
			$msg .=$doesnotexist;
		}
	$msg .= "<br><br>\n";
}

#Verificar directorio de cambios.
if ( $patchdir ne ""){
	$msg .= "<b>Directorio de modificaciones y logs</b><br>\n";
	if (-d $patchdir){
			$msg .= $exists;
			if (-r $patchdir) {
				$msg .= $readable;
			}else{ $msg .= $notreadable }
			if (-w $patchdir) {
				$msg .= $writable;
			}else{ $msg .= $notwritable}
		} else {
			$msg .= "$doesnotexist, debe crear el directorio /patchdir";
		}
	$msg .= "<br><br>\n";
}

$msg .= "<br><center><a href=\"check.cgi\">Verificar nuevamente</a></center>";
#shared::htmlbox
shared::header();
print qq(
    <div class="contenedor">
    <h3>Verificando Archivos</h3>
    <br/>$msg
    </div>
);
