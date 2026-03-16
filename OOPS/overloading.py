class a:
    def disp(self,a,b,c):
        print(a)
        print(b)
        print(c)
class b(a):
    def disp(self,a,b):

        print(a)
        print(b)
class c(b):
    def disp(self,a):
        print(a)
c1=c()
c1.disp(10)
c1.disp(10,20)
c1.disp(10,20,30)