class Dog:
    def __init__(self):
        self.bread="Husky"
    def __Bark(self):
        print("Dog is barking")
    def bak(self):
        #return self.__Bark()
        self.__Bark()
d1=Dog()
# d1.__Bark() o/p-error bcz private
d1.bak()
# res=d1.bak()
# print(res) #o/p-Dog is barking, None
