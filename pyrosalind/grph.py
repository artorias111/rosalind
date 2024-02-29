#!/usr/bin/python3
import scripts

# read the fasta file
d=scripts.read_fasta_file("../data/stronghold_data/rosalind_grph.txt")

# Set overlap length
o=3
l=[]
#print(d)

for i in d:
    for j in d:
        #print(d[i][:o])
        #print(d[j][-o:])
        if d[i][:o]==d[j][-o:]:
            l.append((j,i))

f=open('out.txt','w')
s=''
for i in l:
    s=i[0]+" "+i[1]+'\n'
    f.write(s)
    s=''
    