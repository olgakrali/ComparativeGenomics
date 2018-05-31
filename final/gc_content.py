from collections import Counter
def fastaread(filename):        # reads in a fasta file and writes it into a continuous string #
	sequence= ""
	with open(filename, 'r') as file:
		for line in file:
			if line.startswith(">")== False:
			 sequence+= line
	return sequence

def compute_gc(sequence): # computes the GC content from the previous string, without taking into account 'N'(non-nucleotide) #
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
	return (gccontent)

def dinucleotide(sequence): # computes the di-nucleotide frequency, without taking into account 'N'(non-nucleotide) #
    nucldict={"AA","AT","AC","AG","GG","GC","GA","GT","CA","CG","CT","CC","TA","TC","TT","TG"}
    newlist=[]
    for i in range(0,(len(sequence)-1)):
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
                key,value/len(sequence)
                
def diaminoacids(sequence): # computes the di-amino acid frequency, using the predicted protein file as input #
    x=["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
    y=["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
    combos = [str(i) + str(j) for i in x for j in y]
    combinations= dict(enumerate(combos,1))
    keylist=[]
    newlist=[]
    for key,value in combinations.items():
        keylist.append(value)
    nucldict=set(keylist)
    for i in range(0,(len(sequence)-1)):
        di_nucl=sequence[i:i+2]
        newlist.append(di_nucl)
    new_dict = Counter(newlist)
    newkey= (nucldict).intersection(new_dict)
    for key,value in new_dict.items():
        for i in newkey:
            if key== i:
                key,value/len(sequence)
                
def mononucleotides(sequence): # computes the mono nucleotide frequency #
    contentA = sequence.count('A')/len(sequence)
    contentT = sequence.count('T')/len(sequence)
    contentC = sequence.count('C')/len(sequence)
    contentG = sequence.count('G')/len(sequence)
    return contentA,contentT,contentC,contentG
                
def monoaminoacids(sequence): # computes mono aminoacids 
    #print(sequence)
    a_a=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    for i in a_a:
        Contenti = sequence.count(i)/len(sequence)
        print(i, Contenti)
                      
if __name__=="__main__":
	compute_gc(fastaread("28.fasta"))
	fastaread("28.fasta")
	dinucleotide(fastaread("28.fasta"))
	diaminoacids(fastaread("04.pfa"))
	mononucleotides(fastaread("28.fasta"))
	monoaminoacids(fastaread("04.pfa"))
