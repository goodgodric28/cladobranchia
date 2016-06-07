#!/usr/bin/python                                                     

import os, re, sys

taxa_blast = open("taxa_blast_folders.txt", "r")
gene = sys.argv[1]

# The below program requires three things: 1. A list of blast folders with the blast database for each taxon, 2. A gene .fa file with  multiple sequences of a particular gene to blast against, and 3. The name of the gene. The particular gene of interest also has to be given as input by the user. Usage is simply 'python blastn_seqs.py'.

for line in taxa_blast:
    directory = line.strip()
    #print directory
    taxon = line.split("/")[0]
    #print taxon

    os.system("cp " + gene + ".fa ../" + directory)
    os.chdir("../scripts/")
    os.system("perl -pi -e 's/TAXON/" + taxon + "/g' blastn.sh")
    os.system("perl -pi -e 's/GENE/" + gene + "/g' blastn.sh")

    os.chdir("../" + directory)
    os.system("sh ../../../scripts/blastn.sh")
    os.system("mview -in blast -out fasta -alignment off " + taxon + "_blast_" + gene + ".out > " + taxon + "_blast_" + gene + ".fa")
    os.system("mview -in blast -out fasta -alignment on " + taxon + "_blast_" + gene + ".out > " + taxon + "_blast_" + gene + ".aln")
    os.system("cp " + taxon + "_blast_28S.out ../../../genes/")

    os.chdir("../../../scripts/")
    os.system("perl -pi -e 's/" + taxon + "/TAXON/g' blastn.sh")
    os.system("perl -pi -e 's/" + gene + "/GENE/g' blastn.sh")
    os.chdir("../genes")

    print taxon + " complete."

print "\nBLAST completed for " + gene + "."
    
    
