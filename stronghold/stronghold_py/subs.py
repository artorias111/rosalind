#!/usr/bin/python3

#remember that the dna strings use a 1-based numbering (why, rosalind?, sigh)


f=open('../data/stronghold_data/subs.txt','r')

a=f.readline().strip() #read the first line and assign it to the var a
b=f.readline().strip() #read the second line and assign it to the var b

x=len(a)
y=len(b)

locs=[] #list of locations

for i in range(x):
	if a[i:i+y]==b:
		print(i+1,end=' ')
