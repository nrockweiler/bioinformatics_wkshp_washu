#!/usr/bin/python3

# python imports
import sys

# This script takes a nucleotide ORF string in as an argument and outputs the translated protein sequence.


# define the codon table as a Python dictionary
codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L","UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S", "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*","UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W","CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L","CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P","CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q","CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R","AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M","ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T","AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K","AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R","GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V","GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A","GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E","GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

# get the DNA string from STDIN and remove any return characters
rna_string = sys.argv[1]

# translate rna_string and assign the protein to translated_prot
# TODO: Your code goes here
protein = []

position = 0
codon = ''
for nucleotide in rna_string:
    position = position + 1
    codon = codon + nucleotide

    if position == 3:
        protein.append(codon_table[codon])
        position = 0
        codon = ''

translated_prot = "".join(protein)

# Print out the translated protein sequence
print(translated_prot)
