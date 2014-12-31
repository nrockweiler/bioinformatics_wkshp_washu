#!/usr/bin/env python3

# python imports
import sys

# This script takes as input a nucleotide string and prints out the GC-content of that string
 

# get the DNA string from the first command line argument
dna_string = sys.argv[1]

# calculate GC content of dna_string and assign to variable gc_content
# TODO: Your code goes here

# Get the total length of the nucleotide string
nucl_length = len(dna_string)

# Make sure all of the nucleotides in the input string are capital letters before counting
dna_string.upper()

# Count the total number of Cs and Gs in the input string
c_total = dna_string.count('C')
g_total = dna_string.count('G')

# Calculate the GC content of the string
gc_content = ((c_total + g_total)/nucl_length)*100

# Print out the calculated gc content
print("The GC content is " + str(gc_content) + "%")
