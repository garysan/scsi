#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;
my $usuario = &validate;

shared::header ();
$params = param(params);
($filename,$origen,$startip) = split ",", $params;
#####################################


our $SQUID_CP = 'bin/squid_delete';
our $FLAG=0;
my $ERROR        = '';

if (!-x $SQUID_CP) {
	$SQUID_CP = '';
}
if ($SQUID_CP) {
	$ERROR = `$SQUID_CP 2>&1`;
	$FLAG=1
	if ($ERROR);
	$FLAG=1
	if (!$ERROR);
}
else{
 $FLAG=0;
}

print "$FLAG";
		
		
		
		
		