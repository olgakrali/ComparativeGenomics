path = "parser/"

# Use the BlastParser output file to extract orfs from reference proteome (04) and the other proteomes
ref10 = []
targ10 = []
with open(path + "10parser") as f:
    for line in f:
        ref10.append(line.split(" ")[0])
        targ10.append(line.split(" ")[2])
print(len(ref10))


#find duplicates
print(set([x for x in targ10 if ref10.count(x) > 1]))

# put ORF ids together and repeat for the other pairs

prot10 = []
for re,ta in zip(ref10,targ10):
   prot10.append([re,ta])



ref12 = []
targ12 = []
with open(path + "12parser") as f:
    for line in f:
        ref12.append(line.split(" ")[0])
        targ12.append(line.split(" ")[2])
print(len(ref12))

prot12 = []
for re,ta in zip(ref12,targ12):
   prot12.append([re,ta])



ref50 = []
targ50 = []
with open(path + "50parser") as f:
    for line in f:
        ref50.append(line.split(" ")[0])
        targ50.append(line.split(" ")[2])
print(len(ref50))

prot50 = []
for re,ta in zip(ref50,targ50):
   prot50.append([re,ta])


# Identify ORFs in the reference protein 04, that are common among 10, 12 and 50 lists

unique_ref = list(set(ref10).intersection(ref12,ref50))
#print(unique_ref)

# find the ids of the ORFs of each proteome that have been paired up with an ORF from the reference proteome
list10 = []
for unique in unique_ref:
    for lines in prot10:
        if lines[0] == unique:
            list10.append(lines[1])
#print(len(list10))

list12 = []
for unique in unique_ref:
    for lines in prot12:
        if lines[0] == unique:
            list12.append(lines[1])

list50 = []
for unique in unique_ref:
    for lines in prot50:
        if lines[0] == unique:
            list50.append(lines[1])
#print(len(list50))
my_list = []
for a, b, c, d in zip(unique_ref, list10, list12,list50):
    my_list.append([a,b,c,d])
#print(my_list)

final_list = []
for final in my_list:
    final_list.append(" ".join(final))

# # Save a file in which every line will contain the ref proteome ORFs as well as the ORFs from the other 3 proteomes
# with open(path + "my_file.txt", "w") as file:
#     file.writelines(list("%s\n" % item for item in final_list))