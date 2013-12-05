#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

shared::header ();
shared::modulo ("$config::msg001");
print qq(
<div id="centrar" class="justificar">
Al acceder a este servicio, el usuario esta aceptando las politicas y condiciones de uso del sistema<br>
<ul>
<li>El usuario esta capacitado para la correcta utilizacion y el total cumplimiento de las politicas y normas que rigen a la entidad. </li>
<li>Cualquier tipo de acceso a este servicio es monitoreado de tal forma que cualquier intento de uso indebido sea penalizado segun las leyes nacionales y regulaciones internacionales.</li>
<li>Solo se permite el acceso de direcciones IP registradas para IPs nuevas es necesario realizar la solicitud por la via correspondiente.</li>
</ul>
</div>
</body>
</html>
);
