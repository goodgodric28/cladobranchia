#!/usr/bin/python

#The function of this script is to take all of the .score files in a directory
#and put the cluster name and similarity score into a tab delimited table in 
#the newly created file cluster_sim_scores.txt

#The output of this file is a text file that will have a list of the cluster ID
#numbers and their respective alignment similarity scores

import glob, re

#Opens the output file
output = open("cluster_sim_scores.txt", "w")


for file2 in glob.glob("*.score"):
	
	#Looks for the file name to match the string provided. If it does, a new object is 
	#created called clusterName that contains the cluster ID. The string will need to be changed
	#based on the names of the .score files
	match = re.match("Level50\_ClusterUniRef50\_(.*)\.score", file2)
        if match:
            clusterName = match.group(1)
	    
	print clusterName

	#Opens the .score file into an object
	scorefile = open(file2, "r")
	
	#Allows me to look at a particular line within the .score file. The score is always on the
	#fourth line in the file, so I look to match that line with a score string and break the 
	#for loop after that line
	for i, line in enumerate(scorefile):
       		if i == 3:
			match2 = re.match("SCORE=([0-9]*)", line)
		elif i > 3:
	       		break

	#This creates a new object with the score taken from the .score file
       	if match2:
       		score = match2.group(1)

	#This writes a new line in the text file with the cluster ID and score separated by a tab
	output.write(clusterName + "\t" + score  + "\n")
	
scorefile.close()

output.close()

