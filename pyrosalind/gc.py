#!/usr/bin/python3

gc=0 #gc sum
l=1 #total length 
gcl=0
curr=''#current highest fasta header
m=0

#print the sequence with the highest gc/l (gcl)

#store the fasta file as a dictionary

k,v=[],[]

with open('/Users/shriram/code/rosalind/stronghold/data/stronghold_data/gc.txt') as f:
	for x in f:
		x=x.strip()
		if x[0]=='>':
			v.append(gc/l)
			gc,l=0,0
			k.append(x[1:])
		else:
			for i in x:
				l+=1
				if i=="G" or i=="C":
					gc+=1
v.append(gc/l)
v.pop(0)

print(k[v.index(max(v))],'\n',100*max(v))
