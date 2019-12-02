#!/usr/bin/env python

import numpy as np
import argparse

def parse_fasta(fasta_file):
    with open(fasta_file) as f:
        for line in f:
            if line.startswith('>'):
                seq = f.readline().strip()
                print(seq)

def main(fasta_file):
    sequences = parse_fasta(fasta_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('fasta_file',
        help = 'path to fasta file to parse'
        )

    args = parser.parse_args()

    main()

with open
