import random
'''
1=snake
-1=water
0=gun
'''
computer=random.choice([-1, 0, 1])
youstr=input("Enter your choice (snake, water, gun): ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]

print(f"you chose {reversedict[you]} \ncomputer chose {reversedict[computer]}")
if(you==computer):
    print("It's a draw")

else:
    if(you==1 and computer==-1):
        print("you win!")
    elif(you==0 and computer==1):
        print("you win!")
    elif(you==-1 and computer==0):
        print("you win!")
    elif(you==-1 and computer==1):
        print("you lose!")
    elif(you==1 and computer==0):
        print("you lose!")
    elif(you==0 and computer==-1):
        print("you lose!")
    else:
        print("Something went wrong")