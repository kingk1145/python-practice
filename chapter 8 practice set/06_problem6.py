def inch_to_cms(inch):
    return inch * 2.54
n=int(input("Enter the length in inches: "))
print(f"The length in cm is {round(inch_to_cms(n),2)}") 
