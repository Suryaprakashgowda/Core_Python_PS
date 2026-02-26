class Demo:
    def display(self,a=10,b=20,c=30):
        print(a)
        print(b)
        print(c)
d1=Demo()
x=11
y=22
z=33
d1.display() # it will not passing any parameters

# passing parameter ( it will change or override a b c )
d1.display(x,y,z)

#single parameter only one
d1.display(x) #IT WILL CHANGE only first value (staring variable example a )

#single parameter only but we changed to now to y
d1.display(y)

#single only
d1.display(z)

#double parameters passing , staring 2 formal parameters accepts values
d1.display(x,y)

# double
d1.display(y,z)

#keyword arguments
d1.display(b=z,a=y,c=x) # we assigning value directly we assiging which value to which variable to accept


#single assign
d1.display(c=y)