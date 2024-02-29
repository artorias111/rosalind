#!/usr/bin/python3

# Example usage of my custom python scripts
# Convert a multiline fasta into a single line fasta to stdout (pipe it if you want it as a file ig)

from scripts import read_fasta_file

d=read_fasta_file("../data/test_data/multiline_fasta.fasta")

for i in d:
    print(">"+i+"\n"+d[i])