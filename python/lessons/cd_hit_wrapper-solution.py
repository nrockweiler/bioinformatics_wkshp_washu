#!/usr/bin/env python3

# This script takes a fasta of protein sequences and sequence identity threshold and executes a pipeline for analyzing protein sequence similarity.  The output is a scatterplot of cluster sizes in pdf format.  The steps of the pipeline are:
# Step 1: Run cd-hit on a protein sequences file.
# Step 2: Run a cd-hit tool called clstr_size_stat.pl to calculate the distribution of cluster sizes
# Step 3: Run plot_cluster_size.py to plot the distribution of cluster sizes

# Usage: cd_hit_wrapper.py <protein fasta> <identity threshold>
# <protein fasta> = path to protein fasta file
# <identity threshold> = sequence identity threshold.  A number between 0 and 1.

# python imports
import sys

# import the subprocess module
import subprocess


#
# Step 1: Run cd-hit on a protein sequences file.
#

# Grab the command line arguments
fasta = sys.argv[1]
identity_threshold = sys.argv[2] # Note: Python will treat this variable as a string not a float.  This is okay for this script because we're not doing any math with this variable.  If we were, we'd need to identity_threshold = float(sys.argv[2]).

# Run cd-hit
# The usage for running cd-hit is:
# cd-hit -i <sequence file> -o <output file> -c <identity threshold>

# Create a variable called cd_hit_fasta_output to store the output fasta filename.  Call the output file clustered_<identity_threshold>_<fasta>.  For example, if identity_threshold = 0.8 and fasta = "protein.faa", then call the file clustered_0.8_protein.faa"
cd_hit_fasta_output = "clustered_" + identity_threshold + "_" + fasta
# Use subprocess.call to run the cd-hit command
subprocess.call(["cd-hit", "-i", fasta, "-o", cd_hit_fasta_output, "-c", identity_threshold])

#
# Step 2: Run a cd-hit tool called clstr_size_stat.pl to calculate the distribution of cluster sizes
#

# The usage for running clstr_size_stat.pl is:
# clstr_size_stat.pl cluster_file
# Note 1: clstr_size_stat.pl writes to stdout.  We want to save this text to a file.  Subprocess.call can do this for us as long as we give it a file object to store the text in.
# Note 2: the cluster_file was produced in step 1.

# Create a variable called cd_hit_cluster_output to store the cluster output filename.  cd-hit called this file <cd_hit_fasta_output>.clstr.  For example, if cd_hit_fasta_output = "clustered_0.8_protein.faa", the cluster file will be "clustered_0.8_protein.faa.clstr"
cd_hit_cluster_output = cd_hit_fasta_output + ".clstr"

# Create a variable called cluster_size_output to store the cluster size output filename.  Let's call this file <cd_hit_cluster_output>.size.  For example, if cd_hit_cluster_output = clustered_0.8_protein.faa.clstr, the size file will be clustered_0.8_protein.faa.clstr.size
cluster_size_output = cd_hit_cluster_output + ".size"

# Use subprocess.call to run the clstr_size_stat.pl command
# Since we're going to save the stdout to a file, the syntax for subprocess.call is:
# subprocess.call(list_of_arguments, stdout=file_object)
# Create a file object for the output file using open.  Make sure you open the file for writing.
cluster_size_output_file_object = open(cluster_size_output, "w")
# Call subprocess
subprocess.call(["clstr_size_stat.pl", cd_hit_cluster_output], stdout=cluster_size_output_file_object)
# Close the file object.
cluster_size_output_file_object.close()


#
# Step 3: Run plot_clster_size.py to plot the distribution of cluster sizes
#

# The usage for running plot_clster_size.py is:
# python3 plot_clster_size.py <cluster size output>
# Use subprocess.call to run the Python script
subprocess.call(["python3", "plot_cluster_size.py", cluster_size_output])
