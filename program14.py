class Farmer:
    r=2.5

    def __init__(self, p, t):
        self.principal = p
        self.time = t
    def loan(self):
            si = (self.principal * self.time *Farmer.r) / 100
            print(si)

f1 = Farmer(20000, 4)
f2 = Farmer(50000, 7)
f1.loan()
f2.loan()
print(Farmer.r)
