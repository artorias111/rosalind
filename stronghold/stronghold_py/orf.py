#!/usr/bin/python3
#this problem took waaaay too long
#example run : /orf.py --fasta ../data/stronghold_data/orf.txt | grep -v "*" | sort | uniq

#argparse stuff
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--fasta', type=str, required=True)
args = parser.parse_args()

d = {
    'TCA': 'S',    # Serina
    'TCC': 'S',    # Serina
    'TCG': 'S',    # Serina
    'TCT': 'S',    # Serina
    'TTC': 'F',    # Fenilalanina
    'TTT': 'F',    # Fenilalanina
    'TTA': 'L',    # Leucina
    'TTG': 'L',    # Leucina
    'TAC': 'Y',    # Tirosina
    'TAT': 'Y',    # Tirosina
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cisteina
    'TGT': 'C',    # Cisteina
    'TGA': '*',    # Stop
    'TGG': 'W',    # Triptofano
    'CTA': 'L',    # Leucina
    'CTC': 'L',    # Leucina
    'CTG': 'L',    # Leucina
    'CTT': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCT': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAT': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGT': 'R',    # Arginina
    'ATA': 'I',    # Isoleucina
    'ATC': 'I',    # Isoleucina
    'ATT': 'I',    # Isoleucina
    'ATG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACT': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAT': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGT': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GTA': 'V',    # Valina
    'GTC': 'V',    # Valina
    'GTG': 'V',    # Valina
    'GTT': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCT': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAT': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGT': 'G'     # Glicina
}

cords_f,cords_r=[],[] #forward and reverse coordinates

i,j=0,0 #the two pointers
f=open(args.fasta)
for line in f:
	x=line.strip()
	if x[0]=='>':
		continue
	y=x[::-1]
	a=y.replace('A','t')
	aa=a.replace('T','a')
	aaa=aa.replace('G','c')
	aaaa=aaa.replace('C','g')
	y=aaaa.upper()
	l=len(x)
	while j<=l-3:
		if d[x[j:j+3]]=='*':
			while i<=j-3:
				if d[x[i:i+3]]=='M':
					if (j-i)%3==0:
						cords_f.append([i,j])
				i+=1
		i=0
		j+=1
	
	i,j=0,0
	while j<=l-3:
		if d[y[j:j+3]]=='*':
			while i<=j-3:
				if d[y[i:i+3]]=='M':
					if(j-i)%3==0:
						cords_r.append([i,j])
				i+=1
		i=0
		j+=1


def translate(s):
	st=''
	for i in range(0,len(s)-2,3):
		st=st+d[s[i:i+3]]
	return st

for i in cords_f:
	#print(x[i[0]:i[1]])
	print(translate(x[i[0]:i[1]])) 

for i in cords_r:
	print(translate(y[i[0]:i[1]]))


