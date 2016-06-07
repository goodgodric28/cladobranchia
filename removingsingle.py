import os, glob, subprocess, re

count = 0

for file2 in glob.glob("*.fasta"):

    file = open(file2, "r")

    while file:
        x = file.readline()
        if not x:
            break
        match = re.match(".*>.*", x)
        if match:
            count += 1
            
    if count == 1:
        os.remove(file2)
        
    count = 0
        
