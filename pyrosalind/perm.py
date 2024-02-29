#!/usr/bin/python3


def factorial(a): #Number of loop iterations
	if a==1:
		return 1
	return a*factorial(a-1)


n=int(input('Enter your number sir\n'))
x=[i for i in range(1,n+1)]
print(x)

for i in range(factorial(n)):
	
