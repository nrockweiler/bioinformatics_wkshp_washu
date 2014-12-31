def find_motifs(dna_string, motif):
    '''
    This function takes in two strings, a sequence and a motif, and returns a list of all of the positions in the sequence that the motif is found.
    '''

    # Determine the motif length
    motif_len = len(motif)

    # Initialize an empty list to store the motif locations
    motif_locs = []

    # Iterate through the dna_string to find the motif occurrences
    for position, nucleotide in enumerate(dna_string):
        # position is the current position in the string, e.g., 5.  Note: the first position is 0 not 1!
        # nucleotide is the character at the current position in the string, e.g., A.
	
        # Retrieve the subsequence from dna_string starting at the current position and is motif_len nucleotides long
        seq_in_position = dna_string[position:position+motif_len]

        # If the subsequence matches the motif sequence, add this position to the list
        if seq_in_position == motif:
            motif_locs.append(position+1) # The +1 is to make the position start from 1 instead of 0.

    return motif_locs


