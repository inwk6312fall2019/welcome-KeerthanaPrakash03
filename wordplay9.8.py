from _future_ import print_function,division
def is_triple_double(word):
    i=0
    count=0
    while i<len(word)-1:
          if word[i]==word[i+1]:
             count=count+1
             if count==3:
                return True
             i=i+2
          else:
             i=i+1-2*count
             count=0
    return False
def find_triple_double():
    myfile=open("http://thinkpython2.com/code/words.txt")
    for line in myfile:
        word=line.strip()
        if is_triple_double(word):
           print(word)

print("The words in the list  are :")
print("Three consecutive double letters are:")
find_triple_double()
