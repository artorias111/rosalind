#!/usr/bin/env python3
# this code is so unoptimized holy shit - works for small fastas, not for big files
# I think reducing the time to count the lengths of so many sequences should help, more memory less time
from scripts import read_fasta_file

def failurea(s): # s is a string
    # complete this function
    # return a failure array a, where a[i] is the length of the longest proper prefix that is also a suffix
    # will a two-pointer system work?
    a=[] # the output
    l1=len(s)
    for i in range(1,l1+1):
        m=0 # current max length
        for j in range(1,i):
            # print(s[j:i])
            # print(s[:i-j])
            t2=len(s[j:i])
            if s[:i-j]==s[j:i] and t2>m: # there's a lot of length calculations going on here. I reduced it, but I still think there's a lot
                m=t2
        a.append(m)
    return a


f=read_fasta_file('../data/kmp.txt') # fasta into a dictionary
x=""
for i in f:
    x=failurea(f[i]) # x is the failure array of the first fasta entry
for i in x:
    print(i,end=" ")
