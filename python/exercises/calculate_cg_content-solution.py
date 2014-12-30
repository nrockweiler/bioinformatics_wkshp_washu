#!/usr/bin/env python                                                                                                                                                                                                                        

# python imports
import sys
 
# get the DNA string from STDIN and remove any return characters
dna_string = sys.argv[1]

# calculate CG content of dna_string and assign to variable cg_content
# TODO: Your code goes here

# Get the total length of the nucleotide string
nucl_length = len(dna_string)

# Make sure all of the nucleotides in the input string are capital letters before counting
dna_string.upper()

# Count the total number of Cs and Gs in the input string
c_total = dna_string.count('C')
g_total = dna_string.count('G')

# Calcualte the CG content of the string
cg_content = ((c_total + g_total)/float(nucl_length))*100

# Print out the calculated cg content
print("The CG content is " + str(cg_content) + "%")
