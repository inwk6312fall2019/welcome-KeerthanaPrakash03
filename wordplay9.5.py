word=open("http://thinkpython2.com/code/words.txt")
required="a","e","i","o","u"
def uses_all(word,required):
    for letter in required:
        if letter not in word:
           return False
    return True
uses_all(word,required)

