package shared;

require 'config.pm';
use Switch;
use Config;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

sub get_fecha_hora(){
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$year += 1900;
$mon++;

my $fecha= "$year/$mon/$mday";
my $hora= "$hour:$min:$sec";

return $fecha,$hora;
}


sub htmlbox {		# Uso: htmlbox("titulo","mensaje");
	switch ($_[0]) {
		case "notopened" 	{ 
				$title="El archivo no pudo abrirse";
				$message="<b >El archivo " . $_[1] . " no se puede abrir!</b><br>";
				$message .= "<a href=\"check.cgi\">Verifique los permisos y rutas de configuracion.</a>"
		}
		case "access" { 
			$title="Archivo incorrecto"; 
			$message="<b>No tiene permisos suficientes para acceder al archivo: " . $_[1] . "</b><br>";
			$message .= "<a href=\"check.cgi\">Verifique los permisos y rutas de configuracion.</a>"
		}else{ 
			$title=$_[0];
			$message=$_[1];
		}
	}
	$wrongfile = "
	<table width=100% height=100%>
	    <tr valign=top>
	    <td align=center>
	        <table class=\"mid\">
	            <tr valign=middle>
	            <td align=center class=\"mid\">
	            $message
	            </td></tr>
	         </table>        
	    </td></tr>
	</table>
	";
	print $wrongfile;
	
}

sub modulo {    #encabezado
    $arg=$_[0];
    print <<EOT
    <div id="titulo">
    <h1 class="titulo">$arg</h1>
    </div>
EOT
;
        
}
sub header {	#encabezado
	$arg=$_[0];
	$arg2=$_[1];
	
	if ($arg2 eq ""){
		print <<EOT
Content-type: text/html\n\n
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>$arg</title>
    <link rel="stylesheet" type="text/css" 
      href="/css/estilo.css" />
    <link rel="stylesheet" type="text/css" 
      href="/css/jquery-ui-1.10.2.custom.css" />
    <script type="text/javascript"
      src="/js/jquery.js"></script>
    <script type="text/javascript"
      src="/js/jquery-ui-1.10.2.custom.js"></script>
      <script type="text/javascript"
      src="/js/jslib.js"></script>
     <script>
    \$(function() {
      \$( "#menu" ).menu();
      
    });
    </script>       
  
      
</head>
<body>    
EOT
;
}
else{
	print <<EOT
Content-type: text/html\n\n
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>$arg</title>
    <link rel="stylesheet" type="text/css" 
      href="/css/estilo.css" />
    <link rel="stylesheet" type="text/css" 
      href="/css/jquery-ui-1.10.2.custom.css" />
    <script type="text/javascript"
      src="/js/jquery.js"></script>
    <script type="text/javascript"
      src="/js/jquery-ui-1.10.2.custom.js"></script>
      <script type="text/javascript"
      src="$arg2"></script>
     <script>
    \$(function() {
      \$( "#menu" ).menu();
      
    });
    </script>       
  
      
</head>
<body>    
EOT
;
	
}
		
}

sub header_menu {	#encabezado
print <<EOT
Content-type: text/html\n\n
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title></title>
    <link rel="stylesheet" type="text/css" 
      href="/css/estilo.css" />
    <link rel="stylesheet" type="text/css" 
      href="/css/jquery-ui-1.10.2.custom.css" />
    <script type="text/javascript"
      src="/js/jquery_menu.js"></script>
    <script type="text/javascript"
      src="/js/jquery-ui-1.10.2.custom.js"></script>
      <script type="text/javascript"
      src="/js/jslib.js"></script>
     <script>
     \$(document).ready(function(){
     \$("#accordian h3").click(function(){
		\$("#accordian ul ul").slideUp();
		if(!\$(this).next().is(":visible")){
			\$(this).next().slideDown();
		}
	}); 	

    });
    </script>       
  
      
</head>
<body>    
EOT
;		
}

sub arch{
my $arch="$Config{archname}";
my @val = split('-',$arch);
return @val[0];
}
sub copy_log{

    my $SQUID_CP = '/Tools/bin/squid_copy';
    my $FLAG=0;
    my $ERROR        = '';
    if (!-x $SQUID_CP) {
            $SQUID_CP = '';
    }
    if ($SQUID_CP) {
            $ERROR = `$SQUID_CP 2>&1`;
            $FLAG=-1
            if ($ERROR);
            $FLAG=1
            if (!$ERROR);
    }
    else{
     $FLAG=0;
    }
return $FLAG
}
sub perm_log{
    my $SQUID_PR = '/Tools/bin/squid_perm';
    my $FLAG=0;
    my $ERROR        = '';
    if (!-x $SQUID_PR) {
            $SQUID_PR = '';
    }
    if ($SQUID_PR) {
            $ERROR = `$SQUID_PR 2>&1`;
            $FLAG=-1
            if ($ERROR);
            $FLAG=1
            if (!$ERROR);
    }
    else{
     $FLAG=0;
    }



return $FLAG
}
sub delete_log{

    my $SQUID_DL = '/Tools/bin/squid_delete';
    my $FLAG=0;
    my $ERROR        = '';
    if (!-x $SQUID_DL) {
            $SQUID_DL = '';
    }
    if ($SQUID_DL) {
            $ERROR = `$SQUID_DL 2>&1`;
            $FLAG=1
            if ($ERROR);
            $FLAG=1
            if (!$ERROR);
    }
    else{
     $FLAG=0;
    }
return $FLAG
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

sub squid_exe{
    my $BINARY = '/Tools/bin/squid_executor';
    print qq(Content-type: text/html \n\n);
    my $ERROR        = '';
    my $msg;
    if (!-x $BINARY) {
            $BINARY = '';
    }
    if ($BINARY) {
       $ERROR = `$BINARY 2>&1`;
       $msg=$ERROR
       if ($ERROR);
       $msg="<b>Modificado y aplicado con exito!</b>" 
       if (!$ERROR);
    }
    else{
        $msg="El archivo no existe!";
    }		
    return $msg
}

sub iptables_exe{
    my $BINARY = '/Tools/bin/iptables_executor';
    print qq(Content-type: text/html \n\n);
    my $ERROR        = '';
    my $msg;
    if (!-x $BINARY) {
            $BINARY = '';
    }
    if ($BINARY) {
       $ERROR = `$BINARY 2>&1`;
       $msg=$ERROR
       if ($ERROR);
       $msg="<b>Modificado y aplicado con exito!</b>" 
       if (!$ERROR);
    }
    else{
        $msg="El archivo no existe!";
    }		
    return $msg
}

return 1;
