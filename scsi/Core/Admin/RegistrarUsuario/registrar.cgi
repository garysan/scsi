#!/usr/bin/perl -X
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Email::Valid;
use DBI;
use lib '../../../Config';
use usuarios;
use warnings;

my $sth = $dbh->prepare("SELECT * FROM adusr ") or &dberror;
$sth->execute;
if (my $rec = $sth->fetchrow_hashref) {
    my $usuario = &validate;    
}

#print header;
#print start_html("Resultado del registro");
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
    &dberror("Imposible conectar a la BD:\n $DBI::errstr");

my $username = param('usuario');
my $realname = param('nombre');
my $email    = param('email');
my $rol      = param('rol');
my $password = param('password');
my $rolvalue;
my $rolname;

my $fechatoday=("$longyr/$fixmo/$mday");
my $horatoday =(" $hr:$min:$sec ");

# Set rol value
if ("$rol" eq "")
{
    $rolvalue=0;
}
else
{
    if("$rol" eq "admin")
    {
        $rolvalue=1;
        $rolname="Administrador";
    }
    else
    {
        if("$rol" eq "super")
        {
            $rolvalue=2;
            $rolname="Supervisor";            
        }
    }
}

my $sth = $dbh->prepare("SELECT * FROM adusr WHERE adusrusrn = ?") or &dberror;
$sth->execute($username) or &dberror;
if (my $rec = $sth->fetchrow_hashref) {
   print qq(Content-type: text/html \n\n);  
   &msg("El usuario <b>$username</b> ya se encuentra en uso.");
}

$insert = "
	insert into adusr 
	values(
	'$username',
	'$realname',
	'$email',
	'$rolvalue',
	MD5('$password'),
	'1',
	'gsandi',
	'$horatoday',
	'$fechatoday',
	'',
	'',
	'$fechatoday',
	'0')";
$sth = $dbh->prepare($insert)  or 
	&dberror;
$sth->execute  or &dberror;

# Enviar el correo con el password sin encriptar
$ENV{PATH} = "/usr/sbin";
open(MAIL,"|/usr/sbin/sendmail -t -oi");
print MAIL "To: $email\n";
print MAIL "From: scsiadmin\n";
print MAIL "Subject: Registro de $rolname - SCSI\n\n";
print MAIL <<EndMail;

Bienvenido $realname.
SCSI le comunica que se procedio con la creacion de su cuenta con los siguientes datos.

Nombre de Usuario:
$username 

Rol de acceso:
$rolname 

Clave de Acceso:
'$password'

Para ingresar ingrese a: 
http://$config::ipsystem/

EndMail
print qq(Content-type: text/html \n\n);
&msg("El usuario <b>$username</b> se registro con exito!
<script type=\"text/javascript\">limpiar_registro()</script>");
#print qq(<script type="text/javascript">limpiar_registro()</script>);
#my $url="http://$config::ipsystem";
#my $t=2; 
#print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$url\">\n";

