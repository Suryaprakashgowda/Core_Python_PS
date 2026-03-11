def main():
    str="Pentagon"
    return str
def outer(ptr):
    print("inside outer")
    def inner():
        print("inside inner")
        res=ptr()
        ans=res.upper()
        print(ans)
        print("leaving outer")
    return inner
ref=outer(main)
ref()
