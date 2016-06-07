import re, glob

output = open("transpos", "w")
n = 0

for file in glob.glob("*.fasta"):
	input = open(file, "r")
	line = input.readline()
	title = str(input).split("'")[1].split(".")[0]
	while line:
		if not line:
			break
		match = re.match(".*transpos.*", line, re.IGNORECASE)
		match2 = re.match(".*pol protein.*", line, re.IGNORECASE)
		match3 = re.match(".*gag-pol polyprotein.*", line, re.IGNORECASE)
		match4 = re.match(".*pol polyprotein.*", line, re.IGNORECASE)
		if match or match2 or match3 or match4:
			if n == 0:
				output.write(title+ "\n")
			output.write(line)
			n = 1
		line = input.readline()
	if n == 1:
		output.write("\n")
	n = 0
output.close()
		
