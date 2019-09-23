def example1():
    d=dict()
    myfile = open('https://www.gutenberg.org/files/2600/2600-0.txt')
    for line in myfile:
        word = line.strip()
    return d

def rotate_pairs(word, word_dict):
  
    for i in range(1, 14):
        rotated = rotate_letters(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


if __name__ == '__main__':
    word_dict = example1()
    for word in word_dict:
        rotate_pairs(word, word_dict)
rotate_pairs()
