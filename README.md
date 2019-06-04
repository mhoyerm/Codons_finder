# Codons finder

The program searches in the codon positions 3 and 4 or 4 and 5, the sequences AADTAT or AAVATT, where D is any nucleotide except C and V is any nucleotide except T. The output file contains the genes that match the requirements of sequence and position, with its respective sequence.

Usage:
python codons_finder.py <input_file_name.fasta> <output_file_name.txt>

Input (Required): FASTA file containing genomic sequences, can be in TXT format too

Output (Required): File in TXT format containing the gene header and its sequence of six nucleotides
