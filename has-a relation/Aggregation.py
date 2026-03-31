class charger:
    def __init__(self,name):
        self.cname=name
    def getcharger(self):
        print("Charger is plugedin")
class mobile:
    def __init__(self,name):
        self.mname=name
        self.c=""

    def hascharger(self,p):
        self.c=p
m1=mobile("Iqoo")
c1=charger("cpin")
print(m1.mname)
m1.hascharger(c1)
print(m1.c.cname)
m1.c.getcharger()
del m1
print(c1.cname)
c1.getcharger()
