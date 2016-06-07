import os, glob

for file in glob.glob("*.aln"):
    
    name = str(file).split(".")[0]


    print("./t_coffee -other_pg seq_reformat -in " + str(file) + " -output pir_aln > " + name + ".pir")
    os.system("./t_coffee -other_pg seq_reformat -in " + str(file) + " -output pir_aln > " + name + ".pir")

