#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
use File::Basename;

my $usuario = &validate;

shared::header ("","iptables.js");
$filename = $config::iptablesconf;
shared::modulo ("Bloqueo global y administración de excepciones HTTPS.");
$message .="<p>Bloqueo global de https.</p>";

######### config Area #########
$iptables = $config::iptablesconf;
######################################
if (!open(IPTABLES, "$iptables"))
{
	&box("Error","El archivo $iptables no existe.");
	die;
}
$message .= "<div id=alinear>";
$message .= "<table id=\"tabla_general\">";
$message .= "<tr><th>Descripción</th><th>Valor(es)</th><th>Acciones</th></tr>";
$search = 0;

while (my $line=<IPTABLES>)
{
	$search=1;
	my @valores=split('=',$line);
	if ($search == 1) {
                $valores[1] =~ s/\n//g;
                if ($valores[0]eq "GLOB_BLOCK"){
                    $i+=1;
                    my $var="glob";
                    $message .= "\n<tr>";
                    $message .= "<td>" .$i. ". Aplicación Global:</td>";
                    
                    if ($valores[1] eq "\"SI\""){
                        $message .= "<td><input id=\"$var\" value=$valores[1] name=\"$var\"></td>";
                        $message .= "<td><input class=button type=button value=Desactivar onclick=modificar('$var',$valores[1])></td>";
                        $message .= "</tr>";
                    }
                    else{
                        $message .= "<td><input id=\"$var\" value=$valores[1] name=\"$var\"></td>";
                        $message .= "<td><input class=button type=button value=Activar onclick=modificar('$var',$valores[1])></td>";
                        $message .= "</tr>";
                    }

                }
                ###################LISTADOS DE DOMINIOS E IP'S EN EXCEPCIONES
                if ($valores[0]eq "IPS"){
                    $i+=1;
                    my $var="ips";
                    $message .= "\n<tr>";
                    $message .= "<td>" .$i. ". IP's permitidos en https:</td>";
                    $message .= "<td><input type=hidden id='$var-ant' value=$valores[1] name='$var-ant'></td>";
                    $message .= "<td></td>";    
                    $message .= "</tr>";
                    
                    my @ips=split(',',$valores[1]);
                    my $j=0;
                    
                    foreach (@ips){
                    $ips[$j]=~ s/"//g;
                    $message .= "<tr>";
                    $message .= "<td></td>";    
                    $message .= "<td>$ips[$j]</td>";    
                    $message .= "<td><input class=button type=button value=Quitar onclick=quitar('$j','$ips[$j]')></td>";
                    $message .= "</tr>";
                    $j+=1;
                    }
                    $message .= "<tr>";
                    $message .= "<td></td>";    
                    $message .= "<td>$ips[$j]</td>";    
                    $message .= "<td><input class=button type=button value=Añadir onclick=adicionar('$var',$valores[1])></td>";
                    $message .= "</tr>";

                    
                }
                if ($valores[0]eq "DOM"){
                    $i+=1;
                    my $var="dom";
                    
                    $message .= "\n<tr>";
                    $message .= "<td>" .$i. ". Dominios https Bloqueados:</td>";
                    $message .= "<td></td>";
                    $message .= "<td><input type=hidden id='$var-ant' value=$valores[1] name='$var-ant'></td>";    
                    $message .= "<td></td>";    
                    $message .= "</tr>";

                    my @dom=split(',',$valores[1]);
                    my $k=0;
                    
                    foreach (@dom){
                    $dom[$k]=~ s/"//g;
                    $message .= "<tr>";
                    $message .= "<td></td>";    
                    $message .= "<td>$dom[$k]</td>";    
                    $message .= "<td><input class=button type=button value=Quitar onclick=quitar_url('$k','$dom[$k]')></td>";    
                    $message .= "</tr>";
                    $k+=1;
                    }
                    $message .= "<tr>";
                    $message .= "<td></td>";    
                    $message .= "<td>$dom[$k]</td>";    
                    $message .= "<td><input class=button type=button value=Añadir onclick=adicionar_url('$var',$valores[1])></td>";
                    $message .= "</tr>";
                    
                }
	}
	
};####While!
$message .= "</table></div><br/>

<input type=hidden id=\"archivo\" name=\"archivo\" value=\"$filename\">
<input type=hidden id=\"fin\" name=\"fin\" value=\"$i\">";

$message .= "<div id=\"resultado\"></div>";
 
if ($search == 0) {
    &box("Error","El archivo $iptables, no esta correctamente configurado, Lea el README del programa.");
    die;
}

print $message;

