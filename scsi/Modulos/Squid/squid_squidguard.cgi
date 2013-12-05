#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
use File::Basename;

my $usuario = &validate;

shared::header ("","squid.js");
$filename = $config::squidconf;
shared::modulo ("Administrar el estado de SquidGuard!");
######### config Area #########
$squidconf = $config::squidconf;
######################################
if (!open(SQUIDCONF, "$squidconf"))
{
	&box("Error","El archivo $squidconf no existe.");
	die;
}
###########################################################################################
$message .= "<div id=alinear>";
$message .= "<table id=\"tabla_general\">";
$message .=  "<tr><th>Variable</th><th>Estado Actual</th><th>Cambiar Estado</th>";
$search = 0;

while ($linea=<SQUIDCONF>)
{
	my @valores=split(' ',$linea);
	
	if ($valores[1] eq "SQUID_GUARD" ) { 
		$search = 1;
	}
	if ($valores[1] eq "END_SQUID_GUARD"){
		$search =9;	    
	}
	if ($search == 1) { 
		
		if ($valores[0] eq "#url_rewrite_program") {
			$i+=1;
			$message .= "<tr>";
           	$var =$valores[0] ;
           	$var =~s/\#//;
           	$message .= "<input type=hidden id=\"original$i\" value=\"$linea\">";
			#$message .= "<td><input id=\"original$i\" value=\"$linea\"></td>";
           	$message .= "<td><b>$var</b></td>";
           	$message .= "<td>Desactivado</td>";
           	$message .= "<td><input class=button type=button value=Activar onclick=squidguard('$i',1)></td>";
           	$message .= "</tr>";
		}      	
		if ($valores[0] eq "url_rewrite_program") {
			$i+=1;
			$message .= "<tr>";
           	$var =$valores[0] ;
           	$var =~s/\#//;
           	$message .= "<input type=hidden id=\"original$i\" value=\"$linea\">";
			#$message .= "<td><input id=\"original$i\" value=\"$linea\"></td>";
           	$message .= "<td><b>$var</b></td>";
           	$message .= "<td>Activado</td>";
           	$message .= "<td><input class=button type=button value=Desactivar onclick=squidguard('$i',0)></td>";
           	$message .= "</tr>";
		}	   	
	}	
};
$message .= "</table></div><br/>
<input type=hidden id=\"archivo\" name=\"archivo\" value=\"$filename\">";
$message .= "<div id=\"resultado\"></div>";

if ($search == 0) {
    &box("Error","El archivo $squidconf, no esta correctamente configurado, Lea el README del programa.");
    die;
}



print $message;

