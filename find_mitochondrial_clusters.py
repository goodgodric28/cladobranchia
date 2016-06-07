#!/usr/bin/python                                                                                                                                                                                                                                                                                                          

import re, os, glob


# The function of this script is to take the tab delimited table of cluster identifiers                                                                                                                     
# in uniprot-mitochondrion+genome+taxonomy-gastropoda.tab and finds the associated align                                                                                                                                                                                                                                   

# Open the cluster_sim_scores text file to be read only                                                                                                                                                                                                                                                                    
scores = open("uniprot-mitochondrion+genome+taxonomy-gastropoda.tab", "r")

# For loop that goes through each line of the text file                                                                                                                                                                                                                                                                    
for line in scores:

        # Here we are looking for whether the line matches this string, which should look something like "V3ZRG3 91"                                                                                                                                                                                                       
        match = re.match("(.*?)\t.*", line)

        if match:
                clusterName = match.group(1)

        # Now we have created an object: 1) clusterName

                print "cp Level50_ClusterUniRef50_" + clusterName + ".aln mitochondrial_clusters/"
                os.system("cp Level50_ClusterUniRef50_" + clusterName + ".aln mitochondrial_clusters/")
        else:
                print clusterName + " can not be found in this file"

