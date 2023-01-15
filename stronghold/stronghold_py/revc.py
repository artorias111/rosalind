#!/usr/bin/python3

file=open('data/rosalind_revc.txt')

x=str(file.read())
#x='AAAACCCGGT'
y=''

for i in x:
    if i=='A':
        y+='T'
    if i=='T':
        y+='A'
    if i=='G':
        y+='C'
    if i=='C':
        y+='G'

x=y[::-1]
print(x)

