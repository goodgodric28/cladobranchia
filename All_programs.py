#!/usr/bin/python

import re, sys, os, glob, urllib, urllib2, time, shutil
import xml.etree.ElementTree as ET 

#All programs into one

if (len(sys.argv)) < 3:    #Input is the taxid and identity level
    print("Error\nUsage: Please input desired taxon Id and level after program name \nExample: python26 taxonIdFinder.py 6029 1.0")
    sys.exit()          #If these aren't provided, it kills the program
else:
    ncbiid = sys.argv[1]
    level = sys.argv[2]

file = open("mapping.txt", "r")    #Text document containing search terms that correspond to specific taxid

organismlist = []
count = 1

for line in file:
    match = re.match(ncbiid + ".*", line)
    if match:
        while count < len(line.split(" ")):                 #If there is more than one search term, it adds all the terms to an array
            organismlist.append(line.split(" ")[count])   
            count += 1
        
name = ncbiid + "_" + level                 #Start of name for every file 
for files in glob.glob("*.xml"):            #Looks through the xml files in the directory to find the right one
    match = re.match(".*" + ncbiid + ".*" + level, files)
    if match:
        xmlfile = open(files, "r")
	save = str(files)

newfile = open(name + "_NCBI_Ids.txt", "w")         #File containing every NCBI ID found in the xml file

while xmlfile:                                      #Looks through the xml file and matches and cases it finds
    x = xmlfile.readline()
    if not x:
        break
    match = re.match('.*NCBI taxonomy.*[0-9].*', x)
    if match:
        y = re.sub("\D", "", x)
        newfile.write(y)
        newfile.write("\n")
        
newfile.close()
xmlfile.close()

file2 = open(name + "_NCBI_Ids.txt", "r")
newfile2 = open(name + "_Simplified_NCBI_Ids.txt", "w") #File with all unique NCBI ids
array = []
duplicate = []

while file2:
    x = file2.readline()
    if not x:
        break
    array.extend([x])                                   #Adds all IDs to an array


duplicate = list(set(array))                            #Removes repeats in the array

for item in duplicate:                                  #Writes everything in the shortened array to a new file
    newfile2.write(item)
    
print(len(array))                                       #Tells you how many entries
print(len(duplicate))                                   #Tells you how many unique IDs

file2.close()
newfile2.close()

file = open(name + "_Simplified_NCBI_Ids.txt", "r")
newfile = open(name + "_Organism_XML.txt", "w")       #Contains just the xml data for the NCBI Ids of the organism you want
newfile2 = open(name + "_All_XML.txt", "w")           #Contains all the xml data for the NCBI Ids
failfile = open(name + "_Failed_Searches", "w")     #Contains all the searches that were not identified as the specific organism
array = []
count = 0
flag = 0

while file:
    x = file.readline()
    if not x:
        break
    array.extend([int(x)])

while count <= len(array):                          
    link = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=taxonomy&id=" + ','.join(map(str, array[count:(count + 1000)])) #Url for looking up the xml files
    print(link)
    myfile = urllib2.urlopen(link).read().decode("utf-8")           #The decode takes out all the \n etc. to make it easily readable
    newfile2.write(myfile)
    splitmyfile = myfile.split('<DocSum>')
    for x in splitmyfile:
        for organism in organismlist:               #If there were multiple search terms, it looks through the data seperate times for each term
            print(organism.strip())
            match = re.search('.*' + organism.strip() + '.*', x)    #Looks for a specific word taken from the text file mapping.txt to determine which NCBI Ids belong to the certain organism
            if match:
                flag = 1
                newfile.write(x)
        if flag == 0:
            failfile.write(x)                   #If the word is not found is writes those xml data to a different file
        flag = 0
    count += 1000                   #In groups of 1000 (anything more and the url is too long)

print("Finished")
file.close()
newfile.close()
newfile2.close()



file2 = open(name + "_Organism_XML.txt", "r")
newfile3 = open(name + "_Organism_NCBI_Ids.txt", "w")   #Text file with all the specific organism Ids

while file2:
    x = file2.readline()
    if not x:
        break
    match = re.match('.*Id>[0-9].*', x)   #Finds all the lines in the xml files that contain IDs
    if match:
        y = re.sub("\D", "", x)         #Takes out just the Ids
        newfile3.write(y + "\n")            

print("Finished")
file2.close()    
newfile3.close()
xmlfile = open(save, "r")

#With these NCBI Ids, looks through the orignal xml document and parses out all corresponding Uniprot and Uniparc Ids

