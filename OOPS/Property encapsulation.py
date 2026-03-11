class Person:
    def __int__(self):
        self.__name=""

    def getter(self):
        return self.__name

    def setter(self,value):
        self.__name = value


    getset=property(getter,setter) #error-getset=property(setter,getter)
p1=Person()
p1.getset="Surya"
res=p1.getter()
print(res)