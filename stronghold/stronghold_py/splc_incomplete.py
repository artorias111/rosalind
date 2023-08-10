#!/usr/bin/python3
f=open('../data/stronghold_data/splc.txt')

c=0 #counter variable
s='' #main DNA string
l=[] # list of introns

for i in f:
	x=i.strip()
	c+=1
	if x[0]=='>':
		continue
	if c==2:
		s=x
		continue
	l.append(x)

f.close()


