#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;

my $user = &validate;

my $sth = $dbh->prepare("select * from cookie WHERE cookuser=?") or &dberror;
$sth->execute($user) or &dberror;
my $rec = $sth->fetchrow_hashref;

my $cookie = cookie(-name=>'cid', -value=>$rec->{cookcoid}, -expires=>'now');

$sth = $dbh->prepare("DELETE from cookie WHERE cookuser=?") or &dberror;
$sth->execute($user) or &dberror;
&adlog("El usuario $user, salio del sistema correctamente.",$user);
shared::header();
print qq(<script type="text/javascript">reload()</script>);