tree = ET.parse(xmlfile)
print("CREATED TREE")
root = tree.getroot()
ncbi = open(name + "_Organism_NCBI_Ids.txt", 'r').read().strip().split('\n')
accessions = open(name + "_Uniprot_Uniparc_Ids.txt", 'w')          #File containing all Uniprot and Uniparc IDs. All Ids belonging to a cluster are on the same line.
currentCluster = -1                                             #Different line means different cluster
cluster = 0
num = 0
for cluster in range(0, len(root.getchildren())):				#access each cluster
    clusterID = root[cluster].attrib['id']						#Uniref IDs
    for member in range(4, 4 + int(root[cluster][1].attrib['value'])): 	#access members information of each cluster
        currentNCBI = ''
        currentUniProt = ''
        currentUniParc = ''
        for property in root[cluster][member][0].getiterator('{http://uniprot.org/uniref}property'):  #access properties information of each member
            if property.attrib['type']=='NCBI taxonomy': 			
                currentNCBI = property.attrib['value']						#NCBI id for this member
            if root[cluster][member][0].attrib['type']=='UniProtKB ID':
                currentUniProt = root[cluster][member][0].attrib['id']  	#Uniprot id for this member
            if root[cluster][member][0].attrib['type']=='UniParc ID':	
                currentUniParc = root[cluster][member][0].attrib['id']  	#Uniparc id for this member
        if ncbi.count(currentNCBI)>0:
            num = num+1
            if currentCluster!=cluster:
                currentCluster = cluster
                if cluster!=0:
                    accessions.write('\n')
                accessions.write(clusterID + ' ')
            if currentUniProt!='':
                accessions.write(currentUniProt + ' ')
            elif currentUniParc!='':
                accessions.write(currentUniParc + ' ')
            else:
                print("WHAT")
accessions.close()
print(num)


array = []
count = 0
filecount = 0
countfile = 0
clusters = 0
numberineachcluster = []


idFile = open(name + "_Uniprot_Uniparc_Ids.txt", 'r')
onefile = open(name + '_All_Sequences.txt', 'w')        #A single text file with every Uniprot/Uniparc sequence

while idFile:
	
    x = idFile.readline().strip()
    if not x:
        break
    clusterID = x.strip().split(' ')[0]
    sequences = open(name + "_" + clusterID + '.fasta', 'w')   #Names the file with the cluster ID in it, each file represents one cluster
    cluster = set(x.strip().split(' ')[1:])
    clusterlist = list(cluster)            #Adds all the Uniprot or Uniprac Id into an array one line at a time

    for x in clusterlist:
        
        if x[0:3] != "UPI":                                             #This half is for Uniprot ids
            link = "http://www.uniprot.org/uniprot/" + x + ".fasta"        #Url for finding sequence
            try:
                myfile = urllib2.urlopen(link).read().decode("utf-8")       #Tries each url and if theres an error it notes it and keeps going. This way one error doesn't stop the entire program
            except urllib2.URLError, e:
                if hasattr(e, 'code'):
                    if e.code==408:
                        print 'timeout', e.code                     #Connectivity issue
                    if e.code==404:
                        print 'File not found' , e.code             #No such url
                time.sleep(30)                                      #If it finds an error, it waits 30 seconds 
                try:
                    myfile = urllib2.urlopen(link).read().decode("utf-8")       #and tries it again
                except urllib2.URLError, e:
                    if hasattr(e, 'code'):
                        if e.code==408:
                            print 'timeout', e.code
                        if e.code==404:
                            print 'File not found', e.code
                    sequences.write('Error' + link)              #If the error occurs again, it writes that there was an error to the cluster file and also the single file
                    onefile.write('Error' + link)
            sequences.write(myfile)         #If there are no errors, it writes the whole sequence to a fasta file
            onefile.write(myfile)
            
        else:                                                           #Uniprac Ids
            link = "http://www.uniprot.org/uniparc/" + x + ".fasta"     #Same code as Uniprot Ids, just with a different URL
            try:
                myfile = urllib2.urlopen(link).read().decode("utf-8")
            except urllib2.URLError, e:
                if hasattr(e, 'code'):
                    if e.code==408:
                        print 'timeout', e.code
                    if e.code==404:
                        print 'File not found', e.code
                time.sleep(20)
                try:
                    myfile = urllib2.urlopen(link).read().decode("utf-8")
                except urllib2.URLError, e:
                    if hasattr(e, 'code'):
                        if e.code==408:
                            print 'timeout', e.code
                        if e.code==404:
                            print 'File not found', e.code
                    sequences.write('Error' + link)
                    onefile.write('Error' + link)
            sequences.write(myfile)
            onefile.write(myfile)

    sequences.close()
    title  = name + "_" + clusterID + '.fasta'
    sequences2 = open(title, 'r')       #After the fasta file is complete
    files = sequences2.read()                                       #it reads the file
    if str(files) == "":                                            #and if the file is empty, meaning that the cluster contains no sequences
        os.remove(title)                #that file is removed
    sequences2.close()

    shutil.move(title, title + "~" )

    destination= open(title, "w" )
    source= open(title + "~", "r" )
    for line in source:
        match = re.match('.*>U.*', line)
        if match:
            destination.write(">" + clusterID + "|" + line.split(">")[1])
        else:
            destination.write(line)
    source.close()
    destination.close()

idFile.close()
onefile.close() 
print("FINISH")                                                     #FIN
