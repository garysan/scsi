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

system ("touch $filename");
system ("echo \"$startip\"> $filename" );
print "
    
    <script>
    \$(function() {
    window.location.href=\"$origen?filename=$filename\";
      target=\"main\";          
  });
  </script>
    ";


