#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.patches import Circle

import numpy as np
import matplotlib.pyplot as plt
import argparse

def plot_conformation(ax, seq, turns):
    ax.set_aspect(1.0)

    # positions are (X, Y)
    positions = [(0, 0), (0, 1)]
    direction = (0, 1)
    dirs = [direction]

    # gather all positions based on the sequence and turns
    for move in turns:
        prev_x, prev_y = positions[-1]
        last_dir_x, last_dir_y = direction
        if move == 'R':
            direction = (last_dir_y, -last_dir_x)
        if move == 'L':
            direction = (-last_dir_y, last_dir_x)
        positions.append((prev_x + direction[0], prev_y + direction[1]))
        dirs.append(direction)

    # get the min_x and min_y as the offset
    all_x, all_y = [*zip(*positions)]
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    aa_width = 60
    aa_height = 60

    grid = np.mgrid[0:width, 0:height]

    ax.grid()
    ax.set_axisbelow(True)

    for idx, aa, (aa_x, aa_y), direction in zip(range(len(seq)), seq, positions, dirs + [None]):
        fill = 'k' if aa is 'H' else 'w'
        edge = 'k' if aa is 'H' else '0.75'
        antifill = 'w' if aa is 'H' else 'k'
        px, py = grid[:, aa_x - min_x, aa_y - min_y]
        if direction is not None:
            ax.arrow(px, py, *direction, color = '0.5')

        ax.add_patch(Circle((px, py),
                            aa = True,
                            radius = 0.4,
                            facecolor = fill,
                            edgecolor = edge,
                            lw = 0.5,
                            linestyle = '-'))
        if idx == 0:
            ax.add_patch(Circle((px, py),
                                aa = True,
                                radius = 0.05,
                                color = '0.5',
                                ))

    ax.legend(
        (Circle((0, 0), radius = 0.1, fc = 'k', ec = 'k'), Circle((0, 0), radius = 0.1, fc = 'w', ec = '0.75')), 
        ('H', 'P')
        )

    ax.set_xlim([-1, width + 1])
    ax.set_ylim([-1, height + 1])

def parse_seq_file(seq_file):
    with open(seq_file) as f:
        seq = f.readline().strip()
        turns = f.readline().strip()

    return seq, turns

def main(seq_file):
    seq, turns = parse_seq_file(seq_file)
    fig, ax = plt.subplots()
    plot_conformation(ax, seq, turns)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('seq_file',
        help = 'file containing sequence and conformation',
        type = str
        )

    args = parser.parse_args()

    main(
        seq_file = args.seq_file
        )
