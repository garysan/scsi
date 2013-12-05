#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

$dbh=DBI->connect('DBI:mysql:host=localhost:database=scsi','scsi','scsi') or 
    &vererror("Error en la Base de datos: $DBI::errstr");

$sth=$dbh->prepare("SELECT adusrusrn FROM adusr") or &dberror;
$sth->execute;

if($sth->fetchrow_array)
{
    &mensaje("Enlace Correcto!");
}
else
{   
    &mensaje("Error en el enlace!");    
}
$sth->finish;
$dbh->disconnect;