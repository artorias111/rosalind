#!/usr/bin/python3
import math

#file=open('data/stronghold_data/rosalind_fib.txt'i,'r')
#x=str(file.read())

x='36 3'
y=x.split()
x=[]
for i in y:
    x.append(int(i))

n=x[0]
k=x[1]
print(n,k)

def fib(n,k):
	if n==1:
		return 1
	if n==2:
		return 1
	
	return fib(n-1,k) + k*fib(n-2,k)	

print(fib(n,k))
