myfile=open("http://thinkpython2.com/code/words.txt")
for line in myfile:
    if len(line)>20:
       word=line.strip()
       print(word)
