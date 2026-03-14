class plane:
    def takeoff(self):
        print("plane is take off")
    def fly(self):
        print("plane is fly")
    def land(self):
        print("plane is land")
class PassengerPlane(plane):
    def carry_p(self):
        print("plane is carrying p")
class CargoPlane(plane):
    def carry_g(self):
        print("plane is carrying goods")
class FighterPlane(plane):
    def carry_w(self):
        print("plane is carrying weapons")
p1=PassengerPlane()
c1=CargoPlane()
f1=FighterPlane()
p1.takeoff()
p1.fly()
p1.land()
p1.carry_p()
c1.takeoff()
c1.fly()
c1.land()
c1.carry_g()
f1.takeoff()
f1.fly()
f1.land()
f1.carry_w()

