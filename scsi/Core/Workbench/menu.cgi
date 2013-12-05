#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

shared::header_menu();

print qq(
<div align="center" class="titulo_menu" ><b>$config::msg000</b></div>    

<link rel="stylesheet" type="text/css" 
      href="../../css/menu.css" />
    
    <div id="accordian">
    <ul>
	<li class="active">
            <h3>Bienvenido</h3>
            <ul>
            <li><a href="aviso.cgi" target=main>$config::msg001</a></li>
            </ul>
        </li>


);

    ############Cargar modulos desde la base de datos
    if ( &valadmin("$usuario") ne "") {
    
    my $sth = $dbh->prepare("SELECT * FROM scmod WHERE scmodstat=0 ") or &dberror;
    $sth->execute() or &dberror;

    while (@data = $sth->fetchrow_array()) {
    print qq(\t<h3>$data[1]</h3><ul>\n);
        my $sth_submenu = $dbh->prepare("SELECT * FROM scmdt WHERE scmdtstat=0 AND scmdtnmod=$data[0]") or &dberror;
        $sth_submenu->execute() or &dberror;
        while (@submenu = $sth_submenu->fetchrow_array()) {    
        print qq(\t<li>\n\t<a href="/$submenu[3]" target=main >$submenu[2]</a>\n\t</li>\n);
        }
    print qq(\t</ul>\n);
    }
    
  }####Fin IF de Admin
  
  #############Herramientas Generales##################
  print qq(
    
    <h3>$config::msg007</h3>
    <ul>    
    <li><a href="../../Tools/testdb.cgi" target=main>Verificar BD</a></li>
    <li><a href="../../Tools/check.cgi" target=main>Verificar Permisos</a></li>
    <li><a href="../Admin/CambiarClave/" target=main >Cambiar Clave</a></li>
    <li><a href="javascript:logout()">Salir</a>   
    </ul>
    </ul>
    </div>
  );




