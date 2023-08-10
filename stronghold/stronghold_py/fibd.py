#!/usr/bin/python3
#mortal fibonacci rabbits
n,m=10,3
a=[1,1]
ctr=2 #counter
j=0

for i in range(n-2):
    if ctr==m:
        a.append(a[-1]+a[-2]-a[j])
        j+=1
    else:
        a.append(a[-1]+a[-2])
        ctr+=1 #increases by one in every generation
print(a)
