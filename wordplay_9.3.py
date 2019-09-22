myfile=open("https://thinkpython2.com/code/words.txt")
word=myfile.strip()
forbidden="n","h","o","f","v"
def avoids(word,forbidden):
    for letters in word:
        if letters in forbidden:
           return True
    return False
answer=avoids(word,forbidden)
print(answer)


