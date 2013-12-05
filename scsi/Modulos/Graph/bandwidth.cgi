#!/usr/bin/perl
 
########
# Prints out the bandwidth for a xx second sample in bps.
# Also prints detailed information with the -p switch.
# By: Thomas Hawkins  Date: Jan. 27, 2011
# incoming bps,outgoing bps
########
 
use strict;
use warnings;
 
sub usage(){
    print "Bandwidth Checker Usage Info\n";
    print "==================================\n";
    print "Flags:\n";
    print "-p Print pretty output\n";
    print "-s Print csv output (incoming bps, outgoing bps). Ex: 5042,239\n";
    print "-h Print this page\n";
    print "Optional: -i or --interface={interface} - An Interface Name. Ex: -i=eth0\n";
    print "Optional: -t or --time={seconds} - The number of seconds to monitor. Ex: -t=15\n";
    print "Example: perl bandwidth-checker.pl -p -i=eth0 -t=15\n";
    exit();
}
 
my($simple,$pretty,$help,$time,$interface,$mode);
$time = 15;
$interface = 'eth0';
$mode = 0;
 
use Getopt::Long;
GetOptions("s"=> \$simple,
           "p"=> \$pretty,
           "h"=> \$help,
           "t:i"=> \$time,
           "time:i"=> \$time,
           "i:s"=> \$interface,
           "interface:s"=> \$interface);
 
if($help){
    #Prints Usage Info
    usage();
    exit();
}
if($simple){
    $mode = 0;
}
if($pretty){
    $mode = 1;
}
 
my($result,$initialrx,$initialtx,$finalrx,$finaltx,$differencetx,$differencerx);
 
#Gets a line indicating the current usage.
$result = `ifconfig $interface | grep "RX bytes"`;
 
#strip it into variables for recieved and transmitted
$result =~ /\s*RX bytes:(\d*).*TX bytes:(\d*).*/;
#This converts the bytes to bits.
$initialrx = $1 * 8;
$initialtx = $2 * 8;
 
#wait x seconds and run the command again.
sleep($time);
#Gets a line indicating the current usage.
$result = `ifconfig $interface | grep "RX bytes"`;
 
$result =~ /\s*RX bytes:(\d*).*TX bytes:(\d*).*/;
#This converts the bytes to bits.
$finalrx = $1 * 8;
$finaltx = $2 * 8;
 
#now print out the results
#print 'RX: ' . $finalrx . ' | ' . $initialrx;
#print 'TX: ' . $finaltx . ' | ' . $initialtx;
 
$differencerx = ($finalrx - $initialrx) / $time;
$differencetx = ($finaltx - $initialtx) / $time;
if($mode == 0){
    print $differencerx . ',' . $differencetx;
}
elsif($mode == 1){
    my($kbitpsrx,$kbitpstx,$KBpsrx,$KBpstx,$kbitrx,$kbittx,$KBrx,$KBtx);
    $kbitpsrx = $differencerx / 1024;
    $kbitpstx = $differencetx / 1024;
    $KBpsrx = $differencerx / 1024 / 8;
    $KBpstx = $differencetx / 1024 / 8;
    $kbitrx = ($finalrx - $initialrx) / 1024;
    $kbittx = ($finaltx - $initialtx) / 1024;
    $KBrx = ($finalrx - $initialrx) / 1024 / 8;
    $KBtx = ($finaltx - $initialtx) / 1024 / 8;
    print "Monitored traffic on interface $interface for $time seconds:\n";
    print "Incoming: $kbitrx kbit ($KBrx KB) Average: $kbitpsrx kbps ($KBpsrx KBps)\n";
    print "Outgoing: $kbittx kbit ($KBtx KB) Average: $kbitpstx kbps ($KBpstx KBps)\n";
}