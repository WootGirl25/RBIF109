import random

def find_lcs(seq1, seq2):
    m, n = len(seq1), len(seq2)
    
    # Create a dp 2D array (m+1)x(n+1), initialized with 0
    array = [[0] * (n + 1) for x in range(m + 1)]
    
    # Fill in array by row (m), then by column (n)
    for i in range(1, m + 1):  # Start at one so we leave a row of zeros
        for j in range(1, n + 1):  # Start at one so we leave a column of zeros
            if seq1[i - 1] == seq2[j - 1]:
                array[i][j] = 1 + array[i - 1][j - 1]
            else:
                array[i][j] = max(array[i - 1][j], array[i][j - 1])

    # Find LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif array[i - 1][j] > array[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The lcs list is constructed in reverse order, so reverse it
    lcs.reverse()
    return lcs

def generate_random_nucleotide_seq_length_5to20():
    nucleotides = ['A', 'T', 'C', 'G']
    sequence = ''
    length = random.randint(5,20)
    for x in range(length):
        index = random.randint(0,3)
        sequence += nucleotides[index]
    return sequence 


###execute###
if __name__ == "__main__":
    with open('output.txt', 'w') as output_file:  # Open the file in write mode
        for x in range(10):
            seq1 = generate_random_nucleotide_seq_length_5to20()
            seq2 = generate_random_nucleotide_seq_length_5to20()
            lcs = find_lcs(seq1, seq2)
            # Write to the output file 
            output_file.write(f'>Pair {x+1}\n')
            output_file.write(f'Sequence 1: {seq1}\n')
            output_file.write(f'Sequence 2: {seq2}\n')
            output_file.write(f'Longest Coding Sequence: {"".join(lcs)}\n\n')