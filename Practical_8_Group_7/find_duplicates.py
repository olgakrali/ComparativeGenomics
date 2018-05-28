# Here we will remove duplicates from experiment text file
uniques = []
with open("experiments.txt", "r") as f:

    for line in f.readlines():
        line2 = line.strip()
        line3 = line2.split(" ")
        myset = set(line3)
        myset2 = list(myset)
        uniques.append(myset2)

# In part two we will look through overlapping sequences, and which experiment has the most overlap
genes = []
with open("genes.txt", "r") as myfile:
    for line in myfile.readlines():
        line2 = line.strip()
        line2 = line2.split(" ")
        genes.append(line2)

#print(genes)

for gene in genes:
    i = 0       # provide a counter, so that we find the experiment with the most overlap
    for uni in uniques:
        match = set(gene).intersection(uni)
        i += 1
        print(i, match)
# In our list is experiment number 30 (4 common names), and 33 (3 common names)