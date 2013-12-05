#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
my $usuario = &validate;

print header;
print start_html("Panel Principal");

print qq(
<h2>Segura!</h2>
Bla! <b>$usuario</b>. <a href="logout.cgi">Cerrar sesion</a><br>
);

print end_html;