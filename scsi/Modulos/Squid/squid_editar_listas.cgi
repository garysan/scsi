#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
use File::Basename;


my $usuario = &validate;
shared::header ();
$params = param(params);
($filename,$origen) = split ",", $params;

shared::modulo ("Actualmente Editando: $filename");

if ( $filename eq ""){
    &box("No se puede editar archivo", "No pudo pasar a edicion.");
    die;
}

if ($filename ne "") {
    if (!open(FILE, "$filename")){
        &newfile("Archivo Inexistente","El archivo \"$filename\" no existe, desea crearlo?",$filename,$origen);
        die;
    } 
    
    while (<FILE>) {
        $filecontents .= $_;
    }
    close(FILE);
    chomp $filecontents;
    
print <<EOT
<center>
<table id="centrar"><tr valign=center><td align=center class="mid">
<br><br>
<form action="../../Tools/savem.cgi" method="post">
<textarea class="edicion" name=contents rows=25 cols=180>$filecontents</textarea><br><br>
<input type=submit name=submit value="Guardar">
<input type=hidden name=filename value="$filename">
</form></td></tr></table>
</center>
EOT
;
}
else {
    &box("access",$filename);
}