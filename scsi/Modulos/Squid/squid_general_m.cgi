#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

shared::header ("","squid.js");
$filename = param(filename);
shared::modulo ("Actualmente Editando: $filename");

if ( $filename eq ""){
	&msg("<b>No se puede editar archivo", "No pudo pasar a edicion.</b>");
	
}

if (   $filename eq $config::squidconf ) {

#If the file cannot open, then we create a text box then die.
if (!open(FILE, "$filename"))
{
	&msg("<b>No se puede abrir,$filename</b>");
} 
# open the css file for reading, then set the varible

while (<FILE>) {
	$filecontents .= $_;
}
close(FILE);
chomp $filecontents;

print <<EOT
<div id="alinear">
<table><tr valign=center><td align=center class="mid">
<FORM id=\"form1m\" name=\"form1m\">
<textarea class="edicion" name=contents rows=25 cols=180>$filecontents</textarea>
<br/>
<input type=submit name=submit value="Guardar">
<input type=hidden name=filename value="$filename">
</form></td></tr></table>
</div>
<div id=\"resultado\"></div>
EOT
;

}
else {
	&msg("<b>Access,$filename</b>"); 
}



