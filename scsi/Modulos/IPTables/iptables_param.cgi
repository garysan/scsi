#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
use File::Basename;

my $usuario = &validate;

shared::header ("","iptables.js");
$filename = $config::iptablesconf;
shared::modulo ("Parametros Globales de IPTables");
######### config Area #########
$iptables = $config::iptablesconf;
######################################
if (!open(IPTABLES, "$iptables"))
{
	&box("Error","El archivo $iptables no existe.");
	die;
}
$message .= "<div id=alinear>";
$message .= "<table id=\"tabla_general\">";
$message .= "<tr><th>Descripción</th><th>Valor (Modificable)</th><th>Acciones</th></tr>";
$search = 0;

while (my $line=<IPTABLES>)
{
	$search=1;
	my @valores=split('=',$line);
	if ($search == 1) {
                $valores[1] =~ s/\n//g;
            	if ($valores[0]eq "SERVER"){
                    $i+=1;
                    my $var="server";
                    $message .= "\n<tr>";
                    $message .= "<td>" .$i. ". IP del Servidor SQUID:</td>";
                    $message .= "<td><input id=\"$var\" value=$valores[1] name=\"$var\"></td>";
                    $message .= "<td><input class=button type=button value=Modificar onclick=modificar('$var',$valores[1])></td>";
                    $message .= "</tr>";
                }
                if ($valores[0]eq "INTERNET"){
                    $i+=1;
                    my $var="inter";
                    $message .= "\n<tr>";
                    $message .= "<td>" .$i. ". Interfaz de Red (Externa):</td>";
                    $message .= "<td><input id=\"$var\" value=$valores[1] name=\"$var\"></td>";
                    $message .= "<td><input class=button type=button value=Modificar onclick=modificar('$var',$valores[1])></td>";
                    $message .= "</tr>";
                }
                if ($valores[0]eq "LAN_IN"){
                    $i+=1;
                    my $var="lan";
                    $message .= "\n<tr>";
                    $message .= "<td>" .$i. ". Interfaz de Red (Interna):</td>";
                    $message .= "<td><input id=\"$var\" value=$valores[1] name=\"$var\"></td>";
                    $message .= "<td><input class=button type=button value=Modificar onclick=modificar('$var',$valores[1])></td>";
                    $message .= "</tr>";
                }
                if ($valores[0]eq "SQUID_PORT"){
                    $i+=1;
                    my $var="puerto";
                    $message .= "\n<tr>";
                    $message .= "<td>" .$i. ". Puerto del servidor SQUID:</td>";
                    $message .= "<td><input id=\"$var\" value=$valores[1] name=\"$var\"></td>";
                    $message .= "<td><input class=button type=button value=Modificar onclick=modificar('$var',$valores[1])></td>";

                    $message .= "</tr>";
                }
                
	}
	
};####While!
$message .= "</table></div><br/>
<input type=hidden id=\"archivo\" name=\"archivo\" value=\"$filename\">
<input type=hidden id=\"fin\" name=\"fin\" value=\"$i\">
<div>
<input class=button type=button value=Nuevo onclick=nuevo()>
<input type=\"button\" onclick=\"recarga()\" value=\"Cancelar\">
</div><br>";

$message .= "<div id=\"resultado\"></div>";

if ($search == 0) {
    &box("Error","El archivo $iptables, no esta correctamente configurado, Lea el README del programa.");
    die;
}

print $message;

