import os

input = open("name", "r")

for num in range(1,5):
	word = input.readline().strip('\n')
	print (word)
	os.system("hmmbuild --informat afa --amino " + word + ".hmm " + word+ ".aln")

input.close()
#NOTE: to create name file, use this command
#find . -maxdepth 1 -name "*.fasta" -size +1c > name
#Then on emacs, do Cltr-x, replace-string for ./ and .aln to blank space
