class TV:
    def __init__(self):
        self.name="samsung"
        self.cost=25000

    def display(self):
        self.color="black"
        print(self.color)
t1=TV()
print(t1.name)
print(t1.cost)
#print(t1.color) if we execute this we get error because its not stored in heap segment
t1.display()

print(t1.color)
t1.size=36
print(t1.size)
