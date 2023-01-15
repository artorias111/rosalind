#!/usr/bin/python3
import math

#file=open('data/rosalind_fib.txt')
#x=str(file.read())

x='30 3'
y=x.split()
x=[]
for i in y:
    x.append(int(i))

n=x[0]
k=x[1]
i=4
s=1+k

while(i<=n):
    if(i>4):
        s=s+k+pow(k,i-3)
    else:
        s=s+k
    i+=1

print(s)
