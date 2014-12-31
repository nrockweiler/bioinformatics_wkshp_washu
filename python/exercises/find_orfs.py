#!/usr/bin/env python3  

def reverse_complement(rna_string):
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'} 

    reverse = rna_string[::-1]

    reverse_complement = ''
    for char in reverse:
        reverse_complement = reverse_complement + complement[char]

    return reverse_complement

def identify_orfs(dna_string):
    rna_string = dna_string.replace('T','U')

    orfs_to_return = []
    
    codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L","UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*","UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W","CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L","CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P","CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q","CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R","AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M","ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T","AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K","AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R","GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V","GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A","GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E","GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

    for n in range(0,3):

        # Forward String
        position = 0
        codon = ''
        protein = ''
        for nucleotide in rna_string[n:]:
            position = position + 1
            codon = codon + nucleotide
            
            if position == 3:
                aa = codon_table[codon]
                
                # If it is a start codon or if the protein has already been started
                if aa == "M" or len(protein) > 0:
                    protein = protein + aa
                
                # If there is a stop codon and the protein is already been started
                if aa == "*" and len(protein) > 0:
                    if not protein in orfs_to_return:
                        orfs_to_return.append(protein)
                    protein = ''
                position = 0
                codon = ''

        # Reverse String                                                                                                                                                                                                             
        position = 0
        codon = ''
        protein = ''
        for nucleotide in reverse_complement(rna_string)[n:]:
            position = position + 1
            codon = codon + nucleotide

            if position == 3:
                aa = codon_table[codon]
                if aa == "M" or len(protein) > 0:
                    protein = protein + aa
                
                if aa == "*" and len(protein) > 0:
                    if not protein in orfs_to_return:
                        orfs_to_return.append(protein)
                    protein = ''

                position = 0
                codon = ''

    split_orfs = []
    for orf in orfs_to_return:
        for i,aa in enumerate(orf[1:]):
            if aa == "M":
                split_orfs.append(orf[i+1:])

    return orfs_to_return + split_orfs


print identify_orfs('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')    
