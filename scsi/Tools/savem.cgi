#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;


my $usuario = &validate;

shared::header ();
$filename = param(filename);
##########Configuration Area##########
$filename = param("filename");
$contents = param("contents");
#####################################

if ( $config::patchdir ne ""){
system ("rm /patchdir/scsi-file1 /scsi/scsi-file2");
system ("cp $filename /patchdir/scsi-file1");
}

if ($filename) {

if (!open(FILE, ">$filename")) { 
	&msg("<b>El archivo no se pudo abrir!</b>");
}
$contents .= "\n";
print FILE $contents;
close(FILE);
if ( $config::patchdir ne ""){
	$patchdir = $config::patchdir;
	chomp ($date = `date +%d-%m-%H-%M:%S `);
	system ("cp $filename /patchdir/scsi-file2");
	if ( $filename eq $config::squidconf ){
		system ("diff -p /patchdir/scsi-file1 /patchdir/scsi-file2 > $patchdir/$date-accessm.patch");
		system ("rm -rf /patchdir/scsi-file1 /patchdir/scsi-file2");
	}else{
        	system ("diff -p /patchdir/scsi-file1 /patchdir/scsi-file2 > $patchdir/$date-accessm-sgbf.patch");
		system ("rm -rf /patchdir/scsi-file1 /patchdir/scsi-file2");
	}
}

 print qq(Content-type: text/html \n\n);
     our $BINARY = '../../Tools/bin/squid_executor';
     my $ERROR        = '';
     if (!-x $BINARY) {
             $BINARY = '';
     }
     if ($BINARY) {
        $ERROR = `$BINARY 2>&1`;
        &msg($ERROR)
        if ($ERROR);
        &msg("<b>Modificado y aplicado con exito!</b>") 
        if (!$ERROR);
     }
     else{
         &msg("El archivo $BINARY no existe");
     }		
}

else {
   &msg("<b>Archivo no existente!</b>"); 
}
