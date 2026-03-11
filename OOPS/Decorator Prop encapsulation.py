class Person:
    def __init__(self):
        self.__name=""
    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,value):
        self.__name=value
p1=Person()
p1.dataAccess="Surya"
res=p1.dataAccess
print(res)
# print(p1.dataAccess)