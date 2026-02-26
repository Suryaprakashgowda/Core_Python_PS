def Outer():
    print("Inside Outer")
    def Inner():
        print("Inside Inner")
    Inner()
Outer()
#Inner() if we call this gets error because its inside function so we need to call inside the function

