class Animals():
    pass

class Pet(Animals):
    pass

class Dog(Pet):
    
    @staticmethod
    def bark():
        print("bow bow!")

a=Dog
a.bark()   