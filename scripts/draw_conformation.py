#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import argparse

def plot_conformation(seq, turns):
    # positions are (X, Y)
    positions = [(0, 0), (0, 1)]
    last_direction = (0, 1)

    # gather all positions based on the sequence and turns
    for move in turns:
        prev_x, prev_y = positions[-1]
        last_dir_x, last_dir_y = direction
        if move == 'R':
            direction = (last_dir_y, -last_dir_x)
        if move == 'L':
            direction = (-last_dir_y, last_dir_x)
        positions.append((prev_x + direction[0], prev_y + direction[1]))

    # shift by the mean position in both the X and Y directions



def parse_seq_file(seq_file):
    with open(seq_file) as f:

def main():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument()

    args = parser.parse_args()

    main()
