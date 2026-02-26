#higher order function & first order function
def fun1():
    print("Inside fun1")
def fun2(ptr):
    print("Inside fun2")
    ptr()
    print("leaving fun2")
fun1()
fun2(fun1)
