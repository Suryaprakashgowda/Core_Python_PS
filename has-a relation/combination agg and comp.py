class heart:
    def __init__(self,name):
        self.hname=name
    def HeartAttack(self):
        print("Heart is empty")
class cycle:
    def __init__(self,name):
        self.cname=name
    def buycycle(self):
        print("Cycle buuy")
class Person:
    def __init__(self,name):
        self.pname=name
        self.h=heart("empty")
        self.c=""
    def hasperson(self,p):
        self.c=p
p1=Person("my self")
print(p1.pname)
c1=cycle("my cycle")
p1.hasperson(c1)
p1.c.buycycle()
p1.h.HeartAttack()
print(p1.h.hname)
del p1
print(c1.cname)
c1.buycycle()



