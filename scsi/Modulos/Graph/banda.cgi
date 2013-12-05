#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
shared::header ("Consumo de Megas","byip.js");

my $cantidad = 100;
my $logFile = "/var/log/squid/access.log";
my $ordenar = "ordenar_consumo";

my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$year += 1900;
$mon++;

my $fecha= "$mday/$mon/$year";
my $hora= "$hour:$min:$sec";

my $row;
my($epoch_time_miliseconds, $unknown_integer1, $ip, $tcp_and_http_code);
my($unknown_integer2, $http_method, $url, $minus, $squid_method_site_url, $content_type);
my($ip, %sitios);


shared::perm_log();

$message .= "<div id=alinear>";
$message .= "<table width='100%' ><tr><td>";
$message .= "<h1>Consumo por IP</h1>";
$message .= "<p>Reporte generado en fecha $fecha a horas $hora</p>";
$message .= "<table>";
$message .= "<tr><td><b>Consumo</b></td><td><b>IP</b></td></tr>";
open(LOG, "$logFile") or die "No se puede abrir el archivo $logFile! por favor verifique los permisos del archivo...";
while(<LOG>){
	$row = $_;
	($epoch_time_miliseconds, $unknown_integer1, $ip, $tcp_and_http_code, $unknown_integer2, $http_method, $url, $minus, $squid_method_site_url, $content_type) = split(/\s+/, $row);
       	$url =~ s/http:\/\///;
        $url =~ s/https:\/\///;
	$url =~ s/ftp:\/\///;
	$url =~ s/www.//;
	$url =~ s/\/$//;
	if (!$url ){
            next;
	}        
        ($ip) = ($ip =~ m{ ([0-9.\-:]+)}x );
	if (!$sitios{$ip}->{size})	{
		$sitios{$ip}->{size} = 0;
	}
	$sitios{$ip}->{size} = $sitios{$ip}->{size} + $unknown_integer2;
}

foreach $ip ( sort ($ordenar keys (%sitios) ) )
{
	if ($cantidad > 0)
	{
                $message .="<tr>";
		$message .="<td>".get_size($sitios{$ip}->{size}) ."</td><td> <a href='#' onclick=\"consultar('$ip')\">". $ip . "</a></td>\n";
		$cantidad--;
                $message .="</tr>";
	}
}
$message .= "</table></td>";
$message .= "<td>";
$message .= "<div id='resultado'></div>";
$message .= "</td></table></div>";
sub ordenar_consumo {
        $sitios{$b}->{size} <=> $sitios{$a}->{size}
                ||
        $a cmp $b
}


sub get_size{
  my($bytes) = @_;

  return '' if ($bytes eq '');

  my($size);
  $size = $bytes . ' Bytes' if ($bytes < 1024);
  $size = sprintf("%.2f", ($bytes/1024)) . ' KB' if ($bytes >= 1024 && $bytes < 1048576);
  $size = sprintf("%.2f", ($bytes/1048576)) . ' MB' if ($bytes >= 1048576 && $bytes < 1073741824);
  $size = sprintf("%.2f", ($bytes/1073741824)) . ' GB' if ($bytes >= 1073741824 && $bytes < 1099511627776);
  $size = sprintf("%.2f", ($bytes/1099511627776)) . ' TB' if ($bytes >= 1099511627776);

  return $size;
}

print $message;
