word=open("http://thinkpython2.com/code/words.txt")
string="a","c","e","f","h","l","o"
def uses_only(word,string):
     for name in word:
         if name in string:
            print(name)
               return True
     return False
uses_only("Electronics",string)

