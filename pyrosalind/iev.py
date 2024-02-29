#!/usr/bin/python3

f=open('../data/stronghold_data/iev.txt','r')
s=f.readline().strip()
a=[int(x) for x in s.split()]

x=a[0]*2+a[1]*2+a[2]*2+a[3]*1.5+a[4]
print(x)
