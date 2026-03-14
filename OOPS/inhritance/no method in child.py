class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def hunt(self):
        print("Animal is hunting")
class Lion(Animal):
    pass
class Tiger(Animal):
    pass
class Fox(Animal):
    pass
l1=Lion()
l1.eat()
l1.sleep()
l1.hunt()
t1=Tiger()
t1.eat()
t1.sleep()
t1.hunt()
f1=Fox()
f1.eat()
f1.sleep()
f1.hunt()