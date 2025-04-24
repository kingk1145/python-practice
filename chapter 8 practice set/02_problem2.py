def f_to_c(f):
    return 5*(f-32)/9

f=int(input("Enter the temperature in F: "))
c=5*(f-32)/9
print(f"{round(c,2)}°C")