class plane:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is fly")
class passenger(plane):
    def landing(self):
        print("plane is landing")
class cargo(plane):
    def landing(self):
        print("cargo is takeoff")
class fighter(plane):
    def landing(self):
        print("fighter is landing")
p1=passenger()
c1=cargo()
f1=fighter()
def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.landing()
allowplane(p1)
allowplane(c1)
allowplane(f1)

print()