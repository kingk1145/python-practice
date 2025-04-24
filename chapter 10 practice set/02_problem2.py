class Claculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")
        
    def squareroot(self):
        print(f"The square is {self.n**1/2}")

p=Claculator(4)
p.square()
p.cube()
p.squareroot()