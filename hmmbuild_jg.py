import os, glob, re

for file2 in glob.glob("*.aln"):
	match = re.match("(.*).aln", file2)
	
	if match:
		clusterName = match.group(1)
		print clusterName

		os.system("hmmbuild --informat afa --amino " + clusterName + ".hmm " + clusterName + ".aln")


#NOTE: to create name file, use this command
#find . -maxdepth 1 -name "*.fasta" -size +1c > file_list
#Then on emacs, do Cltr-x, replace-string for ./ and .aln to blank space
