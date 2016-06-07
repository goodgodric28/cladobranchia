#!/bin/sh

source /cbcbhomes/pknut777/.profile

cd /cbcb/project2-scratch/jagood/cladobranchia_transcriptomes/Melibe_leonina/Sample_1_JG31/assembly_test/

/cbcbhomes/jagood/trinityrnaseq-2.0.6/Trinity --seqType fq --JM 96G --left 1_JG31_ATCACG_L005_R1-007_trimmed.fastq --right 1_JG31_ATCACG_L005_R2-007_trimmed.fastq --CPU 8 --bflyHeapSpaceMax 10G
