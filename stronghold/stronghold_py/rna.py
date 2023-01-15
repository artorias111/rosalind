#!/usr/bin/python3

file=open('data/rosalind_rna.txt')

x=str(file.read())
#x='GATGGAACTTGACTACGTAAATT'
y=''
for i in x:
    if i=='T':
        y+='U'
    else:
        y+=i
print(y)
