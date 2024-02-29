#!/usr/bin/env python3

from scripts import read_fasta_file

d=read_fasta_file("../data/stronghold_data/splc.txt")

ctr=0 # counter to get the first fasta entry

# note that this solution works only if dictionary elements are stored in order. 
# This isn't the case for some older versions of python. 
ref=''
coords=[] # indices for start and end of introns
for i in d:
    if ctr==0:
        ref=d[i]
        print(ref)
        ctr+=1
        continue
    if d[i] in ref:
        start=ref.find(d[i])
        end=start+len(d[i])
        coords.append((start,end))

print(coords)

ptr=0 # current pointer
ptr=1 # test
for i in range(len(ref)):
    if ptr==1:
        print(ref[i],end="")