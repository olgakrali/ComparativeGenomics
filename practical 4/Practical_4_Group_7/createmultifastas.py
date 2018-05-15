from proteome_parser import *
path = "parser/"

# List of ORF ids and sequences for each pfa file

id4, sequence4 = my_pars("04.fa.txt.pfa")

id10, sequence10 = my_pars("10.fa.txt.pfa")

id12, sequence12 = my_pars("12.fa.txt.pfa")

id50, sequence50 = my_pars("50.fa.txt.pfa")

#### Link the orf ids to their sequences (draw information from the pfa files)

# Load the ORF id names file
namefile = open(path + "my_file.txt", "r")

namelist = []
for lines in namefile:
    lines = lines.strip()
    my_line = lines.split(" ")
    namelist.append(my_line)
#print(len(namelist))

names4 = []

for n in namelist:
    names4.append(n[0])
#print(names)

names10 = []

for n in namelist:
    names10.append(n[1])

names12 = []

for n in namelist:
    names12.append(n[2])

names50 = []

for n in namelist:
    names50.append(n[3])

# Proteome 4 (reference)



proteome4 = []

for name in names4:
    for ids, seq in zip(id4, sequence4):
        if name == ids:
            ids = ">" + ids  # add the fasta symbol
            proteome4.append([ids,seq])

proteome10 = []

for name in names10:
    for ids, seq in zip(id10, sequence10):
        if name == ids:
            ids = ">" + ids
            proteome10.append([ids,seq])
#print(proteome10[15])


proteome12 = []

for name in names12:
    for ids, seq in zip(id12, sequence12):
        if name == ids:
            ids = ">" + ids
            proteome12.append([ids,seq])
#print(proteome12[15])

proteome50 = []


for name in names50:
    for ids, seq in zip(id50, sequence50):
        if name == ids:
            ids = ">" + ids
            proteome50.append([ids,seq])
#print(proteome50[25])



#### concatenate them all together
alist = []
for a,b,c,d in zip(proteome4, proteome10, proteome12, proteome50):
    alist.append([a,b,c,d])
# put all ids and sequences in the same list for each reference ORF
final_list = []
for final in alist:
    finale = []
    for fin in final:
        finale.extend(fin)
    final_list.append(finale)

#Prepare for make it in a form to save it

savinglist = []
for sav in final_list:
    savinglist.append(" ".join(sav))

# Save a file in which every line will contain the ref proteome ORFs as well as the ORFs from the other 3 proteomes
with open(path + "multiseq.txt", "w") as file:
    file.writelines(list("%s\n" % item for item in savinglist))