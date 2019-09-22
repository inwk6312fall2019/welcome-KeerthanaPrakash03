word=open("http://thinkpython2.com/code/words.txt")
def letter(word):
    for char in word:
        if char=='e':
           return False
    return True
