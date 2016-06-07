#!/usr/bin/python                                                     

import os, re, sys

taxa_blast = open("taxa_blast_folders.txt", "r")
gene = sys.argv[1]

# The below program requires three things: 1. A list of blast folders with the blast database for each taxon, 2. A gene .fa file with  multiple sequences of a particular gene to blast against, and 3. The name of the gene. The particular gene of interest also has to be given as input by the user. Usage is simply 'python tblastn_seqs.py'.

for line in taxa_blast:
    directory = line.strip()
    #print directory
    taxon = line.split("/")[0]
    #print taxon

    os.system("cp " + gene + "_aa.fa ../" + directory)
    os.chdir("../scripts/")
    os.system("perl -pi -e 's/TAXON/" + taxon + "/g' tblastn.sh")
    os.system("perl -pi -e 's/GENE/" + gene + "/g' tblastn.sh")

    os.chdir("../" + directory)
    os.system("sh ../../../scripts/tblastn.sh")
    os.system("mview -in blast -out fasta -alignment off " + taxon + "_blast_" + gene + "_aa.out > " + taxon + "_blast_" + gene + "_aa.fa")
    os.system("mview -in blast -out fasta -alignment on " + taxon + "_blast_" + gene + "_aa.out > " + taxon + "_blast_" + gene + "_aa.aln")
    os.system("cp " + taxon + "_blast_" + gene + "_aa.out ../../../genes/")

    os.chdir("../../../scripts/")
    os.system("perl -pi -e 's/" + taxon + "/TAXON/g' tblastn.sh")
    os.system("perl -pi -e 's/" + gene + "/GENE/g' tblastn.sh")
    os.chdir("../genes")

    print taxon + " complete."

print "\nBLAST completed for " + gene + "."
    
    
