#closure
def out():
    print("Inside out")
    def inner():
        print("Inside inner")
    return inner

ref=out()
ref()

