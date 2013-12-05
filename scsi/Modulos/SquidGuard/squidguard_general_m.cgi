#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

shared::header ();
$filename = param(filename);
shared::modulo ("Actualmente Editando: $filename");

if ( $filename eq ""){
	&box("No se puede editar archivo", "No pudo pasar a edicion.");
	die;
}

if (   $filename eq $config::squidguard) {

#If the file cannot open, then we create a text box then die.
if (!open(FILE, "$filename"))
{
	&box("notopened",$filename);
	die;
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

<br><br>
<form action="../../Tools/savem.cgi" method="post">
<textarea class="edicion" name=contents rows=25 cols=180>$filecontents</textarea><br><br>
<input type=submit name=submit value="Guardar">
<input type=hidden name=filename value="$filename">

</form></td></tr></table>
</div>
EOT
;

}
else {
	&box("access",$filename); 
}
