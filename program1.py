class Fan:
    def __init__(self):
        self.brand="usha"
        self.color="white"
        self.cost=3000
        self.wings=3
    def on(self):
        print("fan is on")
    def off(self):
        print("fan is off")
    def rotate(self):
        print("fan is rotating")
f1=Fan()
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.wings)
f1.on()
f1.off()
f1.rotate()
