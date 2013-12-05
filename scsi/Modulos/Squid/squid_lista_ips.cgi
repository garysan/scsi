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

shared::header ("","squid.js");
shared::modulo ("Listas de direcciones IP");
######### config Area #########
$origen =~ s/\/scsi//g;
$squidconf = $config::squidconf;
######################################
if (!open(SQUIDCONF, "$squidconf")){
	&box("Error","El archivo $squidconf no existe.");
	die;
}
$message .= "<div id=alinear>";
#<FORM ACTION=\"../../Tools/save.cgi\" METHOD=\"post\">
$message .= "<FORM action=\"../../Tools/save.cgi\" id=\"form1\" name=\"form1\">";
$message .= "<table id=\"tabla_lista\" width=300 cellpadding=10>";
$message .=  "<tr><th>$config::msg020</th><th>$config::msg021</th><th>$config::msg022</th><th>$config::msg023</th><th>$config::msg024</th>";
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
 	
 	if ($dos eq "LISTA_IPS" ) { 
		$search = 1; 
	}
	if ($search == 1) { 
		if ($uno eq "acl") {
			$i+=1;
			$cuatro =~ s/"//g;
			$message .= "<tr>";
            $message .= "<td>" .$dos . "";            
            $message .= "<input type=\"hidden\" name=\"name$i\" value=\"$dos $tres\"></td>";
            $message .= "<td>$cuatro</td><td>";
            $message .= "<input type=\"hidden\" name=\"original$i\" value=$cuatro>";
            $message .= "<input name=\"new$i\" value=$cuatro></td>";
            $message .= "<td><a href=\"squid_listas.cgi?filename=$cuatro\" target=main> Editar</a> </td>";
            $message .= "<td><a href=\"squid_edicion_manual.cgi?params=$cuatro,$origen\" target=main> Editar</a></td>";    
            $message .= "</tr>";
		}
		if ($dos eq "END_LISTA_IPS"){
		    	$search =2;
		}
	}
};
close (SQUIDCONF);

if ($search == 0) {
    #&box("Error","El archivo $squidconf, no esta correctamente configurado, Lea el README del programa.");
    #die;
    print qq(Content-type: text/html \n\n);
     &msg("<b>El archivo $squidconf, no esta correctamente configurado, Lea el README del programa.</b>");
}

$message.="</table><br>
<input type=hidden id=\"archivo\" name=\"archivo\" value=\"$origen\">
<input type=hidden id=\"number\" name=\"number\" value=\"$i\">
<input type=hidden id=\"flag\" name=\"flag\" value=\"$flag\">
<div>
<input type=\"button\" onclick=\"insRowL($i)\" value=\"Añadir\">
<input type=submit value=\"Guardar\">
<input type=\"button\" onclick=\"location.reload()\" value=\"Cancelar\">
</div>
</FORM>
<br/>
<div id=\"resultado\"></div>
</BODY></HTML>";

print $message;


