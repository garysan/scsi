#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

my $usuario = &validate;

my $act = param('original');
my $nue = param('nuevo');
my $flag = param('linea');
#&box($act,$nue);
#&box($nue);
##########Configuration Area##########
$squidconf = $config::squidconf;
######################################
my $val=0;
if ( $config::patchdir ne ""){
    #backup configuracion anterior.
    system ("cp $squidconf /patchdir/scsi-file1");
}

if (!open (OLDFILE, "$squidconf")){
	#&box ("Error:", "$squidconf");
	#die;
	print qq(Content-type: text/html \n\n);
    &msg("<b>Error:, $squidconf</b>");
}
#Carga el archivo al filevar
while (<OLDFILE>){
	$filevar .= $_;
}
close(OLDFILE);

if (!open (NEWFILE, ">$squidconf")){
	#&box ("Error:", "$squidconf");
	#die;
	print qq(Content-type: text/html \n\n);
    &msg("<b>Error:, $squidconf</b>");
}
		$filevar =~ s/$act/$nue/g;
		
		print NEWFILE "$filevar";
close(NEWFILE);

if ( $config::patchdir ne "")
{
	system ("cp $squidconf /patchdir/scsi-file2");
}

if ( $config::patchdir ne "")
{
    $patchdir = $config::patchdir;
	chomp ($date = `date +%d-%m-%H-%M:%S `);
	system ("diff -p /patchdir/scsi-file1 /patchdir/scsi-file2 > $patchdir/$date-access.patch");
	#system ("rm -rf /scsi/scsi-file1 /scsi/scsi-file2 ");
	$val=1;
}
#system "$config::squidbin -k reconfigure";

if ($val eq "1") {
   print qq(Content-type: text/html \n\n);
    &msg("<b>Modificado con exito!</b>");
   
}
