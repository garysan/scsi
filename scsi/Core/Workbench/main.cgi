#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $usuario = &validate;

print <<EOT
Content-type: text/html\n\n
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>$config::title</title></head>
<FRAMESET cols="250px,*" scrolling=no frameSpacing=0 frameBorder=0 marginWidth=0 marginHeight=0 >
    <FRAME name="menu" src="menu.cgi" noResize  scrolling=no frameSpacing=0 frameBorder=0 marginWidth=0 marginHeight=0 />
    <FRAMESET name="principal" rows="7%,91%,2%" scrolling=no frameSpacing=0 frameBorder=0 marginWidth=0 marginHeight=0 />
        <FRAME name="encabezado" src="encabezado.cgi" noResize scrolling=no frameSpacing=0 frameBorder=0 marginWidth=0 marginHeight=0 />
        <FRAME name="main"       src="aviso.cgi"      noResize scrolling=auto frameSpacing=0 frameBorder=0 marginWidth=0 marginHeight=0 />
        <FRAME name="pie"        src="footer.cgi"     noResize scrolling=no frameSpacing=0 frameBorder=0 marginWidth=0 marginHeight=0 />
    </FRAMESET>
</FRAMESET>
  
</head>
<body>    
EOT
;
