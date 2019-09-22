from string import punctuation, whitespace

origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'

def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
    
def clean(word):
    result = ''
    for letter in word:
        if (letter in whitespace) or (letter in punctuation):
            pass
        else:
            result += letter.lower()
    return result

def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist

books = [origin, huck, frank, great, meta, sherlock, tale]

def stats():
    for book in books:
        book = open(book, 'r')
        print "Stats for %s:" % book.name
        data = [clean(word) for word in words(book)]
        book.close()
        print "  Total: %s" % len(data)
        print "  Unique: %s" % len(histogram(data))
                
stats()
