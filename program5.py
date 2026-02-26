class Bike:
    def __init__(self):
        self.brand="RE"
        self.color="white"
        self.model=1990

    def start(self):
        print("bike is starting")
        print(self.color)
        print(self)
b1=Bike()
print(b1.brand)
print(b1.color)
print(b1.model)
b1.start()
print(b1)