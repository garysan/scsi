#!/usr/bin/perl -X
require '../../Config/config.pm';            
require '../../Config/shared.pm';
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use lib '../../Config';
use usuarios;
my $usuario = &validate;

shared::header ("Pie");
print qq(
<div class="color_pie" align="center">
$config::progname,
Version del programa: <b>$config::version</b>
Estado del programa: <b>$config::progmod</b>
</div>
</body>
</html>
);