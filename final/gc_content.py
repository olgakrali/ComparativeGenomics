from collections import Counter
def fastaread(filename):        ####reads the fasta file######
	sequence= ""
	with open(filename, 'r') as file:
		for line in file:
			if line.startswith(">")== False:
			 sequence+= line
	return sequence

def compute_gc(sequence): #####computes GC content########
	add=0
	newlen=0
	nonnucl=0
	for x in sequence:
		if x =='G' or x=='C':
			add=add+1
			newlen=len(sequence)
	for y in sequence:
		if y == 'N':
			nonnucl=nonnucl+1
	gccontent= add/(newlen-nonnucl)
	print (gccontent)

def dinucleotide(sequence): #####computes dinucleotide frequency #############
    nucldict={"AA","AT","AC","AG","GG","GC","GA","GT","CA","CG","CT","CC","TA","TC","TT","TG"}
    newlist=[]
    for i in range(0,len(sequence)):
        di_nucl=sequence[i:i+2]
        newlist.append(di_nucl)
    new_dict = Counter(newlist)
    keylist=[]
    for key,value in new_dict.items():
        keylist.append(key)
    keyset= set(keylist)
    newkey= (keyset).intersection(nucldict)
    for key,value in new_dict.items():
        for i in newkey:
            if key== i:
                print(key,value/len(sequence))
                
def diaminoacids(sequence): # diaminoacids frequency#
    x=["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
    y=["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
    combos = [str(i) + str(j) for i in x for j in y]
    combinations= dict(enumerate(combos,1))
    keylist=[]
    newlist=[]
    for key,value in combinations.items():
        keylist.append(value)
    nucldict=set(keylist)
    for i in range(0,len(sequence)):
        di_nucl=sequence[i:i+2]
        newlist.append(di_nucl)
    new_dict = Counter(newlist)
    newkey= (nucldict).intersection(new_dict)
    for key,value in new_dict.items():
        for i in newkey:
            if key== i:
                key,value/len(sequence)
                
def mononucleotides(sequence):
    newlist=[]
    sequence=fastaread(sequence)
    for i in range(0,len(sequence)):
        di_nucl=sequence[i:i+1]
        newlist.append(di_nucl)
    new_dict = Counter(newlist)
    for key,value in new_dict.items():
        if key == 'A':
            Acontent=value/len(sequence)
    for key,value in new_dict.items():
        if key == 'T':
            Tcontent=value/len(sequence)
    for key,value in new_dict.items():
        if key == 'C':
            Ccontent=value/len(sequence)
    for key,value in new_dict.items():
        if key == 'G':
            Gcontent=value/len(sequence)
    return (Acontent,Tcontent,Ccontent,Gcontent)
    
def monoaminoacids(sequence):
    newlist=[]
    keylist=[]
    a_a=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    for i in range(0,len(sequence)-1):
        di_nucl=sequence[i:i+1]
        newlist.append(di_nucl)
    new_dict = Counter(newlist)
    for key,value in new_dict.items():
        keylist.append(key)
    keyset= set(keylist)
    newkey= (keyset).intersection(a_a)
    for key,value in new_dict.items():
        for i in newkey:
            if key== i:
                print(key,value/len(sequence))
    

      
if __name__=="__main__":
	compute_gc(fastaread("28.fasta"))
	fastaread("28.fasta")
	dinucleotide(fastaread("28.fasta"))
	diaminoacids(fastaread("28.pfa"))
	mononucleotides("28.fasta")    
	monoaminoacids(fastaread("28.pfa"))
    






