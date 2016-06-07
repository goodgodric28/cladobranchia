import sys, re
import xml.etree.ElementTree as ET

# Finds all Uniprot Ids associated with the NCBI Ids found by ncbiIdLookUp
# in the originally downloaded xml file. If there was an entry that did not
# contatin a Uniprot Id, the Uniparc Id was taken instead
# Takes two inputs, the first being the xml file and the second being the organism specific ids

if (len(sys.argv)) < 3:
    #thing1 = input("Please input XML file name in quotations ---> ")
    #thing2 = input("Please input name of file with only Microsporidia NCBI Ids in quotations ---> ")
    print("Description: Finds all Uniprot Ids associated with the NCBI Ids found by ncbiIdLookUp in the originally downloaded xml file. If there was an entry that did notcontatin a Uniprot Id, the Uniparc Id is taken instead.")
    print("Error\nUsage: Please input XML file name followed by name of file with only Microsporidia NCBI Ids after program name \nExample: python26 taxonIdFinder.py myxml.xml myxml_Microsporidia_NCBI_Ids.txt")
    sys.exit()
else:
    thing1 = sys.argv[1]
    thing2 = sys.argv[2]
    

name = thing1.split(".")[0]
tree = ET.parse(thing1)
print("CREATED TREE")
root = tree.getroot()
ncbi = open(thing2, 'r').read().strip().split('\n')
accessions = open(name + "_Uniprot_Uniparc_Ids.txt", 'w')
uid = open("uid.txt", 'w')
nid = open("nid.txt", 'w')
cid = open("cid.txt", 'w')
currentCluster = -1
cluster = 0
num = 0
for cluster in range(0, len(root.getchildren())):
    clusterID = root[cluster].attrib['id']
    for member in range(4, 4 + int(root[cluster][1].attrib['value'])):
        currentNCBI = ''
        currentUniProt = ''
        currentUniParc = ''
        for property in root[cluster][member][0].getiterator('{http://uniprot.org/uniref}property'):
            if property.attrib['type']=='NCBI taxonomy':
                currentNCBI = property.attrib['value']
            if root[cluster][member][0].attrib['type']=='UniProtKB ID':
                currentUniProt = root[cluster][member][0].attrib['id']
            if root[cluster][member][0].attrib['type']=='UniParc ID':
                currentUniParc = root[cluster][member][0].attrib['id']
        if ncbi.count(currentNCBI)>0:
            num = num+1
            if currentCluster!=cluster:
                currentCluster = cluster
                if cluster!=0:
                    accessions.write('\n')
                accessions.write(clusterID + ' ')
            if currentUniProt!='':
                accessions.write(currentUniProt + ' ')
                uid.write(currentUniProt + '\n')
                nid.write(currentNCBI + '\n')
                cid.write(clusterID[clusterID.rfind('_')+1:] + '\n')
            elif currentUniParc!='':
                accessions.write(currentUniParc + ' ')
                uid.write(currentUniParc + '\n')
                nid.write(currentNCBI + '\n')
                cid.write(clusterID[clusterID.rfind('_')+1:] + '\n')
            else:
                print("WHAT")
accessions.close()
uid.close()
nid.close()
cid.close()
print(num)
