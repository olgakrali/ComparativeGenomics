# In this script we will extract information from 10_clusters file

path = "parser/"
namefile = open(path + "10_clusters.txt", "r")

namelist = []
for lines in namefile:
    lines = lines.strip()
    my_line = lines.split(" ")
    namelist.append(my_line)

# Create 10 FASTA files
for i in range(0, 10):
    my_name = namelist[i]
    output_file = path + str(i+1) + ".fasta"   #gives the name of each fasta file from 1-10
    with open(output_file, "w") as f:
        for a in my_name:
            f.writelines(a + '\n')
