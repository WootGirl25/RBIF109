#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
import os


#put all in one function so dont have to parse through fastq files more than once
#changed for efficency
def assess_quality(file):
    all_scores = []
    read_lengths = []
    gc_contents = []
    read_count = 0

    # Parse FASTQ file
    for record in SeqIO.parse(file, 'fastq'):
        read_count += 1

        # list of quality scores
        quality_scores = record.letter_annotations['phred_quality']
        all_scores.extend(quality_scores)

        # list of read lengths
        read_lengths.append(len(quality_scores))

        # list of calculated GC content
        gc_content = GC(record.seq)
        gc_contents.append(gc_content)

    return all_scores, read_lengths, gc_contents, read_count

def plot_quality(qualities, file_name, output_dir):
    plt.figure(figsize=(10, 6))
    plt.hist(qualities, bins=50, color='blue', alpha=0.7)
    plt.title(f'Quality Score Distribution for {os.path.splitext(file_name)[0]}')
    plt.xlabel('Quality Score')
    plt.ylabel('Frequency')
    plt.grid(True)

    output_file = os.path.join(output_dir, f'{os.path.splitext(file_name)[0]}_quality_distribution.png')
    plt.savefig(output_file)
    print(f"Quality distribution plot saved to {output_file}")
    plt.close()

def plot_gc_content(gc_contents, file_name, output_dir):
    plt.figure(figsize=(10, 6))
    plt.hist(gc_contents, bins=50, color='green', alpha=0.7)
    plt.title(f'GC Content Distribution for {os.path.splitext(file_name)[0]}')
    plt.xlabel('GC Content (%)')
    plt.ylabel('Frequency')
    plt.grid(True)

    output_file = os.path.join(output_dir, f'{os.path.splitext(file_name)[0]}_gc_content_distribution.png')
    plt.savefig(output_file)
    print(f'GC content plot saved to {output_file}')
    plt.close()

def main():
    # Assign directories to variables
    input_dir = "./inputs/"
    output_dir = "./outputs/"

    # Get FASTQ files from input directory
    fastq_files = [f for f in os.listdir(input_dir) if f.endswith('.fastq')]

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    for fastq_file in fastq_files:
        input_path = os.path.join(input_dir, fastq_file)

        # Assess quality and calculate GC content
        qualities, read_lengths, gc_contents, read_count = assess_quality(input_path)

        # Print metrics
        print(f"File: {fastq_file}, Number of reads: {read_count}")
        print(f"Quality scores (first 10): {qualities[:10]}")
        print(f"Unique Quality Scores: {set(qualities)}")
        print(f"Unique Read Lengths: {set(read_lengths)}")

        # Save plots
        plot_quality(qualities, fastq_file, output_dir)
        plot_gc_content(gc_contents, fastq_file, output_dir)

if __name__ == "__main__":
    main()
