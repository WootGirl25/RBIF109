RBIF109 Assignment 1
Author: Laura Wooten

GOAL
The goal of this project is to implement an in silico DNA to protein translator. The translator considers all six reading frames. The open reading frame (ORF) is defined by the presence of both a start codon (ATG) and a stop codon (TAA, TAG, or TGA). Truncated proteins with missing start or stop codons are not translated. Testing of the script will be conducted with 10 randomly generated sequences of 200bp in length. Because of the length used for testing, the gene will not be defined by a minimum number of codons in this script. Results will be compared to the Expasy Translate tool, and a discussion is provided at the end of this document.


Input files:
codon.txt

Output files:
output.txt

Requirements:
Python3 must be installed on your operating system.

Execute the following script as depicted within the same directory as the input files.
python3 in_silico_DNA_to_protein_translator.py

Steps within the script:
1. The script will read in the file codon.txt and create a dictionary of codons and their corresponding amino acid.
2. The script will generate 10 random DNA sequences of 200bp in length.
3. For each sequence the script will then:
    a. Find the reverse complement of the sequence.
    b. Find the 3 reading frames for each strand, returning a list of all 6 reading frames.
    For each frame:
        i. Determine if open reading frame(s) are present. By traversing the reading frame in intervals of 3 bases, the presence of a start or stop codon is specific to that frame.
        ii. If ORF(s) are found, the sequence is translated using the codon dictionary.
4. The results are outputted to output.txt and contains:
    a. The randomly generated DNA sequence
    b. The DNA sequence of the ORF if found.
        NOTE: If more than one ORF is found, or if a ORF contains more than one start codon before a stop codon is present, the isoforms will be listed on separate lines.
    c. The translated protein sequence.

Additional files and discussion:
The file tested_output.txt has been included to show the execution of the script and to compare to the screenshots from the Expasy Translate tool (https://web.expasy.org/translate/). Screenshots of the first two translated sequences by Expasy have been included and are named Expasy_seq1.png and Expasy_seq2.png. The results between the two are almost completely consistent, with the following exceptions:
1. The Expasy Translate tool will return an ORF if there is no stop codon present before reaching the end of the sequence. As this script defines a gene to have a stop codon, this results in fewer ORFs found in the script than the tool.
2. When two start codons are present before a stop codon is encountered, the Expasy Translate tool refers to this as a single ORF. This script considers that due to mRNA folding, ribosome specificity, or other factors, this may confer in two separate protein isoforms of the gene. As such, both are listed in the output for that specific frame. 

While this script is a great introductory in silico DNA to protein translator, there are some caveats, primarily being that the length of the ORF is not being considered. There are multiple examples in the tested_output.txt file that result in a single amino acid protein product - Methionine. In reality this, and other sequences of only a few amino acids in length, would not be an appropriate marker of a true ORF. 
