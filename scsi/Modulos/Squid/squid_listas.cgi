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
$filename = param(filename);
shared::modulo ("Actualmente Editando: $filename");

if ( $filename eq ""){
    &msg("<b>No pudo pasar a edicion.</b>");
    
}

if (!open(FILENAME, "$filename"))
{
	&msg("<b>El archivo $filename no existe, Intente acceder al archivo de forma manual</b>");
}
$i = 0;
$search = 0;
#$message .= "<div id=alinear>";
$message .= "<table id=\"listas\">";

while (my $line=<FILENAME>)
{
	$search=1;
	#($uno,$dos,$tres,$cuatro) = split ".",$line; #Dividir cada linea
	if ($search == 1) { 
            $i+=1;
            $message .= "<tr><td>" .$i . ":</td>";
            $message .= "<input id=\"original$i\" type=hidden name=\"original$i\" value=\"$line\">";
            $message .= "<td><input id=\"new$i\" value=\"$line\" name=\"new$i\"></td>";
            $message .= "<td><input class=button type=button value=Activar onclick=\"activar($i)\">";
            $message .= "<input class=button type=button value=Desactivar onclick=\"desactivar($i)\">";
            $message .= "<input class=button type=button value=Modificar onclick=\"modificar($i)\"></td>";
	}
	
};####While!

$message .= "</table><br>
<input type=hidden id=\"archivo\" name=\"archivo\" value=\"$filename\">
<input type=hidden id=\"number\" name=\"number\" value=\"$i\">
<input type=hidden id=\"flag\" name=\"flag\" value=\"$flag\">
<div>
<input type=\"button\" onclick=\"insRow($i)\" value=\"Añadir\">
<input type=\"button\" onclick=\"recarga()\" value=\"Cancelar\">
</div><br>";

$message .= "<div id=\"resultado\"></div>";
	
if ($search == 0) {
    &msg("<b>El archivo $filename, no esta correctamente configurado, Lea el README del programa.</b>");
}
print $message;

