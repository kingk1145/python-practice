from random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    
    def book(self,fro,to):
        print(f"The train is booked in train no: {self.trainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    def getfare(self,fro,to):
        print(f"The ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(22,345)}")

p=train(17263)
p.book("rampure", "delhi")
p.getfare("rampure", "delhi")
p.getstatus()