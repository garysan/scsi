#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use File::Basename;
my $origen = $0;
use usuarios;

my $usuario = &validate;

shared::header ();
shared::modulo ("Listas de bloqueo");
######### config Area #########
$origen =~ s/\/scsi//g;
$squidconf = $config::squidconf;
######################################
if (!open(SQUIDCONF, "$squidconf"))
{
	&box("Error","El archivo $squidconf no existe.");
	die;
}
$message .= "<div id=alinear><FORM ACTION=\"save.cgi\" METHOD=\"post\">";
$message .= "<table id=\"tabla_bloqueo\" width=300 cellpadding=10>";
$message .= "<tr><th>$config::msg020</th><th>$config::msg021</th><th>$config::msg022</th><th>$config::msg023</th><th>$config::msg024</th>";
$i = 0;
$search = 0;
while (<SQUIDCONF>)
{
	($uno,$dos,$tres,$cuatro,$cinco) = split; #Dividir cada linea
    ##     uno          dos         tres          cuatro               cinco
    ##     acl        denegado    url_regex         -i          "/etc/squid/denegadoslist"
    ##     acl         master       src           /lista/
    ##http_access      allow      clientes 
    ###Orden correcto   valorant, variable, valornue,variable           
 	
 	if ($dos eq "LISTA_RESTRICCIONES" ) { 
		$search = 1; 
	}
	if ($search == 1) { 
		if ($uno eq "acl") {
			$i+=1;
			$cinco =~ s/"//g;
			$message .= "<tr>";
            $message .= "<td>" .$dos. "";
            $message .= "<input type=\"hidden\" name=\"name$i\" value=\"$dos $tres $cuatro\"></td>";
            $message .= "<td>".$cinco."</td><td>";
            $message .= "<input type=\"hidden\" name=\"original$i\" value=$cinco>";
            $message .= "<input name=\"new$i\" value=$cinco></td>";
            $message .= "<td><a href=\"squid_listas.cgi?filename=$cinco\" target=main> Editar</a> </td>";
            $message .= "<td><a href=\"squid_edicion_manual.cgi?params=$cinco,$origen\" target=main> Editar</a></td>";
            $message .= "</tr>\n\n";	
		}
		if ($dos eq "END_LISTA_RESTRICCIONES"){
		    	$search =2;	    
		}
	}
	
};
close (SQUIDCONF);

if ($search == 0) {
    &box("Error","El archivo $squidconf, no esta correctamente configurado, Lea el README del programa.");
    die;
}
print $message;

print <<EOT
</table><br>
<input type="hidden" id="number" name="number" value="$i">
<input type="hidden" id="flag" name="flag" value="$flag">
<div>
<input type="button" onclick="insRow($i)" value="Añadir">
<input type="submit" name="submit" value="Guardar">
<input type="button" onclick="reload()" value="Cancelar">
</div><br>
</FORM>
</BODY></HTML>
EOT
;


