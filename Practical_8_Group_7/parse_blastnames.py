with open("pract8", "r") as f:
    for line in f.readlines():
        if line.startswith("./28"):
            line2 = line.strip()
            line2 = line2.split("\t")[1]   #split the line and keep the gene and organism name
            line3 = line2.split("|")[2].split("_")[0]  # split organism and gene name to get only gene name
            print(line3)
            with open("genes.txt", "a") as myfile:
                myfile.writelines(line3 + " ")
