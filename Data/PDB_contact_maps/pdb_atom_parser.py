import sys
filename = sys.argv[-1]

data_list = []

with open(filename, 'r') as datafile:
	for line in datafile:
		data_list.append(line)

print(len(data_list))


atom = []
num = []
name = []
aa = []
chain = []
pos = []
xca = []
yca = []
zca = []
occupancy = []
bfactor = []

for x in range(1,len(data_list)):
	atom.append(data_list[x][0:6].strip())
	num.append(data_list[x][7:11].strip())
	name.append(data_list[x][13:17].strip())
	aa.append(data_list[x][17:21].strip())
	chain.append(data_list[x][21:22].strip())
	pos.append(data_list[x][22:27])
	xca.append(data_list[x][32:39].strip())
	yca.append(data_list[x][39:47].strip())
	zca.append(data_list[x][47:55].strip())
	occupancy.append(data_list[x][56:61].strip())
	bfactor.append(data_list[x][61:67].strip())

text_file = open("parsed_"+filename[0:len(filename)-4]+".tsv", "w")
text_file.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % ("atom","num","name","aa","chain","position","xca","yca","zca","occupancy","bfactor"))

for y in range(0,len(num)):
	text_file.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (atom[y],num[y],name[y],aa[y],chain[y],pos[y],xca[y],yca[y],zca[y],occupancy[y],bfactor[y]))
text_file.close()