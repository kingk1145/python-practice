a=int(input("Enter your age: "))
# if statement no 1 
if(a%2==0):
    print("even number")

else:
    print("odd number")

# end of statement no 1

# if statement no 2
if (a>=18):
    print("you are eligible to vote")

elif (a<0):
    print("you are entering a invalid age")

elif(a==0):
    print("you are entering 0 which is a invalid age")

else:
    print("you are not eligible to vote")

# end of statement no 2