#!/usr/bin/perl -X
require '../../../Config/config.pm';            
require '../../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../../Config';
use usuarios;
use Switch;

my $usuario = &validate;
my $cadena;
my $val  = param('flag');
my $nmod = param('nmod');
my $nomb = param('nomb');
my $ruta = param('ruta');
my $desc = param('desc');
my $nmdt = param('item');

switch ($val) {
	case 0 { 
		my $sth = $dbh->prepare("SELECT scmodnmod,scmoddesc FROM scmod ") or &dberror;
                $sth->execute() or &dberror;
                while (@data = $sth->fetchrow_array()) {    
                    $cadena= $cadena."<option id='$data[0]'>$data[1]</option>";
                }
                &printmsg($cadena);
	}
	case 1 {
		my $sth = $dbh->prepare("SELECT scmdtcorr, scmdtdesc FROM scmdt WHERE scmdtnmod='$nmod' AND scmdtstat=0   ") or &dberror;
                $sth->execute() or &dberror;
                while (@data = $sth->fetchrow_array()) {    
                    $cadena= $cadena."<option id='$data[0]'>$data[1]</option>";
                }
                &printmsg($cadena);
	}
	case 2 {
		$sth = $dbh->prepare("INSERT INTO scmod (scmodnmod,scmoddesc,scmodstat)
                                      SELECT(IFNULL((SELECT MAX(scmodnmod)+1 FROM scmod), 1)),'$desc',0");
		$sth->execute()  or &dberror;
		&adlog("El usurio $usuario inserto el modulo $desc",$usuario);
                &printmsg("Modulo <b>$desc</b> fue registrado con exito!");
	}
	case 3 {
		my $consulta = "INSERT INTO scmdt (scmdtcorr,scmdtnmod,scmdtdesc,scmdtruta,scmdtstat)
		                SELECT(IFNULL((SELECT MAX(scmdtcorr)+1 FROM scmdt 
                                WHERE scmdtnmod='$nmod'), 1)),
				'$nmod','$desc','$ruta',0 ";
		$sth = $dbh->prepare($consulta);
		$sth->execute()  or &dberror;
		&adlog("El usurio $usuario inserto el item $desc en el modulo $nmod con la ruta $ruta",$usuario);
                &printmsg("Item <b>$desc</b> registrado con exito!");
	}
	case 4 {
		my $consulta = "SELECT scmdtruta FROM scmdt WHERE scmdtnmod='$nmod' AND scmdtcorr='$nmdt' AND scmdtstat=0 ";
		my $sth = $dbh->prepare($consulta) or &dberror;
		$sth->execute() or &dberror;
    		while (@data = $sth->fetchrow_array()) {    
          		$cadena= $cadena."$data[0]";
    		}
    		&printmsg($cadena);
	}		
	case 8 {
		$sth = $dbh->prepare("UPDATE scmdt set scmdtruta='$ruta' WHERE scmdtnmod='$nmod' AND scmdtcorr='$nmdt' ");
		$sth->execute()  or &dberror;
                &adlog("El usurio $usuario actualizo el item $nmdt a la ruta $ruta en el modulo $nmod",$usuario);
		&printmsg("Actualizado con exito!");
	}
	case 9 {
		$sth = $dbh->prepare("UPDATE scmdt set scmdtstat=9 WHERE scmdtnmod='$nmod' AND scmdtcorr='$nmdt' ");
	        $sth->execute()  or &dberror;
                &adlog("El usurio $usuario dio de baja el item $nmdt en el modulo $nmod",$usuario);
		&printmsg("Se dio de baja con exito!");
	}
}

