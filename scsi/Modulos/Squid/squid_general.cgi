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
shared::modulo ("$config::msg002");
######### config Area #########
if ($config::squidver eq "2"){
    $squidconf = $config::squidconf;
}
if ($config::squidver eq "3"){
    $squidconf = $config::squid3conf;
}
$filename = $squidconf;
######################################
if (!open(SQUIDCONF, "$squidconf"))
{
	&box("Error","El archivo $squidconf no existe.");
	die;
}
###########################################################################################
$message .= "<div id=alinear>";
$message .= "<table id=\"tabla_general\">";
#$message .=  "<tr><th>$config::msg020</th><th>$config::msg021</th><th>$config::msg022</th>";
$search = 0;

while ($linea=<SQUIDCONF>){

	($a,$b,$c,$d) = split (' ',$linea); #Dividir cada linea
	
	if ($b eq "RED_SOPORTADA" ) { 
		$search = 1;
	}
	if ($b eq "END_RED_SOPORTADA"){
		$search =9;	    
	}
	if ($search == 1) { 
		if ($a eq "acl") {
			$i+=1;
			$message .= "<tr>";
			$message .= "<input type=hidden id=\"original$i\" value=\"$linea\">";
			$message .= "<td><b>Red Soportada:</b></td>";            	
            ($ip,$subnet)= split('/',$d);
          	$message .= "<td><input id=\"ip$i\" value=$ip class=\"texto\"></td>";
          	$message .= "<td><input id=\"subnet$i\" value=$subnet class=\"texto\"></td>";
           	$message .= "<input type=hidden id=\"ant$i\" value=\"$ip/$subnet\">";
           	$message .= "<td><input class=button type=button value=Modificar onclick=parser_ip('$i')></td>";
           	$message .= "</tr>";
		}      	
	}
	#############dns
	if ($b eq "SERVIDOR_DNS" ) { 
		$search = 2;
	}
	if ($b eq "END_SERVIDOR_DNS"){
		$search =9;	    
	}
	if ($search == 2) { 
		if ($a eq "dns_nameservers") {
			$i+=1;
			$message .= "<tr>";
			$message .= "<input type=hidden id=\"original$i\" value=\"$linea\">";
			$message .= "<td><b>Servidor DNS:</b></td>";
          	$message .= "<td><input id=\"dns$i\" value=$b  class=\"texto\"></td>";
           	$message .= "<td><input type=hidden id=\"ant$i\" value=\"$b\"></td>";
           	$message .= "<td><input class=button type=button value=Modificar onclick=parser('$i','dns')></td>";
           	$message .= "</tr>";
		}      	
	}
	#############PUERTO HOSTNAME_SQUID
	if ($b eq "PUERTO_SQUID" ) { 
		$search = 3;
	}
	if ($b eq "END_PUERTO_SQUID"){
		$search =9;	    
	}
	if ($search == 3) { 
		if ($a eq "http_port") {
			$i+=1;
			$message .= "<tr>";
			$message .= "<input type=hidden id=\"original$i\" value=\"$linea\">";
			$message .= "<td><b>Puerto SQUID:</b></td>";
          	$message .= "<td><input id=\"puerto$i\" value=$b  class=\"texto\"></td>";
           	$message .= "<td><input type=hidden id=\"ant$i\" value=\"$b\"></td>";
           	$message .= "<td><input type=\"button\" onclick=\"parser('$i','puerto')\" id=\"modificar\" value=Modificar></td>";
           	$message .= "</tr>";
		}      	
	}
	############HOSTNAME_SQUID
	if ($b eq "HOSTNAME_SQUID" ) { 
		$search = 4;
	}
	if ($b eq "END_HOSTNAME_SQUID"){
		$search =9;	    
	}
	if ($search == 4) { 
		if ($a eq "visible_hostname") {
			$i+=1;
			$message .= "<tr>";
			$message .= "<input type=hidden id=\"original$i\" value=\"$linea\">";
			$message .= "<td><b>Hostname SQUID:</b></td>";
          	$message .= "<td><input id=\"hostname$i\" value=$b class=\"texto\"></td>";
           	$message .= "<td><input type=hidden id=\"ant$i\" value=\"$b\"></td>";
           	$message .= "<td><input type=\"button\" onclick=\"parser('$i','hostname')\" id=\"modificar\" value=Modificar></td>";
           	$message .= "</tr>";
		}      	
	}
        if ($b eq "SQUID_GUARD" ) { 
		$search = 5;
	}
	if ($b eq "END_SQUID_GUARD"){
		$search =9;	    
	}
        if ($search == 5) { 
		my @valores=split(' ',$linea);
		if ($valores[0] eq "#url_rewrite_program") {
			$i+=1;
			$message .= "<tr>";
           	$var =$valores[0] ;
           	$var =~s/\#//;
           	$message .= "<input type=hidden id=\"original$i\" value=\"$linea\">";
           	$message .= "<td><b>SQUIDGUARD:</b></td>";
                $message .= "<td>Desactivado</td>";
           	$message .= "<td></td>";
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
           	$message .= "<td><b>SQUIDGUARD:</b></td>";
                $message .= "<td>Activado</td>";
           	$message .= "<td></td>";
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

