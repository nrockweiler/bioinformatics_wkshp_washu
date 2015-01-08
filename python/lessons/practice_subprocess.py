#!/usr/bin/python3

# Import subprocess module
import subprocess

# Run external command
subprocess.call(["cd-hit", "-i", "proteins.faa", "-o", "clustered_proteins2.faa"])

# Run external command and save the STDOUT to a file
# Open file for writing
output_file_object = open("output.txt", "w")
# Run external command
subprocess.call(["ls"], stdout=output_file_object)
# Close file object
output_file_object.close()
