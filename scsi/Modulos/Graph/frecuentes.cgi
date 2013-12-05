#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

shared::header ("Sitios frecuentes","");

my $cantidad = 20;
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
my($sitio_url, %sitios);

shared::perm_log();

$message .= "<div id=alinear>";
$message .= "<h1>Los $cantidad sitios más frecuentes</h1>";
$message .= "<p id='Generated'>Reporte generado en fecha $fecha a horas $hora</p>";
$message .= "<table >";
$message .= "<tr><td><b>Consumo</b></td><td><b>Pagina WEB</b></td></tr>";
open(LOG, "$logFile") or die "No se puede abrir el archivo $logFile! por favor verifique los permisos del archivo...";
  
while(<LOG>)
{
	$row = $_;
	($epoch_time_miliseconds, $unknown_integer1, $ip, $tcp_and_http_code, $unknown_integer2, $http_method, $url, $minus, $squid_method_site_url, $content_type) = split(/\s+/, $row);
	$url =~ s/http:\/\///;
	$url =~ s/ftp:\/\///;
	$url =~ s/www.//;
	$url =~ s/\/$//;
	if (!$url ){
		next;
	}
	($sitio_url) = ($url =~ m{ ([A-Za-z0-9.\-:]+)}x );

	if($content_type =~ m{text/html}){
		if ($sitios{$sitio_url}){
		     $sitios{$sitio_url}->{count}++;
		}
		else{
			$sitios{$sitio_url}->{count} = 1;
		}
	}

	if (!$sitios{$sitio_url}->{size}){
		$sitios{$sitio_url}->{size} = 0;
	}
	$sitios{$sitio_url}->{size} = $sitios{$sitio_url}->{size} + $unknown_integer2;
}


foreach $sitio_url ( sort ($ordenar keys (%sitios) ) )
{
	if ($cantidad > 0)
	{
                $message .="<tr>";
		if ($ordenar eq "by_times_visited_then_name")
		{
			$message .="<td>".$sitios{$sitio_url}->{count} ."</td><td><a href=\"http://" . $sitio_url . "/\">" . $sitio_url . "</a></td>\n";
		}
		elsif ($ordenar eq "ordenar_consumo")
		{
			$message .="<td>".shared::get_size($sitios{$sitio_url}->{size}) ."</td><td><a href=\"http://" . $sitio_url . "/\">" . $sitio_url . "</a></td>\n";
		}

		$cantidad--;
                $message .="</tr>";
	}
}

$message .= "</table></div></body></html>";

sub ordenar_consumo {
        $sitios{$b}->{size} <=> $sitios{$a}->{size}
                ||
        $a cmp $b
}



print $message;