#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

######### Configuration Area #########
$masterconf = $configuration::master;
######################################
#If opening the squid config file fails to open, then show an error box and die.
if (!open(MASTERCONF, "$masterconf"))
{
	shared::htmlbox("notopened",$masterconf);
	die;
}
#The whole idea behind $message1 and $message, is that the page will not behave badly if it errors. Before when we did not have thsi procedure, it would do all the html code twice, once here, and if openeing the file failed, then shared::css() would do it all again. As we do not want this, I created these two varibles, $message1 ends just befoe the <style> block, and $message starts after the </style>. We need to do this because I cannot figure out howto set the outcome of shared::css to gointo a varible, and it is easier this way.
$message1 = "Content-type: text/html\n\n";
$message1 .= "<HTML><HEAD><TITLE>Configuracion principal</TITLE>";
$message .= "</HEAD><BODY><div align=center><FORM ACTION=\"testsave.cgi\" METHOD=\"post\"><FONT class=\"title\">Parametros de SQUID segun $configuration::progabre</FONT><br><br>";
$message .= "<table class=\"mid\" width=500 cellpadding=10>";
$i = 0;
##Making boxes that you click on to allow and deny.
$search = 0; #Varible to ensure that ### IAC_START ### Is included somewhere in the config file.

while (<MASTERCONF>)
{
	$search = 1;
        chomp;

        if(/^\s*$/)
            {
            $vfiler = 0;
            }
        if(/vfiler0/)
            {
            $vfiler = 1;
            }
        if (!$vfiler && m/([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})/)
            {
            my $ip=$1;
            $i+=1;
            $message .=  "<tr><td>Direcci�n IP " .$i.": ";
            $message .= "<input name=\"original$ip\" value=\"$ip\">\n";
            $message .= "<br></td></tr>\n\n";
            }
};

close (MASTERCONF); #close unwanted file, as we do not like to use more ram on the server than needed.
# Need to check if we actually printed any check boxes, and if not, we will suggest to them to read the manual.

if ($search == 0) {
shared::htmlbox ( "$masterconf", "El archivo no existe.");
die;
}
print $message1; #read my paragraph on these two varibles (message1 and message).
shared::css ();
print $message;
#finnish off all the html.
print <<EOT
</table><br>
<input type=hidden name="number" value="$i">
<table class="mid" width=300><tr align=center><td>
<input type=submit name="submit" value="Guardar"><br>
<a href="accessm.cgi?filename=$masterconf">Editar Manualmente</a>
</td></tr></table><br>
</FONT></FORM>
</BODY></HTML>
EOT
;
