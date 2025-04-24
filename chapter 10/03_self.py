class Employee:
    language = "Python"
    salary = 390000

    def getinfo(self):  # Move this method inside the class and include 'self'
        print(f"The language is {self.language}, The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morining")
    
Kritesh = Employee()
Kritesh.greet()
Kritesh.getinfo()  # Call the method to display information