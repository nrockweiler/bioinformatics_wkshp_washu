#!/usr/bin/env python

# This script takes in a tab separated file that has heights
# corresonding to different groups definied by the first column
# and outputs the mean and variance of the heights for each group


# python imports
import sys

# import user defined module
import heights_analysis as h 

## TODO: Your code goes here

# open an output file for writing
output = open("mean_athlete_heights.txt", 'w')

# read in each line of the file from the command line
for line in open(sys.argv[1], 'r'):
    split_line = line.rstrip().split('\t')

    group = split_line[0]
    heights = split_line[1:]

    
    mean  = h.calculate_mean(heights)
    var = h.calculate_variance(heights)

    print("The mean height of " + group + " basketball players is " + str(mean) + " with a variance of " + str(var))
