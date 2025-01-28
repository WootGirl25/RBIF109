import random
import csv

def generate_random_nucleotide_seq(length):
    nucleotides = ['A', 'T', 'C', 'G']
    sequence = ''
    for x in range(length):
        index = random.randint(0,3)
        sequence += nucleotides[index]
    return sequence


def reverse_complement(sequence):
    nucleotide_dict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    rc = ''

    for i in range(len(sequence)):
        nuc = sequence[-(i+1)]
        rc += (nucleotide_dict[nuc])

    return rc

def read_tsv_to_dict(file_path):
    dic = dict()
    with open(file_path, 'r') as file:
        r = csv.reader(file, delimiter='\t')
        headers = next(r)
        for row in r:
            if row[0].startswith('#') or not row[0]:
                continue
            try: #use try so it doesnt throw error
                key = row[0] # first column "Codon"
                value = row[2] # third column "Letter"
                dic[key] = value
            except IndexError:
                continue # skip rows that don't have enough columns
    return dic

def find_3_frames(sequence):
    list = []
    for i in range(3):
        list.append(sequence[i:]) #move up one nucleotide for each following frame
    
    return list

def create_frame_list(sequence):
    forward = find_3_frames(sequence)
    reverse = find_3_frames(reverse_complement(sequence))
    frames = forward + reverse #results in a list of 6 frames
    # print(frames)

    return frames

def find_orf(seq):
    stop_codons = ['TAA', 'TAG', 'TGA']
    orfs = []
    start_positions = [] # create an empty list of ATG indicies incase there are more than one start codon before encoutering a stop

    for i in range(0, len(seq) - 2, 3):  # -2 to ensure loop doesn't go out of bounds
        codon = seq[i:i+3]
        if codon == 'ATG':
            start_positions.append(i)
        elif codon in stop_codons:
            for start_i in start_positions:
                orfs.append(seq[start_i:i])
            start_positions = []  # Reset start positions after finding a stop codon

    # If anything present in orf list, return this result.
    if orfs:
        return orfs
    else:
        return None

def translate(orf, codon_dict):
    aa_seq = []
    for i in range(0, len(orf), 3):  #each orf is a single frame, therefore traverse the sequence by x3
        codon = orf[i:i+3]
        aa_seq.append(codon_dict[codon])
    return ''.join(aa_seq)

#___________________________
#Execute

if __name__ == "__main__":
    codon_dict = read_tsv_to_dict('./codon.txt')
    with open('output.txt', 'w') as output_file:
        for i in range(10):
            dna_sequence = generate_random_nucleotide_seq(200)
            frames = create_frame_list(dna_sequence)
            output_file.write(f"Random DNA Sequence {i+1}:\n {dna_sequence}\n")
            for j, frame in enumerate(frames):
                orfs = find_orf(frame)
                if orfs:
                    for orf in orfs:
                        protein = translate(orf, codon_dict)
                        output_file.write(f"  Frame {j+1}: ORF {orf} -> Protein {protein}\n")
                else:
                    output_file.write(f"  Frame {j+1}: No ORF found\n")
            output_file.write("\n")