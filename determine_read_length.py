#!/usr/bin/python

import glob, re

for file in glob.glob("*.fastq"):

    file2 = open(file, "r")
    
    for i, line in enumerate(file2):
        
        if i == 1:
            read = str(line)
            read_length = len(read) - 1
        
        elif i > 1:
            break
    
    print file2,
    print " read length: ",
    print read_length
