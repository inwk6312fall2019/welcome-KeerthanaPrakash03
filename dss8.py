from __future__ import print_function, division

import sys
import string
import random


suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    
    fp = open(filename)
    skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS'): 
            break

        for word in line.rstrip().split():
            process_word(word, order)


def skip_gutenberg_header(fp):
   
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def process_word(word, order=2):
  
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
       
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
  

    start = random.choice(list(suffix_map.keys()))
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            
            random_text(n-i)
            return

        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)


def shift(t, word):
    
    return t[1:] + (word,)


def main(script, filename='158-0.txt', n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
    else: 
        process_file(filename, order)
        random_text(n)
        print()


if __name__ == '__main__':
    main(*sys.argv)
