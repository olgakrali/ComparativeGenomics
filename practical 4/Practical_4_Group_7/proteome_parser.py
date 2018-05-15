
def my_pars(filename):
    with open(filename) as f:
        orfid = []
        orfseq = []
        tempo = []
        # creates a temporary file that will contain the each protein sequence and then it will get empty
        # as long as it will find a new ORF id
        for line in f:
            if line.startswith(">./"):

                if tempo:
                    one_line = "".join(tempo)
                    orfseq.append(one_line)
                    tempo = []
                line = line.replace(">", "")
                orfid.append(line.rstrip())
            else:
                tempo.append(line.rstrip())
        del orfid[-1]   # it is a simple >./ I added on each file for taking the right results back
        return orfid, orfseq


if __name__ == "__main__":
    print('This is my function for parsing my files')

