#!/usr/bin/env python                                                                                                                                                                                                                        

# python imports
import sys
 
# get the DNA string from STDIN and remove any return characters
dna_string = sys.argv[1]
motif = sys.argv[2]

# translate rna_string and assign the protein to translated_prot
# TODO: Your code goes here

motif_len = len(motif)
motif_locs = []
for position, nucleotide in enumerate(dna_string):
    seq_in_position = dna_string[position:position+motif_len]

    if seq_in_position == motif:
        motif_locs.append(position+1)

# Print out the calculated cg content
print motif_locs
