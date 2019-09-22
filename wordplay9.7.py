def three_consecutive(s):
    i=0
    count=0
    while i<len(s)-1:
          if s[i]==s[i+1]:
             count+=1
             i+=2
             if count==3:
                print("Found!")
          else:
             count=0
             i+=1
    return ("Not Found!!!",count)
s=input("Enter any string with 3 pairs of consecutive letters:")
print(three_consecutive(s))

