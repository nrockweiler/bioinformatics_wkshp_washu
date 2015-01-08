#!/usr/bin/python3

# This script takes in a tab separated file that has heights
# corresponding to different groups defined by the first column
# and outputs the mean and variance of the heights for each group

# At the beginning of your script, import all of the modules that your 
# script will use using the import function

# import the sys module because we will need to use sys.argv to get 
# the input filename from the command line
import sys

# import your stats.py module because we will use the functions 
# stats.calculate_mean and stats.calculate_variance
import stats


# Create a variable to store the input filename
# The input filename is the first command line argument.
# The script name and command line arguments are stored in the list sys.argv
# (You never had to define this list, Python generated it for you.)
# sys.argv[0] is the script name
# sys.argv[1] is the first command line argument
# Therefore, the input filename is the value of sys.argv[1]
input_filename = sys.argv[1]

# This script will write the mean and variance to an output file
# Before we can do any writing to that file, we need to open it
output = open("mean_athlete_heights.txt", "w") # Use "w" so we can write to the file

# Now we're reading to read from the input file
# Use a for loop to read each line of the input file
# For each of these lines, we will calculate the mean and variance of 
# the heights and then write the statistics to the output file

for line in open(input_filename, 'r'):

    # line is a variable that contains a line of the input file
    # In the first iteration of this loop, line will be the first line
    # of the input file, "Male 83 74 ..."
    # In the second iteration of this loop, line will be the second 
    # line of the input file, "Female 77 67 ..."
    
    # When Python reads a file, it reads the data in as string, so the 
    # line variable is a string. At the end of this string, there 
    # is a "newline" or "return" character (written as a "\n").  We 
    # need to remove that character because we only want the gender 
    # and the height values)

    # Strip off the "newline" character at the end of the line
    # Save the stripped line as a new variable
    line_stripped = line.rstrip()
    
    # Currently, line_stripped is a string, but we want to convert it to
    # a list because it will be easier to perform the statistics on the data
    # Since the input file uses tabs to separate the fields, we need to 
    # split line_stripped by tabs.  The character for tab is "\t".
    split_line = line_stripped.split('\t')
    # split_line is a list, e.g., ["Male", "83", "74" ... ]

    # We want to calculate the mean using stats.calculate_mean.  To use 
    # this function, we must give it a list of heights.
    # Make a new list that *only* contains height data.  The heights 
    # start at the second index and continue until the end of the list
    # To select just the mth index until the end, use this syntax: lins_name[m:]
    # (This is called a slice).
    heights = split_line[1:]
    
    # When Python reads the file, it reads the text as strings.  So 
    # heights is actually a list of strings ["83", "74" ...].  We need
    # to convert this to a list of *integers* so we can do statistics on them.

    # We convert a list of strings to a list of integers, in two steps
    # Step 1: convert the strings to integers with the function map:
    heights = map(int, heights)
    # Step 2: the map function returns something called an "iterator", 
    # not a list, so convert this iterator to a list with the function list
    heights = list(heights)

    # We now have the heights variable in a format that we can work with
    # Calculate the mean of the heights using the function calculate_mean from the stats.py module
    # To call a function in a module, the syntax is module_name.function_name
    # The input to stats.calculate_mean is a list of numbers.
    # The output of stats.caclulate_mean is the mean of that list of numbers
    mean = stats.calculate_mean(heights)
    
    # Calculate the variance using the function calculate_variance from the stats.py module
    # The input to stats.calculate_variance is a list of numbers.
    # The output of stats.calculate_variance is the variance of that list of numbers
    variance = stats.calculate_variance(heights)

    # Now we can write the statistics to the output file
    # We want to format the output like this: "The mean height of <gender> 
    # basketball players is <mean> with a variance of <variance>"
    
    # Note that the output we want to write includes the gender (e.g., 
    # male or female).  Therefore, we're going to need the gender.
    # The gender is stored in the first element of split_line
    # Create a variable for gender
    gender = split_line[0]
    
    # We're going to use string concatenation to write the sentence.  
    # To use this, we can only join together strings, not strings and 
    # numbers so we'll have to convert the mean and variance variables 
    # to strings using the function str.  For example, if the mean is 
    # 50, then str(mean) would return "50" (note the quotes).  
    # Lastly, since the function write doesn't automatically add 
    # newline characters at the end of a line, we'll have to add them 
    # ourselves by adding a "\n" string at the end.
    
    # To write to a file, the syntax is <output file object>.write(string)
    # The variable name of our output file object "output".  (We defined 
    # this variable near the beginning of this script)
    output.write("The mean height of " + gender + " basketball players is " + str(mean) + " with a variance of " + str(variance) + "\n")

# Close the output file since we're done writing to it.
output.close()
