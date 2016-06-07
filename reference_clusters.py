#!/usr/bin/python                                                                                   

#The function of this script is to                                           

import os, re

reference = open("ref_mapping.txt", "r")

for line in reference:
    
    match = re.match("\"[0-9]*\"\ ([0-9]*)\ \"(.*)\"", line)

    if match:
        number = match.group(1)
        clusterName = match.group(2)

        if int(number) == 6500:

            os.system("cp Level50_ClusterUniRef50_" + clusterName + ".aln test/")
            
        else:
            print "Different Taxon"

reference.close()
        
            
