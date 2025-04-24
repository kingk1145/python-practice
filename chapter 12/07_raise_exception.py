a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

if(b==0 or a==0):
    raise ZeroDivisionError("Hey our program is not meant to be divide numbers by zero")
else:
    print(f"The dividion of a/b is {a/b}")