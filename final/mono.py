from collections import Counter
def fastaread(filename):        ####reads the fasta file######
	sequence= ""
	with open(filename, 'r') as file:
		for line in file:
			if line.startswith(">")== False:
			 sequence+= line
	return sequence
def mononucleotides(sequence):
    newlist=[]
    sequence=fastaread(sequence)
    for i in range(0,len(sequence)-1):
        di_nucl=sequence[i:i+1]
        newlist.append(di_nucl)
    new_dict = Counter(newlist)
    for key,value in new_dict.items():
        if key == 'A':
            Acontent=value/(len(sequence)-1)
    for key,value in new_dict.items():
        if key == 'T':
            Tcontent=value/(len(sequence)-1)
    for key,value in new_dict.items():
        if key == 'C':
            Ccontent=value/(len(sequence)-1)
    for key,value in new_dict.items():
        if key == 'G':
            Gcontent=value/(len(sequence)-1)
    return Acontent,Tcontent,Ccontent,Gcontent
    
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
                print(key,value/(len(sequence)-1))
    

if __name__=="__main__":
    mononucleotides("04.fasta")    
    monoaminoacids(fastaread("04.pfa"))
