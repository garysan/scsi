#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
use File::Basename;
use PDF::API2;
use PDF::Table;

my $usuario = &validate;
my $reporte = "frecuentes.pdf";
my $titulo="Lista de sitios frecuentes";
shared::header ("","reportes.js");
shared::modulo ("$titulo");

my $cantidad = 9000;
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

$message .= "<div id=alinear>";
$message .= "<table id=\"tabla_general\">";

####################PDF TABLE
my $pdftable = PDF::Table->new();
my $pdf      = PDF::API2->new( -file => "$reporte" );
my $page_num  = 1;
my $data =[];

shared::perm_log();
open(LOG, "$logFile") or die "No se puede abrir el archivo $logFile! por favor verifique los permisos del archivo...";

push(@$data , ["Nro","MB Consumidos","Sitio WEB"]); 
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

my $i=1;
foreach $sitio_url ( sort ($ordenar keys (%sitios) ) )
{
	if ($cantidad > 0){
                
                if ($ordenar eq "ordenar_consumo"){
                        push(@$data , [$i,shared::get_size($sitios{$sitio_url}->{size}),$sitio_url]);
                        $i++;
		}
		$cantidad--;
                
	}
}


sub ordenar_consumo {
        $sitios{$b}->{size} <=> $sitios{$a}->{size}
                ||
        $a cmp $b
}

main_table($pdf, $data);

$pdf->saveas();

$message .= "</table></div><br/>

<div id=completo>
<object style=\"float:left;width:100%;height:100%;\" data=\"$reporte\" type=\"application/pdf\">
alt : <a href=\"$reporte\">$reporte</a>
</object>
</div>
<script type=\"text/javascript\">
\$(window).load(function(){
    \$('#completo').width(\$(window).width());
    \$('#completo').height(\$(window).height());
});
\$(window).resize(function(){
    \$('#completo').width(\$(window).width());
    \$('#completo').height(\$(window).height());
});
</script>

<input type=hidden id=\"archivo\" name=\"archivo\" value=\"$filename\">
<input type=hidden id=\"fin\" name=\"fin\" value=\"$i\">";

$message .= "<div id=\"resultado\"></div>";
 
print $message;

sub main_table {
    my $pdf  = shift;
    my $data = shift;
    my $page = newpage();
    $pdftable->table(
        # required params
        $pdf,
        $page,
        $data,
        x => 50,
        w => 505,
        start_y => 700,
        next_y  => 700,
        start_h => 650,
        next_h  => 650,
        padding => 3,
        #padding_right => 10,
        new_page_func => \&newpage, 
        header_props          => { 
             bg_color   => 'silver',
             font       => $pdf->corefont("Helvetica", -encoding => "utf8"),
             font_size  => 10,
             font_color => 'black',
             repeat     => 1,
         },
     );
}    

sub newpage {
my  $page = $pdf->page;
    $page->mediabox('Letter');
    header($page);
    footer($page);
    page_nr($page, $page_num++);

    return $page;
}

sub header {
    my $page = shift;  # we need a page to place ourselves on
    my $head_data =[["$titulo",],["Reporte generador por: $usuario",]];
    $pdftable->table(
    # required params
    $pdf,
    $page,
    $head_data,
    x => 50,
    w => 505,
    start_y => 750,
    next_y  => 700,
    start_h => 400,
    next_h  => 500,
        
    #OPTIONAL PARAMS BELOW
    #max_word_length=> 20,   # add a space after every 20th symbol in long words like serial numbers
    padding        => 2,     # cell padding
    #padding_top    => 1,    # top cell padding, overides padding
    padding_right  => 10,    # right cell padding, overides padding
    #padding_left   => 5,    # left cell padding, overides padding
    #padding_bottom => 5,    # bottom padding, overides -padding
    border         => 0,     # border width, default 1, use 0 for no border
    #border_color   => 'navy', # default black
    font           => $pdf->corefont("Helvetica", -encoding => "utf8"), # default font
    font_size      => 14,
    #font_color_odd => 'black',
    #font_color_even=> 'black',
    
    #background_color_odd  => "#ffffff",
    #background_color_even => "#ffffff", #cell background color for even rows
    #header_props   => $hdr_props,
    column_props   => [ { justify => 'center' } ],
    ); 
}

sub footer {
my $page = shift;  # we need a page to place ourselves on
my $footer_data =[["$config::progname $config::swver $config::progmod"]];
$pdftable->table(
    # required params
    $pdf,
    $page,
    $footer_data,
    x => 50,
    w => 505,
    start_y => 30, # top od doc on page
    next_y  => 30,
    start_h => 30,
    next_h  => 30,
    
    #OPTIONAL PARAMS BELOW
    #max_word_length=> 20,   # add a space after every 20th symbol in long words like serial numbers
    padding        => 5,     # cell padding
    border         => 0,     # border width, default 1, use 0 for no border
    #border_color   => 'red', # default black
    font           => $pdf->corefont("Helvetica", -encoding => "utf8"), # default font
    font_size      => 10,
    #header_props   => $hdr_props,
    column_props   => [ { justify => 'center' } ],
    ); 
}

sub page_nr {
my $page = shift;
my $num  = shift;
$page->gfx->textlabel(   # PDF::API2 method
    570, 15,                           # x, y
    $pdf->corefont("Helvetica", -encoding => "utf8"), 10,   # font, size
    "Pagina $num",                       # text
    -color => '#808080',
    -align => 'right',
    );
}
