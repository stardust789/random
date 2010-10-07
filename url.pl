use strict;
use warnings;

#use Regexp::Common qw /URI/;

while (1)
{
        #getting the input from stdin.
        print "Enter the line: \n";
        my $line = <>;
        chomp ($line); #removing the unwanted new line character
        my ($uri)= $line =~ /$RE{URI}{HTTP}{-keep}/       and  print "Contains an HTTP URI.\n";
        print "URL : $uri\n" if ($uri);
}
