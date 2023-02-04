#/usr/bin/python3

f=open('../data/stronghold_data/rosalind_gc.txt',r)
d={}
for i in f:
	i.strip()
	if i[0]==">":
		k=i[1:]
		d[k]=''
	else:
		d[k].append(i)
f.close()

print(d)
