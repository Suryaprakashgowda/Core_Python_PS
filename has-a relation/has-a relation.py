class Radio:
    def turnon(self,x):
        if x==1:
            print("Radio is on")
        else:
            print("Radio is off")
class Car:
    def __init__(self,min,max):
        self.cmin=min
        self.cmax=max
        self.r=Radio()
c1=Car(10,120)
print(c1.cmax)
print(c1.cmin)
c1.r.turnon(1)
c1.r.turnon(0)