import os, glob, re

count = 0

for file in glob.glob("*.fasta"):

    file2 = open(file, "r")
    
    while file2:
        line = file2.readline()
        if not line:
            break
        match = re.match('>.*', line)
        if match:
            count += 1
    if count >= 2:
        print("/fs/mikeproj/sw/RedHat9-32/bin/einsi " + str(file) + " > " + str(file).split(".")[0] + ".aln 2> " + str(file).split(".")[0] + ".log")
        os.system("/fs/mikeproj/sw/RedHat9-32/bin/einsi " + str(file) + " > " + str(file).split(".")[0] + ".aln 2> " + str(file).split(".")[0] + ".log")

    count = 0
    file2.close()

