import random
class Deckofcards:
      a=list()
      b=list()
      def __init__(self):
          for key in range(4):
              for card in range(13):
                  mycards=cards(key,card)
                  Deckofcards.a.append(mycards)
      def __str__(self):
          for key in Deckofcards.a:
              Deckofcards.b.append(str(key))
          return "\n".join(Deckofcards.b)
      def shuff(self):
          self.c=[]
          self.remaining=[]
          for key in range(5):
              self.c.append(random.choice(Deckofcards.b))
          for key in self.c:
              print(key)
          return self.c
class Numberofcards:
      def __init__(self,one,two):
          suit=['Spade','Heart','Dia','Clubs']
          rank=['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
          self.suit1=suit[one]
          self.rank1=rank[two]
      def __str__(self):
          return (self.rank1,self.suit1)
d=Deckofcards()
print("The numbers of cards in a deack are:")
print(d)
numberofplayers=int(input("Enter the number of players:"))
game=dict()
for key in range(numberofplayers):
    game[key]=str(d.shuff())
print(game)

