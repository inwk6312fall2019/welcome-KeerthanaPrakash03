word=open("http://thinkpython2.com/code/words.txt")
def is_abecedarian(word):
    previous=word[0]
    for c in word:
        if c<previous:
           return False
        previous=c
    return True
is_abecedarian(word)

