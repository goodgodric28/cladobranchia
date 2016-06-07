#!/usr/bin/python                                                                                                                                                                                                                                                                                                            

#The function of this script is to                                                                                                                                                                                                                                                                                           

import os, glob, re

for file2 in glob.glob("*.aln"):
    
    match = re.match("Level50\_ClusterUniRef50\_(.*)\.aln", file2)

    if match:
        
        clusterName = match.group(1)

        print "cp ../../../0.5/Level50_ClusterUniRef50_" + clusterName + ".fasta ../fa_dir/" 

        os.system("cp ../../../0.5/Level50_ClusterUniRef50_" + clusterName + ".fasta ../fa_dir/")
