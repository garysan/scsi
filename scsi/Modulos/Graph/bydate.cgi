#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
use Time::Local;

shared::header ();

my $cantidad = 100;
my $logfile = "/var/log/squid/access.log.2";
my $ordenar = "ordenar_consumo";
my $message;
my $starttime;
my $endtime;

my $fecha  = "01/11/2013-00:00";
my $fecha2 = "10/11/2013-20:00";

if (defined $fecha)
{
	$fecha =~ /^(\d+)\/(\d+)\/(\d+)-(\d+):(\d+)$/ or die "-s format looks weird\n";
	my ($startday, $startmonth, $startyear, $starthour, $startminute) = ($1, $2, $3, $4, $5);
	$startmonth--;
	$startyear-=1900;
	$starttime = timelocal(0,$startminute,$starthour,$startday,$startmonth,$startyear);
}
if (defined $fecha2)
{
	$fecha2 =~ /^(\d+)\/(\d+)\/(\d+)-(\d+):(\d+)$/ or die "-e format looks weird\n";
	my ($endday, $endmonth, $endyear, $endhour, $endminute) = ($1, $2, $3, $4, $5);
	$endmonth--;
	$endyear-=1900;
	$endtime = timelocal(0,$endminute,$endhour,$endday,$endmonth,$endyear);
}

shared::perm_log();

open(LOG, "$logfile") or die "No se puede abrir el archivo $logfile! por favor verifique los permisos del archivo...";


$message .= "<div id=alinear>";

my $line;
while (<LOG>)
{
	my ($timestamp, $junk, $ip, $errorcode, $size, $method, $url, $user,
		$routing, $mime_type)
		= split;
	if ($line++ == 0){
		$message .= "Log starts at ".localtime($timestamp)."\n";
	}

	if (defined $starttime && $starttime>0){
		next if $timestamp < $starttime;
	}
	if (defined $endtime && $endtime>0){
		exit if $timestamp > $endtime;
	}

	$message .= "<br />Time:           ".localtime($timestamp)."\n";
	$message .= "<br />IP:             $ip\n";
	$message .= "<br />Error:          $errorcode\n";
	$message .= "<br />Size:           $size Bytes\n";
	$message .= "<br />Method:         $method\n";
	$message .= "<br />URL:            $url\n";
	$message .= "<br />User:           $user\n";
	$message .= "<br />Routing method: $routing\n";
	$message .= "<br />MIME type:      $mime_type\n";
	$message .= "<br />--------------------------------\n";
}

close LOG;
$message .= "</div></body></html>";
print $message;
