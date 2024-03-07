#!/usr/bin/python3

def read_fasta_file(filename):
# Takes a fasta file and returns a dictionary with key:value as header:sequence
# Warning : The sequence is returned as a single string, be wary of memory usage
# Works with both single line and multiline fasta
    d={} # output dictionary
    with open (filename,'r') as f :
        for line in f :
            l=line.strip()
            if l=="":
                continue
            if l[0]==">":
                d[l[1:]]=""
                tmp=l[1:]
                continue
            d[tmp]+=l
    return d

if __name__ == "__main__" :
    print("this python script contains a few functions that used multiple times in rosalind projects")

    # Tests
    print(read_fasta_file("../data/grph.txt"))
