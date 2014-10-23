#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $co=new CGI;
my $user = param('usuario');
my $pass = param('password');
my $usuario ="";
my $query = "SELECT adusrnomb FROM adusr WHERE adusrusrn='$user' AND adusrclav=MD5('$pass') AND adusrstat=1 ";
my $sth = $dbh->prepare($query) or &dberror;
$sth->execute;

if($usuario = $sth->fetchrow_array){
    
    my $cookie_id = &random_id;
    my $cookie = cookie(-name=>'cid',  value=>$cookie_id, -expires=>'+1y');
    $sth = $dbh->prepare("INSERT INTO cookie VALUES(?, ?, current_timestamp(), ?)") or &dberror;
    $sth->execute($cookie_id, $user, $ENV{REMOTE_ADDR}) or &dberror;
    if (param('page')) {
       my $url = param('page');
       print redirect(-location=>"http://$config::ipsystem/$url", -cookie=>$cookie);
    
    } else { 
        print header(-cookie=>$cookie);
        my ($fecha,$hora) = shared::get_fecha_hora();
        $sth = $dbh->prepare("UPDATE adusr set adusrflog=?,adusrhlog=? WHERE adusrusrn=?") or &dberror;
        $sth->execute($fecha,$hora,$user) or &dberror;
        &adlog("El usuario $user ingreso al sistema",$user);
        &msg("<script type=\"text/javascript\">go_link('../Workbench/main.cgi')</script>");

    }	
}

else{
    print qq(Content-type: text/html \n\n); 
    &adlog("Intento erroneo de $user",'');   
    &msg("<b><font color='#e80000'>Error, Verifique los datos e intente nuevamente.</font><b>
          <script type=\"text/javascript\">limpiar_login()</script>");
}
	
sub random_id {
    my $rid = "";
    my $alphas = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    my @alphary = split(//, $alphas);
    foreach my $i (1..32) {
       my $letter = $alphary[int(rand(@alphary))];
       $rid .= $letter;
    }
    return $rid;
}
