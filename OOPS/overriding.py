class a:
    def disp(self):
        print("inisde a")
class b(a):
    def disp(self):
        print("inisde b")
class c(b):
    def disp(self):
        print("inisde c")
c1=c()
c1.disp()
c1.disp()
c1.disp()