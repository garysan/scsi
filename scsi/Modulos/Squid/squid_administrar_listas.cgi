#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

shared::header ("","squid.js");
shared::modulo ("Permitir/Rechazar a Listas especificas");
######### config Area #########
if ($config::squidver eq "2"){
    $squidconf = $config::squidconf;
}
if ($config::squidver eq "3"){
    $squidconf = $config::squid3conf;
}

######################################
if (!open(SQUIDCONF, "$squidconf")){
    &box("Error","El archivo $squidconf no existe.");
    die;
}
$message .= "<div id=alinear>";
$message .= "<table id=\"tabla_lista\">";
$message .=  "<tr><th>Lista</th><th>Estado</th><th>Modificar</th>";
$i = 0;
$search = 0;

while ($linea=<SQUIDCONF>)
{
    my @valores=split(' ',$linea);
    
    if ($valores[1] eq "ACCESO" ) { 
        $search = 1; 
    }
    if ($search == 1) { 
        if ($valores[0] eq "#http_access") {
            $i+=1;
            $len=@valores;
            
            $message .= "<input type=hidden id=\"anterior$i\" value=\"$linea\"></td>";            
			for (my $count=2; $count<=$len-1;$count++){
				$message .= "<tr>";
				$message .= "<td>".$valores[$count]."</td>";
                                $message .= "<td>Desactivado</td>";
				$message .= "<td><input class=button type=button value=Activar onclick=listas($i,'$valores[$count]',1)></td>";
				$message .= "</tr>";		
			}
        }
        if ($valores[0] eq "http_access") {
            $i+=1;
            $len=@valores;
            
            $message .= "<input type=hidden id=\"anterior$i\" value=\"$linea\"></td>";            
			for (my $count=2; $count<=$len-1;$count++){
				$message .= "<tr>";
				$message .= "<td>".$valores[$count]."</td>";
                                $message .= "<td>Activado</td>";
				$message .= "<td><input class=button type=button value=Desactivar onclick=listas($i,'$valores[$count]',0)></td>";
				$message .= "</tr>";		
			}
        }
        if ($valores[1] eq "END_ACCESO"){
                $search =2;
        }
    }
};
close (SQUIDCONF);

if ($search == 0) {
    &box("Error","El archivo $squidconf, no esta correctamente configurado, Lea el README del programa.");
    die;
}

$message .= "</table></div>
<input type=hidden id=\"archivo\" name=\"archivo\" value=\"$squidconf\">
<input type=hidden id=\"number\" name=\"number\" value=\"$i\">
<input type=hidden id=\"flag\" name=\"flag\" value=\"2\">
<br>
<div id=\"resultado\"></div>

</BODY></HTML>";

print $message;


