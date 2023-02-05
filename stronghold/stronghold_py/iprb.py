#!/usr/bin/python3

k=24
m=22
n=28

s=k+m+n

p1=(m/s)*((1/4)*((m-1)/(s-1))+(2/4)*(n/(s-1)))
p2=(n/s)*((2/4)*(m/(s-1)) + ((n-1)/(s-1)))

p=p1+p2
p=1-p

print(p)
