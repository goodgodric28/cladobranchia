#!/usr/bin/python                                                                              

import re, os, glob

scores = open("cluster_sim_scores.txt", "r")
count = 0
total = 0

# For loop that goes through each line of the text file                                        
for line in scores:

# Here we are looking for whether the line matches this string, which should look something like "V3ZRG3 91"                                                                        
 
        match = re.match("(.*)\t([0-9]*)", line)

        if match:
                clusterName = match.group(1)
                score = match.group (2)
        
        count += 1
        total += int(score)

average = total / count

print "The average similarity is: " +  str(average)
