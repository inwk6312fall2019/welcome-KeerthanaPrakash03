def random_word(hist):

    words = []
    freqs = []
    total_freq = 0

    
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]


def main():
    hist = process_file('158-0.txt', skip_header=True)

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()
