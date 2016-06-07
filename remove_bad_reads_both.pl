#!/usr/bin/perl

open REMOVEDR1, ">bad_reads_removed_R1.fastq";
open REMOVEDR2, ">bad_reads_removed_R2.fastq";
open FASTQ, "fastq_files";

while(<FASTQ>) {
    chomp;
    $file = $_;
    print "file is: $file\n";
    $type = "R1";
    if($file =~ /.*_R2_.*/) {
	$type = "R2";
    }
    open FILE, "$file";
    while(<FILE>) {	
	chomp;
	$line = $_;
	if($line =~ /^\@.* 1:Y:[0-9]*:[ACGT]*$/ || $line =~ /^\@.* 2:Y:[0-9]*:[ACGT]*$/) {
	    # throw away this line and the next three
	    $junk = <FILE>;
	    $junk = <FILE>;
	    $junk = <FILE>;
	} else {
	    if($type eq "R1") {
		print REMOVEDR1 $line . "\n";
	    } else {
		print REMOVEDR2 $line . "\n";
	    }
	}
    }
    close FILE;
}
close FASTQ;
close REMOVEDR1;
close REMOVEDR2;
