def main():
    print("inside main")
def outer(ptr):
    print("inside outer")
    def inner():
        print("inside inner")
        ptr()
        print("leaving outer")
    return inner
ref=outer(main)
ref()
