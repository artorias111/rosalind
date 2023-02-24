#!/usr/bin/python3

f=open('../data/stronghold_data/hamm.txt','r')

x=f.readline().strip()
y=f.readline().strip()
#beautiful
h=0 #hamming distance

for i in range(len(x)):
	if x[i] != y[i]:
		h+=1

print(h)
