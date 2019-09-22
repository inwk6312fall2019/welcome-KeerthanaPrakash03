
import string, time

def del_punctuation(item):
    
    punctuation = string.punctuation
    for c in item:
        if c in punctuation:
            item = item.replace(c, '')
    return item 

def break_into_words():
  
    book = open('tsawyer.txt')
    words_list = []
    for line in book:
        for item in line.split():
            item = del_punctuation(item)
            item = item.lower()
            #print(item)
            words_list.append(item)
    return words_list

def create_dict():
    
    words_list = break_into_words()
    dictionary = {}
    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
        
    dictionary.pop('', None)  
    return dictionary

def words_list():
  
    res = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        res.append(word)
    return res

def avoids():
    dictionary = words_list()
    book = create_dict()
    count = 0
    for i in book:
        if i not in dictionary:
            print(i)
            count += 1
    print()
    print('In total there are {} words which are not in words.txt file'.format(count))

   
start_time = time.time()
avoids()
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time
