#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

shared::header();
print qq(
    <div class="menu">
    <br /><br /><br /><br /><br /><br />
    <div align="center"><b>$config::msg000</b></div>
    <ul id="menu">
    <li class="ui-state-focus">Bienvenido</a></li>
    <li><a href="aviso.cgi" target=main>$config::msg001</a></li>
);

    ############Cargar modulos desde la base de datos
    if ( &valadmin("$usuario") ne "") {
    
    my $sth = $dbh->prepare("SELECT * FROM scmod WHERE scmodstat=0 ") or &dberror;
    $sth->execute() or &dberror;

    while (@data = $sth->fetchrow_array()) {
    print qq(\t<li class="ui-state-focus">$data[1]</li>\n);
        my $sth_submenu = $dbh->prepare("SELECT * FROM scmdt WHERE scmdtstat=0 AND scmdtnmod=$data[0]") or &dberror;
        $sth_submenu->execute() or &dberror;
        while (@submenu = $sth_submenu->fetchrow_array()) {    
        print qq(\t<li>\n\t<a href="/$submenu[3]" target=main >$submenu[2]</a>\n\t</li>\n);
        }
    }
    
  }####Fin IF de Admin
  
  #############Herramientas Generales##################
  print qq(
    <li class="ui-state-focus">$config::msg007</li>
    <li><a href="../../Tools/testdb.cgi" target=main>Verificar BD</a></li>
    <li><a href="../../Tools/check.cgi" target=main>Verificar Permisos</a></li>
    <li><a href="../Admin/CambiarClave/" target=main >Cambiar Clave</a></li>
    <li><a href="javascript:logout()">Salir</a>   
    </ul>
    </div>
  );


