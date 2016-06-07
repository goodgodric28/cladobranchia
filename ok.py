input = open("sequence_counts", "r")
output = open("yes", "w")
line = input.readline().strip('\n')

while(line != ""):
	if(line != "1"):
		output.write(line + '\n')
	line = input.readline().strip('\n')
	
input.close()
output.close()
