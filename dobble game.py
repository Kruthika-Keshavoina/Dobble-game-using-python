print("Look at the lists and find the common letter:")
import string
import random
l=list(string.ascii_letters)
print(l)
c=1
while c==1:
 ss=random.choice(l)
 l.remove(ss)
 card1=[0]*5
 card2=[0]*5
 pos1=random.randint(0,4)
 pos2=random.randint(0,4)
 if(pos1==pos2):
    card1[pos1]=ss
    card2[pos1]=ss
 else:
    card1[pos1]=ss
    card2[pos2]=ss
    card1[pos2]=random.choice(l)
    l.remove(card1[pos2])
    card2[pos1]=random.choice(l)
    l.remove(card2[pos1])
 for i in range(5):
    if(i!=pos1 and i!=pos2):
        a=random.choice(l)
        l.remove(a)
        b=random.choice(l)
        l.remove(b)
        card1[i]=a
        card2[i]=b
 print(card1)
 print(card2)
 n=input("Enter the matching letter:")
 if(n==ss):
    print("Correct")
 else:
    print("wrong")
 c=int(input("Enter 0 to exit or 1 to continue:"))
if c==0:
       print("Thank you for playing")
