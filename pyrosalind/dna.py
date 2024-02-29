#!/usr/bin/python3

file=open("data/rosalind_dna.txt",'r')
#x='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
x=str(file.read())
a,t,g,c=0,0,0,0
for i in x:
    if i=='A':
        a+=1
    if i=='T':
        t+=1
    if i=='G':
        g+=1
    if i=='C':
        c+=1

print(a,c,g,t,sep=" ")
