import sys
import os

#### assign input & output ####
input_fastq_file = sys.argv[1]
output_fasta_file = os.path.splitext(input_fastq_file)[0] + '.fa'

#### read in each line ####

with open(input_fastq_file, 'r') as fq, open(output_fasta_file, 'w') as fa:
    while True:
        identifier = fq.readline().strip()
        if not identifier:
            break # end of file
        if not identifier.startswith('@'):
            continue # skip lines that don't stat with @
        sequence = fq.readline().strip()
        fq.readline() #skip + 
        fq.readline() #skip quality score

        fa_seq_header = '>' + identifier[1:]
        fa.write(f'{fa_seq_header}\n{sequence}\n')

print(f'Conversion complete: {input_fastq_file} > {output_fasta_file}')

