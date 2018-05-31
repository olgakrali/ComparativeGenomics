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
	return (gccontent)*100

def dinucleotide(sequence): # computes the di-nucleotide frequency, without taking into account 'N'(non-nucleotide) #
    sequence = fastaread(sequence)
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
                print(key,value/(len(sequence)-1))
                
def diaminoacids(sequence): # computes the di-amino acid frequency, using the predicted protein file as input #
    sequence = fastaread(sequence)
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
                print(key,value/(len(sequence)-1))
                
def mononucleotides(sequence): # computes the mono nucleotide frequency #
    sequence = fastaread(sequence)
    contentA = sequence.count('A')/len(sequence)
    contentT = sequence.count('T')/len(sequence)
    contentC = sequence.count('C')/len(sequence)
    contentG = sequence.count('G')/len(sequence)
    return (contentA,contentT,contentC,contentG)
                
def monoaminoacids(sequence): # computes mono aminoacids 
    sequence = fastaread(sequence)
    a_a=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    for i in a_a:
        Contenti = sequence.count(i)/len(sequence)
        print(i, Contenti)
                      
if __name__=="__main__":
    fastaread("28.fasta")
    compute_gc(fastaread("28.fasta"))
    dinucleotide("28.fasta")
    diaminoacids("28.pfa")
    mononucleotides("28.fasta")
    monoaminoacids("28.pfa")
