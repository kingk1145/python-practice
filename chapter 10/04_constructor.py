class Employee:
    language = "Python"
    salary = 390000

    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        print("I am creating an object")
    def getinfo(self):
        print(f"The language is {self.language}, The salary is {self.salary}")
    
    def greet(self):
        print("Good morining")
    
Kritesh = Employee("kritesh","javascript",690000)
print(Kritesh.name,Kritesh.salary,Kritesh.language)

print(" ")

Anant=Employee("Anant","Python",83000)
print(Anant.name,Anant.language,Anant.salary)