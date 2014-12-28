#!/usr/bin/env python                                                                                                                                                                                                                        

# python imports
import sys
 
# 
input_file = sys.argv[1]
output_file = sys.argv[2]

# 
# 
out = open(output_file, 'w')
for line in open(input_file, 'r'):
    if line.startswith(">"):
        out.write(line)
    else:
        out.write(line[14:])
        print len(line[14:])

# Close the output file
out.close()

