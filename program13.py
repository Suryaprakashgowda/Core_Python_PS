class Farmer:
    def __init__(self,p,t,r):
        self.principal=p
        self.time=t
        self.rate=r
    def loan(self):
        si=(self.principal*self.time*self.rate)/100
        print(si)
f1=Farmer(20000,7,2.5)
f2=Farmer(50000,4,2.5)
f1.loan()
f2.loan()