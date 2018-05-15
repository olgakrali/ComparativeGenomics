from proteome_parser import *
import os
path = "metagene/"
fnames = os.listdir(path)
#par
id1, sequence1 = my_pars(path + "1.fasta.txt")

multi_clust = []
for fname in fnames:
    ids, sequence = my_pars(path + fname)
    my_list  = []
    for id,seq in zip(ids, sequence):
        my_list.extend([id, seq])
    multi_clust.append(my_list)
print(multi_clust)

# Put the sequences from each genome together in separate lists
seq4 = []
for n in multi_clust:
    seq4.extend(n[1])
print(len(seq4))
string4 = "".join(seq4)

seq10 = []
for n in multi_clust:
    seq10.extend(n[3])
print(len(seq10))
string10 = "".join(seq10)

seq12 = []
for n in multi_clust:
    seq12.extend(n[5])
print(len(seq12))
string12 = "".join(seq12)

seq50 = []
for n in multi_clust:
    seq50.extend(n[7])
print(len(seq50))
string50 = "".join(seq50)


# Save a file in which every line will contain each organisms sequences that direved from alignment
with open("metagene.fasta", "w") as file:
    file.write('>04' + '\n')
    file.write(string4 + '\n')
    file.write('>10' + '\n')
    file.write(string10 + '\n')
    file.write('>12' + '\n')
    file.write(string12 + '\n')
    file.write('>50' + '\n')
    file.write(string50 + '\n')



