a=int(input("Enter your age: "))
# if elif else ladder
if (a>=18):
    print("you are eligible to vote")

elif (a<0):
    print("you are entering a invalid age")

elif(a==0):
    print("you are entering 0 which is a invalid age")

else:
    print("you are not eligible to vote")
