class complex():
    def __init__(self,i,r):
        self.i=i
        self.r=r

    def __add__(self,c2):
        return complex(self.r+c2.i,self.i+c2.i)
    
    def __str__(self):
        return (f"{self.r}r+{self.i}i")
    
c1=complex(1,2)
c2=complex(3,4)
print(c1+c1)