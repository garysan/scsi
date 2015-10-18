#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

shared::header ("","squid.js");
shared::modulo ("Delay Pool's");
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
$message .= "<table border=1 id=\"tabla_delay\">";
$message .=  "<tr><th>Delay Nº</th><th>Clase</th><th>Velocidad Actual</th><th>Modificar/Establecer Velocidad</th>";

$i = 0;
$search = 0;

while ($linea=<SQUIDCONF>)
{
    my @valores=split(' ',$linea);
    
    if ($valores[1] eq "DELAYS" ) { 
        $search = 1; 
    }
    if ($valores[0] eq "delay_pools") {
		$i+=1;
		$cant= $valores[2];
		#$message .= "<b>Cantidad de Delays:</b> $valores[1]<br/>";
	}
    if ($search == 1) {
		if ($valores[0] eq "delay_class") {
			$message .= "<tr><td>$valores[1]</td>";
			$message .= "<td>$valores[2]</td>";
		}
		####       Global    Vel   Obj
		####  128000/128000 32000/56000
        if ($valores[0] eq "delay_parameters") {
        	$message .= "<input type=hidden id=\"original$valores[1]\" name=\"original$valores[1]\" value=\"$linea\">";
        	my @vel=split('/',$valores[2]);
        	$operacion = $vel[1]/1024;
        	my ( $kbps ) = $operacion =~ /(\d+)/;
        	if ($operacion < 0){
        		$kbps = $operacion = 0;		
        	}
			$message .= "<td><div class=\"kb\">$kbps Kbps</div></td>";
			$message .= "<td width=\"50%\"><p>
						 <div class=\"inputWrap\">
						 <b>Velocidad:</b>
						 	<input id=\"txt\" class=\"inputNumber\" size=\"3\" type=\"text\" value=\"$kbps\" > <b>Kbps</b>
						    <div class=\"slider\"></div> 
						 </div>
						 </td>";
		}
        if ($valores[0] eq "delay_access") {
			$message .= "<td>$valores[3]</td>";
		}
        ########Fin del archivo
        if ($valores[1] eq "END_DELAYS"){
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
<div>Para no controlar los kbps deben ser 0 (cero)</div>
<input type=hidden id=\"archivo\" name=\"archivo\" value=\"$squidconf\">
<input type=hidden id=\"number\" name=\"number\" value=\"$i\">
<input type=hidden id=\"flag\" name=\"flag\" value=\"2\">
<br>
<div id=\"resultado\"></div>

</BODY></HTML>";

print $message;


