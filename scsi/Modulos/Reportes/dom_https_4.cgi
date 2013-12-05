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
my $reporte = "excepciones https.pdf";
my $titulo="Lista de excepciones HTTPS";
shared::header ("","reportes.js");
shared::modulo ("$titulo");
$filename = $config::iptablesconf;
$iptables = $config::iptablesconf;

if (!open(IPTABLES, "$iptables"))
{
	&box("Error","El archivo $iptables no existe.");
	die;
}
$search = 0;

$message .= "<div id=alinear>";
$message .= "<table id=\"tabla_general\">";

####################PDF TABLE
my $pdftable = PDF::Table->new();
my $pdf      = PDF::API2->new( -file => "$reporte" );
my $page_num  = 1;
my $data =[];

push(@$data , ["Nro","Direccion IP permitida"]);

while (my $line=<IPTABLES>)
{
	$search=1;
	my @valores=split('=',$line);
	if ($search == 1) {
                $valores[1] =~ s/\n//g;
                
                if ($valores[0]eq "DOM"){
                    $i+=1;
                    my $var="dom";
                    my @dom=split(',',$valores[1]);
                    my $j=0;
                    
                    foreach (@dom){
                    $dom[$j]=~ s/"//g;
                    push(@$data , [$j+1,$dom[$j]]);    
                    $j+=1; 
                    }
                }
	}
	
};####While!



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
 
if ($search == 0) {
    &box("Error","El archivo $iptables, no esta correctamente configurado, Lea el README del programa.");
    die;
}

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
