#!/usr/bin/env python                                                                                                                                                                                                                        

# python imports
import sys
 
# get the DNA string from STDIN and remove any return characters
dna_string = sys.argv[1]

# calculate CG content of dna_string and assign to variable cg_content
# TODO: Your code goes here

# Get the total length of the nucleotide string
nucl_length = len(dna_string)

dna_string.capitalize()

c_total = dna_string.count('C')
g_total = dna_string.count('G')

cg_content = ((c_total + g_total)/float(nucl_length))*100

# Print out the calculated cg content
print "The CG content is " + str(cg_content) + "%"
