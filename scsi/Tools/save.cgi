#!/usr/bin/perl -X
require '../Config/config.pm';            
require '../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../Config';
use usuarios;

my $usuario = &validate;

shared::header ();
##########Configuration Area##########
$squidconf = $config::squidconf;
######################################
my $val=0;
if ( $config::patchdir ne ""){
    #backup configuracion anterior.
    system ("cp $squidconf /patchdir/scsi-file1");
}
$i = param("number");

if (!open (OLDFILE, "$squidconf")){
    &msg("<b>Error:, $squidconf</b>");
}
#Carga el archivo al filevar
while (<OLDFILE>){
	$filevar .= $_;
	
}
close(OLDFILE);

if (!open (NEWFILE, ">$squidconf")){
	print qq(Content-type: text/html \n\n);
    &msg("<b>Error:, $squidconf</b>");
}
    $n=0;
    while ($n != $i) {
        $number=$n+1;
        @name[$n] = param("name$number");
        @original[$n] = param("original$number");
        @new[$n] = param("new$number");
        $n+=1;
    }
    $n=0;
    while ($n != $i) {
        if (param("flag")eq "2"){
        $filevar =~ s/@original[$n] @name[$n]/@new[$n] @name[$n]/g;
        $n+=1;
        }
        else{   
        $filevar =~ s/@name[$n] "@original[$n]"/@name[$n] "@new[$n]"/g;
        $n+=1;
        }
    }
    if (param("flag")eq "1"){
        ####acl clientes src "/etc/squid/clientes.list"
        $filevar =~ s/@name[$i-2] "@original[$i-2]"/@name[$i-2] "@new[$i-2]"\nacl @name[$i-1] "@new[$i-1]"/g;
        @name[$n-$i] =~ s/ src//g;
        @name[$n-1] =~ s/ src//g;
        $filevar =~ s/http_access allow @name[$n-$i]/http_access allow @name[$n-$i]\nhttp_access allow @name[$n-1]/g;
        
        #print qq(<script type="text/javascript">
        #alert ("val @name[$n-1]");
        #</script>);
        
        
    }   
    if (param("flag")eq "3"){
        $filevar =~ s/http_port @original[$n-$i] transparent/http_port @new[$n-$i] transparent/g;
    }
    
   	if (param("flag")eq "4"){
        $filevar =~ s/@name[$n-$i] @original[$n-$i]/@name[$n-$i] @new[$n-$i]/g;
    }
                
    #print qq(<script type="text/javascript">
    #   alert ("$original[0],$name[0],$new[0],$name[0]");
    #   alert ("$original[1],$name[1],$new[1],$name[1]");
    #   alert ("$original[2],$name[2],$new[2],$name[2]");
    #    </script>);
        

print NEWFILE "$filevar";
close(NEWFILE);

if ( $config::patchdir ne "")
{
	system ("cp $squidconf /patchdir/scsi-file2");
}

if ( $config::patchdir ne "")
{
    $patchdir = $config::patchdir;
	chomp ($date = `date +%d-%m-%H-%M:%S `);
	system ("diff -p /patchdir/scsi-file1 /patchdir/scsi-file2 > $patchdir/$date-access.patch");
	#system ("rm -rf /scsi/scsi-file1 /scsi/scsi-file2 ");
	$val=1;
}
#system "$config::squidbin -k reconfigure";

if ($val eq "1") {
      print qq(Content-type: text/html \n\n);
     our $BINARY = '../../Tools/bin/squid_executor';
     my $ERROR        = '';
     if (!-x $BINARY) {
             $BINARY = '';
     }
     if ($BINARY) {
        $ERROR = `$BINARY 2>&1`;
        &msg($ERROR)
        if ($ERROR);
        &msg("<b>Modificado y aplicado con exito!</b>") 
        if (!$ERROR);
     }
     else{
         &msg("El archivo $BINARY no existe");
     }		
}
