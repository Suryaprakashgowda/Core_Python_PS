def outer():
    a=100
    print(a)
    print(b)
    def inner():
        b=200
        print(b)
    inner()
outer()