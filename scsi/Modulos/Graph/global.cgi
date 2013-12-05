#!/usr/bin/perl -w
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
use Time::Local;

shared::header ();

my $cantidad = 20;
my $logfile = "/var/log/squid/access.log";
my $ordenar = "ordenar_consumo";

my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$year += 1900;
$mon++;

my $fecha= "$mday/$mon/$year";
my $hora= "$hour:$min:$sec";

shared::perm_log();

$message .= "<div id=alinear>";
open(LOG, "$logfile") or die "No se puede abrir el archivo $logfile! por favor verifique los permisos del archivo...";

my $data;
my $line;
while (<LOG>)
{
	my ($timestamp, $junk, $ip, $errorcode, $size, $method, $url, $user,
		$routing, $mime_type)
		= split;

        $data= $data+$size;
        
        $row = $_;

	($epoch_time_miliseconds, $unknown_integer1, $ip, $tcp_and_http_code, $unknown_integer2, $http_method, $url, $minus, $squid_method_site_url, $content_type) = split(/\s+/, $row);

	$url =~ s/http:\/\///;
	$url =~ s/ftp:\/\///;
	$url =~ s/www.//;
	$url =~ s/\/$//;
	if (!$url )
	{
		next;
	}
	($sitio_url) = ($url =~ m{ ([A-Za-z0-9.\-:]+)}x );

	if($content_type =~ m{text/html})
	{
		if ($sitios{$sitio_url})
		{
		     $sitios{$sitio_url}->{count}++;
		}
		else
		{
			$sitios{$sitio_url}->{count} = 1;
		}
	}

	if (!$sitios{$sitio_url}->{size})
	{
		$sitios{$sitio_url}->{size} = 0;
	}
	$sitios{$sitio_url}->{size} = $sitios{$sitio_url}->{size} + $unknown_integer2;
}
close LOG;

$data= convertir($data);
$message .="<b>Consumo Global de Internet</b>: <h3>$data</h3>";
$message .="<b>Sitios frecuentes</b><br/>";
$message .="<table>";
$message .="<tr><td><b>Consumo</b></td><td><b>Pagina WEB</b></td></tr>";
foreach $sitio_url ( sort ($ordenar keys (%sitios) ) )
{
	if ($cantidad > 0)
	{
                $message .="<tr>";
		$message .="<td>".shared::get_size($sitios{$sitio_url}->{size}) ."</td><td><a href=\"http://" . $sitio_url . "/\">" . $sitio_url . "</a></td>\n";
                $message .="</tr>";
                $cantidad--;    
	}
}

$message .= "</table></div></body></html>";




sub convertir{
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


sub ordenar_consumo {
        $sitios{$b}->{size} <=> $sitios{$a}->{size}
                ||
        $a cmp $b
}




print $message;
