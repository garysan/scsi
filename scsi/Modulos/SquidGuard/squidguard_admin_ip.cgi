#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
use File::Basename;

my $usuario = &validate;

shared::header ("","squidguard.js");

shared::modulo ("Administrar lista, Administradores");
######### config Area #########
if ($config::squidver eq "2"){
    $squidguard  = $config::sgbf;
}
if ($config::squidver eq "3"){
    $squidguard = $config::sgbf3;
}
$filename = $squidguard;

######################################
if (!open(SQUIDGUARD, "$squidguard"))
{
	&box("Error","El archivo $squidguard no existe.");
	die;
}
$message .= "<div id=alinear>";
$message .= "<table id=\"tabla_general\">";
#$message .=  "<tr><th>Variable</th><th>Estado Actual</th><th>Cambiar Estado</th>";
$search = 0;

while (my $line=<SQUIDGUARD>)
{
	$search=1;
	my @valores=split(' ',$line);
	if ($search == 1) {
            #$message .= "<input name=\"name$i\" value=\"$valores[0]\"></td><td align=right>";
            #$message .= "<input name=\"original$i\" value=\"$valores[1]\">";
		if ($valores[0]eq "ip"){
			$i+=1;
			$message .= "<tr>";
			$message .= "<td><b>" .$i. ":</b></td>";
            $message .= "<td><input id=\"new$i\" value=\"$valores[1]\" name=\"new$i\"></td>";
            $message .= "<td><input class=button type=button value=Quitar onclick=\"quitar('$valores[1]')\"></td>";
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
  $message .="<div id=\"dialog-form\" title=\"Valor\">
						  <form>
						  <fieldset>
						    <label for=\"valor\">Valor</label>
						    <input type=\"text\" name=\"valor\" id=\"valor\" class=\"text ui-widget-content ui-corner-all\" />
						  </fieldset>
						  </form>
						</div>";


if ($search == 0) {
    &box("Error","El archivo $squidguard, no esta correctamente configurado, Lea el README del programa.");
    die;
}

print $message;

