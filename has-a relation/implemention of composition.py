class os:
    def __init__(self):
        self.status=True
        print("os is ready")
    def getos(self):
        print("os is installing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=os()
        print("Mobile os is ready")
        print("with os is installed")
m1=Mobile("Nokia")
print(m1.mname)
print(m1.o.status)
m1.o.getos()
del m1
# print(m1.o.status) #error-NameError: name 'm1' is not defined