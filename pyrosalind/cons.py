#!/usr/bin/python3
#input : a fasta file


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--fasta', '-f' ,type=str, required=True)
args = parser.parse_args()

f=open(args.fasta)
#d={'A':0,'T':0,'C':0,'G':0}

#initialize the arrays
l=0 # length of the arrays
for i in f:
	x=i.strip()
	if x[0]=='>':
		continue
	l=len(x)
	break
f.close()
A,T,G,C=[],[],[],[]

#initialize the arrays with 0s
for i in range(l):
	A.append(0)
	T.append(0)
	C.append(0)
	G.append(0)

f=open(args.fasta)
for i in f: 
	x=i.strip()
	if x[0]=='>':
		continue
	for j in range(l):
		if x[j]=='A':
			A[j]+=1
		if x[j]=='T':
			T[j]+=1
		if x[j]=='C':
			C[j]+=1
		if x[j]=='G':
			G[j]+=1
f.close()

d={'A':A,'C':C,'G':G,'T':T}

cons=''
for i in range(l):
	m=(max(A[i],T[i],C[i],G[i]))
	if m==A[i]:
		cons=cons+'A'
		continue
	if m==G[i]:
		cons=cons+'G'
		continue
	if m==T[i]:
		cons=cons+'T'
		continue
	if m==C[i]:
		cons=cons+'C'

q=open('/Users/shrirambhat/Desktop/ans.txt','w')

q.write(cons)
q.write('\n')
#print(cons)

for i in d:
	s=i+': '
	q.write(s)
	#print(i+': ',end='')
	for j in d[i]:
		s=str(j)+' '
		q.write(s)
		#print(j,end=' ')
	q.write('\n')
	#print()

q.close()
