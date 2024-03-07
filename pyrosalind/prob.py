#!/usr/bin/env python3
import math
# modeling random genomes - done
s,l='',''
x=[]

# Get the values from the file and store them in two variables : s and x
with open('../data/prob.txt') as f:
    i=f.readlines()
    for line in i:
        l=line.strip()
        if l[0] in 'ATGC':
            s=l # s is the string of interest
        else:
            x=[float(j) for j in l.split(' ')]

d=[] # output array
p=0 # product
char_freq={} # character frequency table, based on the GC content

for i in 'ATGC':
    char_freq[i]=0.0

for i in x:
    char_freq['G']=i/2
    char_freq['C']=char_freq['G']
    char_freq['A']=(1-i)/2
    char_freq['T']=char_freq['A']
    p=0
    for j in s:
        p=p+math.log10(char_freq[j]) # Add the log values here to prevent very small multiplication
    d.append(p)

for i in d:
    print(i,end=" ")
