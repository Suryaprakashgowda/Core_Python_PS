class Hero:
    def __init__(self):
        self.name="Sudeep"
        self.age=51
        self.numOfMovies=54 #camel case
    def act(self):
        print("Sudeep is good actor")
h1=Hero()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()