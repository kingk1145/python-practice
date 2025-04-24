try:
    a=int(input("Hey enter a number: "))
    print(a)
    print("Great choice")

except ValueError as v :
    print("HEy WhAt ThE HeLL you are doing")

else:
    print("I am inside else")