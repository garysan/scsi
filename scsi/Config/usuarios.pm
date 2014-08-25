package usuarios;
require 'config.pm';            
require 'shared.pm';

use base qw(Exporter);
use strict;
our @EXPORT = qw($dbh 
                    printmsg
                    validate 
                    valadmin
                    ira_login
                    fail 
                    vererror 
                    mensaje 
                    mostrar 
                    dberror 
                    msg
                    box
                    newfile
                    adlog
                    encrypt
                    random_password
                    );
our @EXPORT_OK = qw();

use DBI;
use CGI qw(:standard);

my $cookie="";

our $dbh = DBI->connect( "dbi:mysql:$config::database","$config::userbase", "$config::passbase") or 
    &vererror("Imposible conectar a la BD:\n $DBI::errstr");

sub printmsg{
    my($msg) = @_;
    print qq(Content-type: text/html \n\n);
    print qq($msg);
    exit;    
}

sub validate {
    my $username="";
    $cookie=cookie('cid');
    if (cookie('cid')) {
       my $sth = $dbh->prepare("SELECT cookuser FROM cookie WHERE cookcoid='$cookie' ") or &dberror;
       #$sth->trace( 3, '/tmp/te.txt' );
       $sth->execute;
       my $rec;
       unless ($rec = $sth->fetchrow_hashref) {
          &alogin; 
       }
       $username = $rec->{cookuser};
    } else {
       &alogin;
    }
    return $username;
}

sub valadmin {
    my $username=$_[0];
    my $sth = $dbh->prepare("SELECT adusrusrn FROM adusr WHERE adusradmn=1 AND adusrstat=1 AND adusrusrn='$username' ") or &dberror;
       #$sth->trace( 3, '/tmp/ad.txt' );
       $sth->execute;
       my $rec;
       unless ($rec = $sth->fetchrow_hashref) {
          $username=""; 
       }
       $username = $rec->{adusrusrn};
    return $username;
}



sub alogin {
 
    my $url = $ENV{REQUEST_URI};
    print redirect("http://$config::ipsystem/");
    exit;
}

sub fail {
	my($msg) = @_;
    print header;
    print start_html("Error");
    print "<h2>Error</h2>\n";
    print $msg;
    exit;
}

sub vererror {
    my($msg) = @_;
    shared::header ();
    print qq(
    <div class="center_screen">
    <h2>$msg
    </h2>
    </div>);
    
    exit;
}

sub mensaje{
    my($msg) = @_;
    shared::header ("Mensaje");
    print qq(
    <div class="center_screen">
    <h2>$msg
    </h2>
    </div>);
    
    exit;
}

sub mostrar{
    my($msg) = @_;
    print header;
    print start_html("Mostrar");
    print "<h2>Mostrar Valor</h2>\n";
    print $msg;
    exit;
}

sub dberror {
    print qq(Content-type: text/html \n\n);
    my($package, $filename, $line) = caller;
    my($errmsg) = "Error en la base de datos: $DBI::errstr<br>\n invocacion desde $package $filename linea $line";
    &msg($errmsg);
}

sub msg{
    my($msg) = @_;
    #print qq(Content-type: text/html \n\n);
    print qq($msg);
    exit;    
}

sub box {
    my $titulo=$_[0];
    my $mensaje= $_[1];
    #print "Content-type: text/html\n\n";
    print "
    <link rel=\"stylesheet\" href=\"/css/jquery-ui-1.10.2.custom.css\" />
    <script src=\"/js/jquery.js\"></script>
    <script src=\"/js/jquery-ui-1.10.2.custom.min.js\"></script>
    <script>
    \$(function() {
      
    \$( \"#box\" ).dialog({
     modal: true,
      buttons: {
        Ok: function() {
             \$( this ).dialog( \"close\" );
        }
      }
      
    });
  });
  </script>
    ";
    print "<body>
    <div id=\"box\" title=\"$titulo\">
    
    $mensaje
    
    </div>";
    exit;
    
    
}
sub newfile {
    my $titulo=$_[0];
    my $mensaje= $_[1];
    my $archivo= $_[2];
    my $origen= $_[3];
    print "
    <link rel=\"stylesheet\" href=\"../css/smoothness/jquery-ui-1.10.0.custom.css\" />
    <script src=\"../js/jquery.js\"></script>
    <script src=\"../js/jquery-ui.js\"></script>
    <script>
    \$(function() {
    \$( \"#box\" ).dialog({
     resizable: false,
     modal: true,
      buttons: {
      Si: function() {
      var ip= prompt('Valor Inicial');
      window.location.href=\"../Tools/newfile.cgi?params=$archivo,$origen,\"+ip;
      target=\"main\";
      },
      No: function() {
      window.location.href = \"$origen\" ;
      target=\"main\";
      }
     }
      
    });
  });
  </script>
    ";
    print "<body>
    <div id=\"box\" title=\"$titulo\">
    
    $mensaje
    
    </div>";
    exit;
    
    
}

sub adlog {
my $desc=$_[0];    
my $user=$_[1];    
    my ($fecha,$hora) = shared::get_fecha_hora();
    my $sth = $dbh->prepare("INSERT INTO adlog VALUES('','$desc','$user','$fecha','$hora')") or &dberror;
       
      $sth->execute() or &dberror;
}



sub encrypt {
    my($plain) = @_;
    my(@salt) = ('a'..'z', 'A'..'Z', '0'..'9', '.', '/');
    return crypt($plain, $salt[int(rand(@salt))] . $salt[int(rand(@salt))] 	);
}


sub random_password {
    my($length) = @_;
    if ($length eq "" or $length < 3) {
        $length = 6;            #Mas de 6 caracteres.
    }
    my @letters = ('a'..'z', 'A'..'Z', '0'..'9');
    my $randpass = "";
    foreach my $i (0..$length-1) {
      $randpass .= $letters[int(rand(@letters))];
    }
    return $randpass;
}



1;
