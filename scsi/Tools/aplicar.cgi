#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

my $usuario = &validate;


shared::header ();
shared::modulo ("Aplicar Cambios - Squid");

our $SQUID_WRAPPER = 'bin/squid_executor';
my $ERROR        = '';
print qq(
    <div class="center_screen">
    <br/>
);

if (!-x $SQUID_WRAPPER) {
	$SQUID_WRAPPER = '';
}
if ($SQUID_WRAPPER) {
    $ERROR = `$SQUID_WRAPPER 2>&1`;
	print "$ERROR";
	&box($ERROR) 
	if ($ERROR);
	print "<br><h3 ><center><font color=green >SQUID reconfigurado correctamente!</h3></div>"
	
	if (!$ERROR);
}
else{
    &box("El archivo $SQUID_WRAPPER no existe");
}		
		
		
		
		
		
