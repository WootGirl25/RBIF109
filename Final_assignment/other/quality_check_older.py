#!/usr/bin/env python3

from Bio import SeqIO
import matplotlib.pyplot as plt
import os
import sys

def assess_quality(file):
    all_scores = []
    read_lengths = []
    read_count = 0

    # Parse FASTQ file
    for record in SeqIO.parse(file, 'fastq'):
        read_count += 1
        quality_scores = record.letter_annotations['phred_quality']
        all_scores.extend(quality_scores)
        read_lengths.append(len(quality_scores))
    return all_scores, read_lengths, read_count

def plot_quality(qualities, file_name, output_dir):
    plt.figure(figsize=(10, 6))
    plt.hist(qualities, bins=50, color='blue', alpha=0.7)
    plt.title(f'Quality Score Distribution for {file_name}')
    plt.xlabel('Quality Score')
    plt.ylabel('Frequency')
    plt.grid(True)

    output_file = os.path.join(output_dir, f'{file_name}_quality_distribution.png')
    plt.savefig(output_file)
    print(f"Quality distribution plot saved to {output_file}")
    plt.close()

def main():
    # assign directories to variables
    input_dir = "./inputs/"
    output_dir = "./outputs/"

    # Get FASTQ files from input directory
    fastq_files = [f for f in os.listdir(input_dir) if f.endswith('.fastq')]

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    for fastq_file in fastq_files:
        input_path = os.path.join(input_dir, fastq_file)
        qualities, read_lengths, read_count = assess_quality(input_path)

        print(f"File: {fastq_file}, Number of reads: {read_count}")
        print(f"Quality scores (first 10): {qualities[:10]}")
        print(f"Unique Quality Scores: {set(qualities)}")
        print(f"Unique Read Lengths: {set(read_lengths)}")

        # Save plot
        plot_quality(qualities, fastq_file, output_dir)

if __name__ == "__main__":
    main()
    
