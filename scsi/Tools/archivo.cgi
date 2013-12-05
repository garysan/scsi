#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

my $usuario = &validate;

print header;
print start_html("Resultado del registro");
##############Para obtener la Hora
my @days = qw(Sunday Monday Tuesday Wednesday Thursday Friday Saturday);
my @shortdays = qw( Sun Mon Tue Wed Thu Fri Sat );
my @months = qw(January February March April May June July August September October November December);
my @shortmonths = qw( Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);

my ( $sec, $min, $hr, $mday, $mon, $year, $wday, $yday, $isdst ) =  localtime(time);
my $longyr = $year + 1900;
my $fixmo  = $mon + 1;

my $tz = $isdst == 1 ? "CDT" : "CST";
my $yr2 = substr( $longyr, 2, 2 );
##############Fin de la Hora.
our $dbh = DBI->connect( "dbi:mysql:scsi", "scsi", "scsi") or 
    &vererror("Imposible conectar a la BD:\n $DBI::errstr");

my $nmod = param('nmod');
my $desc = param('desc');
my $arch = param('arch');

my $statvalue;

my $fechatoday=("$longyr/$fixmo/$mday");
my $horatoday =(" $hr:$min:$sec ");

# Verificar Campos
if ($nmod eq "") {
    &vererror("Este campo no puede estar vacio.");   
}

if ($arch eq "") {
    &vererror("Este campo no puede estar vacio.");
}

if ($desc eq "") {
    &vererror("Este campo no puede estar vacio.");
}

$sth = $dbh->prepare("
	insert into archi
	values(
	'$nmod',
	'$arch',
	'$desc',
	'gsandi',
	'$fechatoday',
	'$fechatoday',
	'$horatoday',
	'0')")  or 
	&dberror;
	
#$sth->trace( 3, '/tmp/al.txt' );
$sth->execute  or &dberror;
print qq(<h2>Registrado!</h2>);
my $url="../modulos/archivo.html";
my $t=2; 
print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$url\">\n";

