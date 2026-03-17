class A:
    def disp(self):
        print(" inisde A")
class B(A):
    def disp(self):
        print(" inisde B")
class C(B):
    def disp(self):
        print(" inisde C")
        B.disp(self)
        A.disp(self)
C1=C()
C1.disp()
# C1.disp()
# C1.disp()
