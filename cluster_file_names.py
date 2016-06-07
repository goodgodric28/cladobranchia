#!/usr/bin/python                                                                                                                                                                                                                                                                                                            

import glob, re, os


# Looks in the current directory for .aln files, then search through it using the index number provided                                                                                                                                                                                                                      
for file2 in glob.glob("*.fasta"):

        # Looks at the name and decides whether it matches the pattern given                                                                                                                                                                                                                         
        match = re.match("Level50\_ClusterUniRef50\_(.*)\.fasta", file2)

        if match:
                clusterName = match.group(1)

            # This goes into the shell and changes the name of the <file name>clusterName.aln to clusterName.aln to get rid of the fasta                                                                                                                                                                                           
		#print "mv " + file2 + " " + clusterName + ".fasta"
		os.system("mv " + file2 + " " + clusterName + ".fasta")

            
		print clusterName + " complete."
