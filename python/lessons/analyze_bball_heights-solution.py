#!/usr/bin/python3

# This script takes in a tab separated file that has heights
# corresponding to different groups defined by the first column
# and outputs the mean and variance of the heights for each group


# python imports
import sys

# import user defined module
import stats 

## TODO: Your code goes here

# open an output file for writing
output = open("mean_athlete_heights.txt", 'w')

# read in each line of the file from the command line
for line in open(sys.argv[1], 'r'):
    # Remove the whitespace at the end of the line
	line = line.rstrip()
	
	# Split the line by tab characters
    split_line = line.split('\t')

	# Grab the group (the first column)
    group = split_line[0]
	# Grab the heights (the second column until the end of the line)
    heights = split_line[1:]
	
	# When Python reads the file, it reads the text as strings.  Therefore, convert the list of heights from strings to integers
	heights = list(map(int, heights))

    # Calculate the mean from the stats.py module
    mean  = stats.calculate_mean(heights)
	
	# Calculate the variance from the stats.py module
    var = stats.calculate_variance(heights)

	# Print the statistics to the file.  Remember to add the final return character and convert the statistics to strings for priting.
    output.write("The mean height of " + group + " basketball players is " + str(mean) + " with a variance of " + str(var) + "\n")

# Close the output file
output.close()