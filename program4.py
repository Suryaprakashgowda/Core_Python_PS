# class Heroine:
#     def __init__(self):
#         self.name="Rukku"
#         self.age=27
#         self.numOfMovies=7
#     def act(self):
#         print("Rukku is Good actress")
# h1= Heroine()
# print(h1.name)
# print(h1.age)
# print(h1.numOfMovies)
# h1.act()
# h1.address="Karnataka" #Adding
# print(h1.address)
# h1.age=28
# print(h1.age) #update / modify4
# print(h1.numOfMovies) #before deleting numOfMovies
# del h1.numOfMovies
#print(h1.numOfMovies) # after deleting if we run we will get an error is numOfMovies is not defined

#example CAR program
class Car:
    def __init__(self):
        self.name="maruthi suzuki"
        self.color="white"
        self.model=2020
    def Buy(self):
        print("car is sold")
    def clean(self):
        print("car is clean")
c1=Car()
print(c1.name)
print(c1.model)
print(c1.color)
c1.Buy()
c1.clean()
