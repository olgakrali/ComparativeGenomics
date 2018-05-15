path = "parser/"
namefile = open(path + "multiseq.txt", "r")

namelist = []
for lines in namefile:
    lines = lines.strip()
    my_line = lines.split(" ")
    namelist.append(my_line)

# pick 10 clusters
my_10_clust = namelist[50:60]

final_list = []
for clus in my_10_clust:
    final_list.append(" ".join(clus))
print(final_list)

with open(path + "10_clusters.txt", "w") as f:
    f.writelines(list("%s\n" % item for item in final_list))