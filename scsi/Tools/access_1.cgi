#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

my $usuario = &validate;

shared::header ();
shared::modulo ("$config::msg002");

######### Configuration Area #########
$squidconf = $config::squidconf;
######################################
#If opening the squid config file fails to open, then show an error box and die.
if (!open(SQUIDCONF, "$squidconf"))
{
    &box($squidconf);
    die;
}
#The whole idea behind $message1 and $message, is that the page will not behave badly if it errors. Before when we did not have thsi procedure, it would do all the html code twice, once here, and if openeing the file failed, then shared::css() would do it all again. As we do not want this, I created these two varibles, $message1 ends just befoe the <style> block, and $message starts after the </style>. We need to do this because I cannot figure out howto set the outcome of shared::css to gointo a varible, and it is easier this way.
$message1 = "Content-type: text/html\n\n";
$message1 .= "<HTML><HEAD><TITLE>Config File Changer</TITLE>";
$message .= "</HEAD><BODY><div align=center><FORM ACTION=\"save.cgi\" METHOD=\"post\"><FONT class=\"title\">Internet Access Control</FONT><br><br>";
$message .= "<table class=\"mid\" width=300 cellpadding=10>";
$i = 0;
##Making boxes that you click on to allow and deny.
$search = 0; #Varible to ensure that ### IAC_START ### Is included somewhere in the config file.
while (<SQUIDCONF>)
{
    ($type,$access,$name) = split; #Set varibles $type, $access and $name to thevalues of the lines of the config file.
    if ($access eq "SIAC_START" || $access eq "IAC_START") { 
        $search = 1; 
    }
#If the $search varible equals 1, then enable searching for allow deny varibles from now on. 
#$access is the second varible on the line.
    if ($search == 1) { #check if we are allowed to continue looking for varibles.
        if ($type eq "http_access") { #if the first varible type is http_access, then procede.
            $i+=1;
            $message .=  "<tr><td>" .$name . " ";
            $message .= "<input  name=\"name$i\" value=\"$name\"></td><td align=right>\n";
            $message .= "<input  name=\"original$i\" value=\"$access\">\n";
            $message .=  "<select name=\"new$i\">";
            $option1 = "<option value=\"allow\">Allow</option>";
            $option2 = "<option value=\"deny\">Deny</option>";
            if ($access eq "allow"){
                $message .=  $option1 . "<br>\n";
                $message .= $option2 . "<br>\n";
            } else {
                $message .=  $option2 . "<br>\n";
                $message .=  $option1 . "<br>\n";
            }
            $message .=  "</select>";
            $message .= "<br></td></tr>\n\n";
        }
    }
};

close (SQUIDCONF); #close unwanted file, as we do not like to use more ram on the server than needed.
# Need to check if we actually printed any check boxes, and if not, we will suggest to them to read the manual.
if ($search == 0) {
&box( "Setup $squidconf", "You have not setup your squid config file for SIAC properly, you need to insert \"### SIAC_START ###\" without the double quotes before the http_access allow/deny area you want to be able to edit.");
die;
}
print $message1; #read my paragraph on these two varibles (message1 and message).

print $message;
#finnish off all the html.
print <<EOT
</table><br>
<input type=hidden name="number" value="$i">
<table class="mid" width=300><tr align=center><td>
<input type=submit name="submit" value="Save"><br>
<a href="accessm.cgi?filename=$squidconf">Manually Edit File</a>
</td></tr></table><br>
</FONT></FORM>
</BODY></HTML>
EOT
;
