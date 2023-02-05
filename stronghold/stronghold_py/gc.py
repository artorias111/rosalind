#!/usr/bin/python3

f=open('../data/stronghold_data/rosalind_gc.txt','r')

l,gc=0,0 #length, gc count and gc/l ratio
m,m2=0,0 #max running gc content
h='' #header with the highest gc content
tmp=''

for i in f:
	x=i.strip()
	if x[0]==">":
		m2=m
		tmp=x
		l,gc=0,0
		continue

	for j in x:
		if j=='G' or j=='C':
			gc+=1
		l+=1

	gcl=gc/l	
	if gcl > m :
		m=gcl
		h=tmp
f.close()

print(h[1:])
print(m2)
