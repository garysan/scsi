#!/usr/bin/perl -X
require '../../../Config/config.pm';            
require '../../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../../Config';
use usuarios;
use Switch;

#my $usuario = &validate;
my $usuario = &validate;
my $cadena;
my $val  = param('flag');
my $user = param('user');

switch ($val) {
	case 0 { 
		my $sth = $dbh->prepare("SELECT adusrusrn,adusrnomb FROM adusr WHERE adusrstat=1") or &dberror;
                $sth->execute() or &dberror;
                while (@data = $sth->fetchrow_array()) {    
                    $cadena= $cadena."<option id='$data[0]'>$data[1]</option>";
                }
                &printmsg($cadena);
	}
        case 2 { 
		my $sth = $dbh->prepare("SELECT adusrusrn,adusrnomb FROM adusr  WHERE adusrstat=9") or &dberror;
                $sth->execute() or &dberror;
                while (@data = $sth->fetchrow_array()) {    
                    $cadena= $cadena."<option id='$data[0]'>$data[1]</option>";
                }
                &printmsg($cadena);
	}
	case 1 {
		$sth = $dbh->prepare("UPDATE adusr set adusrstat=1 WHERE adusrusrn='$user' ");
		$sth->execute()  or &dberror;
                &adlog("El usuario $usuario actualizo el estado del usuario $user a ACTIVO",$usuario);
		&printmsg("Se activo con exito el usuario <b>$user</b>.");
	}
	case 9 {
		$sth = $dbh->prepare("UPDATE adusr set adusrstat=9 WHERE adusrusrn='$user' ");
	        $sth->execute()  or &dberror;
                &adlog("El usuario $usuario actualizo el estado del usuario $user a DESACTIVADO",$usuario);
		&printmsg("Se dio de baja al usuario <b>$user</b>.");
	}
}

