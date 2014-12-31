#!/usr/bin/python3

# This script trims a 14 base pair adapter and (a) writes the 
# cleaned sequences to a new file and (b) prints the length of
# each sequence to the screen.


# python imports
import sys
 
# Grab the command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the output file for writing
out = open(output_file, 'w')

# Read the input fasta file line by line
for line in open(input_file, 'r'):

    # If the line begins with a ">", the line is a header not a sequence
    if line.startswith(">"):
	    # Print the header line to the output file
        out.write(line)
    
	# Else, the line is a sequence
	else:
	    # Trim the first 14 bases from the sequence
		line = line[14:]
	    # Print the sequence line to the output file
        out.write(line)
		# Print the length of the sequence after trimming to the screen
        print(len(line))

# Close the output file
out.close()

