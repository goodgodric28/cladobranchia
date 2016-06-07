import glob, re
keys = open('uid.txt', 'r').read().strip().split('\n')
values = open('nid.txt', 'r').read().strip().split('\n')
uniquetaxonids = open('gastropodaidfor0.5.txt', 'r').read().strip().split('\n')
mapping = dict(zip(keys,values))
members = ['']*8852
n = 0
UniId = 0

for f in glob.glob('*.fasta'):
    print(f)
    cluster = open(f, 'r')
    if (cluster.read().count('>')>1):
        cluster = open(f, 'r')
        flag = 0
        while cluster:
            if flag == 0:
                x = cluster.readline()
                flag = 1
            if not x:
                break
            match = re.match(">.*", x)
            if match: 
                if x[1] == "U":
                    UniId = x.split(' ')[0].strip('>')
                elif (x[1] == "t" or "s"):
                    UniId = x.split(' ')[0].strip('>').split('|')[2]
                else:
                    print("SWAG")
                    print(x)
                #print UniId
                if(UniId != 0):
                    ncbi = open('gastropodaidfor0.5.txt', 'r')
                    ncbiId = int(mapping.get(UniId))
                    #print ncbiId
                    for i in ncbi:
                        if(int(i.strip("\n")) == ncbiId):
                            #print("ya")
                            if(members[n] == ""):
                                # print("first")
                                members[n] = x
                                x = cluster.readline().strip()
                                newmatch = re.match(".*>.*", x)
                                while not newmatch:
                                    members[n] = members[n] + x
                                    x = cluster.readline()
                                    if not x:
                                        break
                                    newmatch = re.match(".*>.*", x)
                                 # print members[n]
                            else:
                                 #print("second")
                                members[n] = members[n] + x
                                x = cluster.readline()
                                newmatch = re.match(".*>.*", x)
                                while not newmatch:
                                    members[n] = members[n] + x
                                    x = cluster.readline()
                                    if not x:
                                        break
                                    newmatch = re.match(".*>.*", x)
                                 # print members[n]
                            break
                        n += 1
                n = 0	
                UniId = 0
        
county = 0
for i in members:
    output = open("taxon_fastas/" + str(uniquetaxonids[county]) + ".fasta", "w")
    output.write(i)
    county += 1

output.close()
ncbi.close()

#input = open("array","r")
#output = open("hits","w")

#for line in input:
#    if(line == "\n"):
#        output.write("0\n")
#    else:
#        n = len(line.strip().split(" "))
#        output.write(str(n) + "\n")
    
#input.close()
#output.close()

#file2 = open("hits", "r")
#biggest = open("singlehits.txt", "w")

#top = 0
#count = 0
#topcount = 0
#while file2:
#    x = file.readline()
#    if not x:
#        break
#    if int(x) > top:
#        top = int(x)
#        topcount = count
#    count += 1

#biggest.write(members[topcount])

#biggest.close()
#file2.close()
