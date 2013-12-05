#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use File::Basename;
use usuarios;

my $usuario = &validate;

my $act = param('original');
my $nue = param('nuevo');
my $arch = param('arch');
my $file = basename($arch);
#&box($arch,"$act,$nue");
##########Configuration Area##########
my $val=0;
if ( $config::patchdir ne ""){
    #backup configuracion anterior.
    system ("cp $arch /patchdir/$arch1");
}

if (!open (OLDFILE, "$arch")){
	print qq(Content-type: text/html \n\n);
	&msg("Error en OLDFILE, $arch");
	#&box("Error OldFile",$arch);

}
#Carga el archivo al filevar
while (<OLDFILE>){
	$filevar .= $_;
}
close(OLDFILE);

if (!open (NEWFILE, ">$arch")){
	print qq(Content-type: text/html \n\n);
	&msg("Error en NEWFILE, $arch");
	#&box("Error Newfile",$arch);
}
		$filevar =~ s/$act/$nue/g;
		
		print NEWFILE "$filevar";
close(NEWFILE);

if ( $config::patchdir ne "")
{
	system ("cp $arch /patchdir/$arch2");
}

if ( $config::patchdir ne "")
{
    $patchdir = $config::patchdir;
	chomp ($date = `date +%d-%m-%H-%M:%S `);
	system ("diff -p /patchdir/$arch1 /patchdir/$arch2 > $patchdir/$date-$file.patch");
	#system ("rm -rf /patchdir/$arch1 /patchdir/$arch2 ");
	$val=1;
}
system "$config::squidbin -k reconfigure";

if ($val eq "1") {
   print qq(Content-type: text/html \n\n);
    &msg("<b>Modificado con exito!</b>");
   
}
