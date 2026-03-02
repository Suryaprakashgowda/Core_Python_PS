from math import pi
#pi=10
def outer():
    #pi=20
    def inner():
        #pi=30
        print(pi)
    inner()
outer() #if we not import math we will get for build in scope