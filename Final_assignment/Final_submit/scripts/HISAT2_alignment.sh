#!/bin/bash

####### File paths #######
reference="./inputs/Homo_sapiens.GRCh38.dna.primary_assembly.fa"
annotation="./inputs/Homo_sapiens.GRCh38.113.gtf"
forward_fastq="./inputs/sample1_R1.fastq"
reverse_fastq="./inputs/sample1_R2.fastq"

# Decide genome index path
if [ "$SKIP_INDEX" = false ]; then
    GENOME_INDEX="./index/genome_index"
else
    GENOME_INDEX="./prebuilt_index/genome_index"
fi

# Make new directories if they don't exist
mkdir -p  alignment_files outputs

# Step 1: Genome indexing (if not skipped)
if [ "$SKIP_INDEX" = false ]; then
    echo "Creating genome index..."
    mkdir -p index

    # build indexed reference
    hisat2-build $reference $GENOME_INDEX
else
    echo "Skipping genome indexing step."
fi

# Step 2: Align FASTQ files to genome index
echo "Aligning FASTQ files to genome index at $GENOME_INDEX..."
hisat2 -x $GENOME_INDEX -1 $forward_fastq -2 $reverse_fastq -S alignment_files/sample1.sam

# Step 3: Convert SAM to BAM, sort, and index
echo "Converting SAM to BAM, sorting, and indexing..."
samtools view -b alignment_files/sample1.sam > alignment_files/sample1.bam
samtools sort alignment_files/sample1.bam -o alignment_files/sample1_sorted.bam
samtools index alignment_files/sample1_sorted.bam

# Step 4: Convert BAM to BED
echo "Converting BAM to BED..."
bedtools bamtobed -i alignment_files/sample1_sorted.bam > alignment_files/sample1.bed

# Step 5: Intersect BED with annotation file
echo "Intersecting BED file with annotation..."
bedtools intersect -a alignment_files/sample1.bed -b $annotation -wa -wb > outputs/sample1_annotated.bed

# Step 6: Count reads for each gene
echo "Counting reads for each gene..."
# awk -F 'gene_name "' '{if (NF > 1) {split($2, a, ";"); print a[1]}}' outputs/sample1_annotated.bed | sort | uniq -c > outputs/gene_counts.txt
awk -F 'gene_name "' '{if (NF > 1) {split($2, a, "\""); print a[1]}}' outputs/sample1_annotated.bed | sort | uniq -c > outputs/gene_counts.txt

echo "Pipeline completed!"

