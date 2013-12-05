use Net::Pcap;
use strict;

my $err;
my $dev = Net::Pcap::lookupdev(\$err);
if (defined $err) {
    die 'Unable to determine network device for monitoring - ', $err;
}