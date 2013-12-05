#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

##########Configuration Area##########
$masterconf = $configuration::master;
$patchdir = $configuration::patchdir;
######################################

if ( $patchdir ne "")
{
system ("cp $masterconf /scsi/scsi-file1");
}
$i = param("number");
if (!open (OLDFILE, "$masterconf")){
	shared::htmlbox ("notopened", "$masterconf");
	die;
}

while (<OLDFILE>)
{
	$filevar .= $_;
}
close(OLDFILE);
if (!open (NEWFILE, ">$masterconf")){
	shared::htmlbox ("notopened", "$masterconf");
	die;
}

$n=0;
while ($n != $i) {
	$number=$n+1;
	@name[$n] = param("name$number");
	@original[$n] = param("original$number");
	@new[$n] = param("new$number");
	$n+=1;
}

print "Content-type: text/html\n\n";
print "<HTML><HEAD><TITLE>Archivo Modificado</TITLE>";
shared::css ();
print "</HEAD>\n<BODY>";

$n=0;
while ($n != $i) {
	$filevar =~ s/@original[$n] @name[$n]/@new[$n] @name[$n]/g;
	$n+=1;
}

print NEWFILE "$filevar";
close(NEWFILE);
if ( $patchdir ne "")
{
	system ("cp $masterconf /scsi/scsi-file2");
}
print "<table width=100% height=100%>";
print "<tr valign=middle><td align=center>";
print "<table class=\"mid\"><tr valign=middle><td align=center class=\"mid\">";

print "El archivo fue grabado correctamente!\n";

print "</td></tr></table>";
print "</td></tr></table>";
print "</BODY>\n</HTML>";
if ( $patchdir ne "")
{
	chomp ($date = `date +%d-%m-%H-%M:%S `);
	system ("diff -p /scsi/scsi-file1 /scsi/scsi-file2 > $patchdir/$date-access.patch");
	system ("rm -rf /scsi/scsi-file1 /scsi/scsi-file2 ");
}
#system "$configuration::squidbin -k reconfigure";
