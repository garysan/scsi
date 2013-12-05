#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$year += 1900;
$mon++;

my $date= "$mday/$mon/$year";

shared::header ("Encabezado");

print qq(
    <div class="div_header">
    <div align="center" class="div_iz">
        <h2 class="nombre_programa"> $config::progname</h2>
    </div>
    <div class="div_der">
        <h3 class="usuario_logeado"> Bienvenido <b>$usuario - Fecha: $date</b>  </h3>
    </div>
    </div>
</body>
</html>
);
