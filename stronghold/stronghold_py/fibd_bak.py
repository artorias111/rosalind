#!/usr/bin/python3
#moral fibonacci rabbits
n,m=86,20
a=[1,1]
b=[1,1]
ctr=0 #counter

for i in range(n-2):
    a.append(a[-1]+a[-2])
    if ctr==m:
        b.append(b[-1]+b[-2])
    else:
        ctr+=1 #increases by one in every generation

print(a)
print(b)
print(a[-1]-sum(b))
