#!/bin/bash


####### download STAR #####
# curl -L -o STAR-2.7.11b.tar.gz https://github.com/alexdobin/STAR/archive/2.7.11b.tar.gz
# tar -xzf STAR-2.7.11b.tar.gz
# cd STAR-2.7.11b/source
# make STARforMacStatic CXX=/opt/homebrew/Cellar/gcc/14.2.0_1/bin/g++-14
# mv STAR ~/Documents/venvS/PyVenv109/bin/


####### unzip ref files ###############
#gunzip ./Inputs/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
#gunzip ./Inputs/Homo_sapiens.GRCh38.113.gtf.gz

reference="./Inputs/Homo_sapiens.GRCh38.dna.primary_assembly.fa"
annotation="./Inputs/Homo_sapiens.GRCh38.113.gtf"
forward_fastq="./Inputs/sample1_R1.fastq"
reverse_fastq="./Inputs/sample1_R2.fastq"

#index ref using star
#mkdir index #so dont have to copy ref file.
~/Documents/venvS/PyVenv109/bin/STAR --runThreadN 4 --runMode genomeGenerate --genomeDir ./index --genomeFastaFiles $reference --sjdbGTFfile $annotation --sjdbOverhang 149 --limitGenomeGenerateRAM 16000000000

#align paired end reads with ref
#STAR --runThreadN 4 --genomeDir ./index/<indexed_ref_file> --readFilesIn $forward_fastq $reverse_fastq --outFileNamePrefix ./sample1 --outSAMtype BAM SortedByCoordinate
## this should result in a BAM file. we can change to result as sam if we want to check sam file

#bedtools to convert bam > bed

#bed intersect with annotation track > results in a bed file listing the "intersections"/genes.

#count reads for each gene
#awk '{print $4}' intersected.bed | sort | uniq -c > gene_counts.txt

