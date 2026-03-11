class Person:
    def __init__(self):
        self.__name=""
    def setter(self,name):
        self.__name=name
    def getter(self):
        return self.__name
p1=Person()
p1.setter("Surya")
res1=p1.getter()
print(res1)
