#!/usr/bin/python

import re, os, glob


# The function of this script is to take the tab delimited table of cluster similarity scores found
# in cluster_sim_scores.txt and determine which clusters have a similarity greater than or equal to
# 70%. The script then sends a command to the shell to copy the alignment file associated with the
# cluster ID number to a new folder. This allows us to work only with alignments that have similarity
# scores greater than or equal to 70%. The number can be changed.
                                                                 
# Open the cluster_sim_scores text file to be read only                                                                            
scores = open("cluster_sim_scores.txt", "r")

# For loop that goes through each line of the text file
for line in scores:

	# Here we are looking for whether the line matches this string, which should look something like "V3ZRG3 91"
	match = re.match("(.*)\t([0-9]*)", line)

	if match:
		clusterName = match.group(1)
		score = match.group (2)

	# Now we have created two objects: 1) clusterName, which contains the cluster ID number, and 2) 
	# score, which contains the similarity score for that cluster
		
	# Here, we are trying to determine if the score is greater than or equal to 70%. If it is, we
	# send a command to the shell that copies the aln file for that cluster and sends it to a new 
	# folder, greater_than_70/

	if int(score) >= 70:
				
		print "cp Level50_ClusterUniRef50_" + clusterName + ".aln greater_than_70/"
		os.system("cp Level50_ClusterUniRef50_" + clusterName + ".aln greater_than_70/")
	else:
		print clusterName + " has less that 70% similarity" 


		
		
