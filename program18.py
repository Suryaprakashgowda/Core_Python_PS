class CALCULATOR: # with parameter and with return value
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def add(self,a,b):
        c=a+b
        return c
c1=CALCULATOR()
print(c1.color)
print(c1.brand)
x=10
y=20

res=c1.add(x,y)
print(res)

