#!/usr/bin/perl -X
require '../../../Config/config.pm';            
require '../../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../../Config';
use usuarios;

my $usuario = &validate;

my $dbh = DBI->connect( "dbi:mysql:scsi", "scsi", "scsi") or 
    &dberror("Error en la Base de datos: $DBI::errstr");
    
my $username = $usuario;
my $email="";
my $cant = param('ant');
my $cnue = param('nueva');
my $ccla = param('cnueva');

my $sth = $dbh->prepare("SELECT adusrmail FROM adusr WHERE adusrusrn='$usuario' AND adusrclav=MD5('$cant') ") or &dberror;
#$sth->trace( 3, '/tmp/rp.txt' );
$sth->execute;

if($email = $sth->fetchrow_array){
		###Procesar
		# Almacenar en la base de datos
        $sth = $dbh->prepare("UPDATE adusr SET adusrclav=MD5(?) WHERE adusrusrn=?")  or &dberror;
        #$sth->trace( 3, '/tmp/fg.txt' );
        $sth->execute($cnue, $username) or &dberror;
        &adlog("El usuario $user cambio la clave de acceso.",$user);
        # Enviar el correo con el password sin encriptar
        $ENV{PATH} = "/usr/sbin";
        open(MAIL,"|/usr/sbin/sendmail -t -oi");
        print MAIL "To: $email\n";
        print MAIL "From: scsiadmin\n";
        print MAIL "Subject: Nueva clave en SCSI\n\n";
print MAIL <<EndMail;

Su clave dentro el sistema SCSI ahora es:

'$cnue'

Puede probar su nueva clave en: 
http://$config::ipsystem/


Recuerde que no debe realizar el 
EndMail

    print qq(Content-type: text/html \n\n);
    &msg("Su clave fue cambiada con exito! <script type=\"text/javascript\">limpiar_formulario()</script>");
}

else{
    print qq(Content-type: text/html \n\n);
    &msg("El Password anterior no corresponde <script type=\"text/javascript\">limpiar_formulario()</script>");
}



