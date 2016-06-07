#!/usr/bin/python   


#The function of this script is to take each aln file within a directory and generate a .score file using t_coffee
#This file will contain a similarity score and associated output from t_coffee using the blosm62 substitution matrix

import glob, os


for file in glob.glob("*.aln"):
	

	#This takes the name of the file of interest from before the .aln so it can be transplanted onto the .score extension
	name = str(file).split(".")[0]

	#This prints the command that is being run in order to keep track of the .aln files that have been completed
	print("./t_coffee -other_pg seq_reformat -in " + str(file) + " -action +evaluate blosum62mt -output score_ascii  > " + name + ".score")

	#This is the part of the script that outputs this command to the shell for each .aln file, which is generating similarity scores and outputting them to the .score file
	os.system("./t_coffee -other_pg seq_reformat -in " + str(file) + " -action +evaluate blosum62mt -output score_ascii > " + name + ".score")
