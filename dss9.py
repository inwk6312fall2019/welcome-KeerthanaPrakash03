from __future__ import print_function, division

import sys

import matplotlib.pyplot as plt

from analyze_book1 import process_file


def rank_freq(hist):
    
    
    freqs = list(hist.values())
    freqs.sort(reverse=True)

   
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    
    for r, f in rank_freq(hist):
        print(r, f)


def plot_ranks(hist, scale='log'):
    
    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main(script, filename='emma.txt', flag='plot'):
    hist = process_file(filename, skip_header=True)

    
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Usage: zipf.py filename [print|plot]')


if __name__ == '__main__':
    main(*sys.argv)
