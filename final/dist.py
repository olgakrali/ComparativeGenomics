from mono import *
import math
import pandas as pd
import numpy as np
## Get the GC content for all species for the module mygc.py

A4 = mononucleotides("04.fasta")[0]
A10 = mononucleotides("10.fasta")[0]
A12 = mononucleotides("12.fasta")[0]
A28 = mononucleotides("28.fasta")[0]
A50 = mononucleotides("50.fasta")[0]

T4 = mononucleotides("04.fasta")[1]
T10 = mononucleotides("10.fasta")[1]
T12 = mononucleotides("12.fasta")[1]
T28 = mononucleotides("28.fasta")[1]
T50 = mononucleotides("50.fasta")[1]

C4 = mononucleotides("04.fasta")[2]
C10 = mononucleotides("10.fasta")[2]
C12 = mononucleotides("12.fasta")[2]
C28 = mononucleotides("28.fasta")[2]
C50 = mononucleotides("50.fasta")[2]

G4 = mononucleotides("04.fasta")[3]
G10 = mononucleotides("10.fasta")[3]
G12 = mononucleotides("12.fasta")[3]
G28 = mononucleotides("28.fasta")[3]
G50 = mononucleotides("50.fasta")[3]


def distance(baseA, baseT, baseC, baseG, baseA2, baseT2, baseC2, baseG2):
    D = round(math.sqrt((baseA-baseA2)**2 + (baseT-baseT2)**2 + (baseC-baseC2)**2+ (baseG-baseG2)**2), 3)
    return D

# Calculate the distance


four_d = [distance(A4,T4,C4,G4,A4,T4,C4,G4),
distance(A4,T4,C4,G4,A10,T10,C10,G10),
distance(A4,T4,C4,G4,A12,T12, C12, G12),
distance(A4,T4,C4,G4,A28,T28,C28,G28),
distance(A4,T4,C4,G4,A50,T50,C50,G50)]

ten_d = [distance(A10,T10,C10,G10,A4,T4,C4,G4),
distance(A10,T10,C10,G10,A10,T10,C10,G10),
distance(A10,T10,C10,G10,A12,T12, C12, G12),
distance(A10,T10,C10,G10,A28,T28,C28,G28),
distance(A10,T10,C10,G10,A50,T50,C50,G50)]


twelve_d = [distance(A12,T12,C12,G12,A4,T4,C4,G4),
distance(A12,T12,C12,G12,A10,T10,C10,G10),
distance(A12,T12,C12,G12,A12,T12, C12, G12),
distance(A12,T12,C12,G12,A28,T28,C28,G28),
distance(A12,T12,C12,G12,A50,T50,C50,G50)]

twe8_d = [distance(A28,T28,C28,G28,A4,T4,C4,G4),
distance(A28,T28,C28,G28,A10,T10,C10,G10),
distance(A28,T28,C28,G28,A12,T12, C12, G12),
distance(A28,T28,C28,G28,A28,T28,C28,G28),
distance(A28,T28,C28,G28,A50,T50,C50,G50)]


fifty_d = [distance(A50,T50,C50,G50,A4,T4,C4,G4),
distance(A50,T50,C50,G50,A10,T10,C10,G10),
distance(A50,T50,C50,G50,A12,T12, C12, G12),
distance(A50,T50,C50,G50,A28,T28,C28,G28),
distance(A50,T50,C50,G50,A50,T50,C50,G50)]


# Join them all in a matrix

matrix = np.array([four_d, ten_d, twelve_d, twe8_d, fifty_d])

# Create a pandas DataFrame and add column names

df = pd.DataFrame(matrix, columns = ["Genome4", "Genome10", "Genome12", "Genome28", "Genome50"])
print(matrix)
print(df)


# Save the dataframe in a file named distances
with open("final_dist.txt", "w") as file:
    df.to_string(file, index = False)

