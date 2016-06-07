#!/usr/bin/python                                                                                                      

#Requirements for this script: 1. Must be run in the same directory as the .aln files, 2. Must have t_coffee in same folder, and 3. Must have blosum in the same folder, and 4. The prefix must be included as a system argument for this to run properly. The names of the .aln files may need to be checked for each section as well.

#Usage: 'python find_alns_70_or_greater 6157_0.5_UniRef50_'

import glob, os, re, sys


#Example of a prefix: 6157_0.5_UniRef50_
prefix = str(sys.argv[1])

#aln_similarity_scores.py
#------------------------------------

#The function of this script is to take each aln file within a directory and generate a .score file using t_coffee     
#This file will contain a similarity score and associated output from t_coffee using the blosm62 substitution matrix   

print "Creating score files... "
count = 0

for file in glob.glob("*.aln"):


        #This takes the name of the file of interest from before the .aln so it can be transplanted onto the .score extension                  
        name = str(file).split(".")[0]
        count += 1

        #This prints the command that is being run in order to keep track of the .aln files that have been completed   
        #print("./t_coffee -other_pg seq_reformat -in " + str(file) + " -action +evaluate blosum62mt -output score_ascii  > " + name + ".score")

        #This is the part of the script that outputs this command to the shell for each .aln file, which is generating  similarity scores and outputting them to the .score file                                                              
        os.system("./t_coffee -other_pg seq_reformat -in " + str(file) + " -action +evaluate blosum62mt -output score_ascii > " + name + ".score")

print "completed " + str(count) + " files.\n"

#====================================


#concatenate_scores.py
#------------------------------------

#The function of this script is to take all of the .score files in a directory                                                                  
#and put the cluster name and similarity score into a tab delimited table in                                                                    
#the newly created file cluster_sim_scores.txt                                                                                                  
 
#The output of this file is a text file that will have a list of the cluster ID                                                                  
#numbers and their respective alignment similarity scores                                                                                       

print "Concatenating scores... "
count = 0
output = open("cluster_sim_scores.txt", "w")

for file2 in glob.glob("*.score"):

        #Looks for the file name to match the string provided. If it does, a new object is                                                       
        #created called clusterName that contains the cluster ID. The string will need to be changed                                            
        #based on the names of the .score files                                                                                                  
        match = re.match(prefix + "(.*)\.score", file2)
        if match:
            clusterName = match.group(1)

        #print clusterName

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
        count += 1

print "analyzed " + str(count)+ " score files.\n"

scorefile.close()
output.close()

#====================================


#aln_greater_than_70.py
#------------------------------------

# The function of this script is to take the tab delimited table of cluster similarity scores found                                              
# in cluster_sim_scores.txt and determine which clusters have a similarity greater than or equal to                                              
# 70%. The script then sends a command to the shell to copy the alignment file associated with the                                               
# cluster ID number to a new folder. This allows us to work only with alignments that have similarity                                            
# scores greater than or equal to 70%. The number can be changed.                                                                                

# Open the cluster_sim_scores text file to be read only                                                                                          
print "Moving files... "
count = 0
scores = open("cluster_sim_scores.txt", "r")
os.system ("mkdir greater_than_70")

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

                #print "cp Level50_ClusterUniRef50_" + clusterName + ".aln greater_than_70/"
                os.system("cp " + prefix + "_" + clusterName + ".aln greater_than_70/")
                count += 1
        else:
                print clusterName + " has less that 70% similarity"

print "moved " + str(count)+ " files.\n"

#=====================================


#avg_aln_similarity
#-------------------------------------

print "Calculating average similarity score... "

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
