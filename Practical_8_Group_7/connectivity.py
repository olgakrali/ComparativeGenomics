
from collections import Counter
import matplotlib.pyplot as plt

node = []   # this list will include the proteins from the left column of the file

with open("28out.txt", "r") as f:
	for line in f.readlines():
		new = line.split(" ")[0]	
		node.append(new)

# Count the number of interactions each gene has (degree)
count_set = Counter(node)  # it counts how many times a protein is found
#print(count_set)

# Extract their values from the dictionary
extract_values_list = []
for keys, values in count_set.items():
	extract_values_list.append(values)


# Get the degrees (keys) and frequency (values) of the degree in a dictionary

freq_deg_list = Counter(extract_values_list)
# print(freq_deg_list)


# Prepare lists for the scatter plot

degree_list =  []
frequency_list = []

for keys, values in freq_deg_list.items():
	degree_list.append(keys)
	frequency_list.append(values)


plt.scatter(degree_list, frequency_list)
plt.xscale("log")
plt.yscale("log")
plt.title("Degree distribution")
plt.xlabel("log10 node degree")
plt.ylabel("log10 frequency of node degree")
plt.show()



#### Average connectivity #####

# Find the total number of degrees (interactions)
# e.g. if a protein interacts with 2 other proteins the total number of interactions will be 4 (degree*2)
final = []
sum_d = 0
for num in extract_values_list:
	num2 = num*2
	sum_d = sum_d + num2
print(sum_d)

# print(len(extract_values_list))
# print(len(total_num_deg))

# Find the total number nodes 
# if a protein interacts with other 2 proteins, then the total number of interacting proteins will be 3 (degree + 1)

sum_n = 0
for num in extract_values_list:
	num2 = num + 1
	sum_n = sum_n + num2
print(sum_n)

average_connectivity = sum_d/sum_n

print(average_connectivity)



