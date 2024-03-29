#!/usr/bin/perl -X
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser); 
use DBI;
use Email::Valid;
use lib '../../../Config';
use usuarios;
use warnings;

my $username = param('usuario');
my $email = param('correo');

unless (Email::Valid->address($email)) {
    print qq(Content-type: text/html \n\n);
    &msg("El correo electronico <b>$email</b> no es valido.
    <script type=\"text/javascript\">limpiar_formulario()</script>
    ");
}

my $sth = $dbh->prepare("SELECT * FROM adusr WHERE adusrmail=? AND adusrusrn=? ");

$sth->execute($email,$username) or &dberror;

if (my $uinfo = $sth->fetchrow_hashref) {
  
    my $randpass = &random_password();
    my $encpass = &encrypt($randpass);
    $sth = $dbh->prepare("UPDATE adusr SET adusrclav=MD5(?) WHERE adusrusrn=?")  or &dberror;
    $sth->execute($encpass, $username) or &dberror;
    $ENV{PATH} = "/usr/sbin";
    open(MAIL,"|/usr/sbin/sendmail -t -oi");
    print MAIL "To: $email\n";
    print MAIL "From: scsiadmin\n";
    print MAIL "Subject: Nueva clave en SCSI\n\n";
print MAIL <<EndMail;

Su clave dentro el sistema SCSI ahora es:

'$encpass'

Puede probar su nueva clave en: 
http://$config::ipsystem/

Recuerde que no debe realizar el 
EndMail
    &adlog("Se envió una nueva clave a $username con cuenta de email $email",$username);
    print qq(Content-type: text/html \n\n);
    &msg("Su nueva clave fue enviada al correo electronico: <b>$email</b>
    <script type=\"text/javascript\">limpiar_formulario()</script>");
      
  
} else {
    &adlog("Datos para recuperar clave erroneos usuario $username correo $email",'');
    print qq(Content-type: text/html \n\n);
    &msg("Datos invalidos, Verifique por favor.
    <script type=\"text/javascript\">limpiar_formulario()</script>");
}