class CALCULATOR: # no parameter and with return value
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def add(self):
        a=10
        b=20
        c=a+b
        return c
c1=CALCULATOR()
print(c1.color)
print(c1.brand)
res=c1.add()
print(res)

