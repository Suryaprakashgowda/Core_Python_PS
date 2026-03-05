#map()
def add(num):
    return num+10
l=[]
i=0
while i<=4:
    num=int(input("Enter a number:"))
    l.insert(i,num)
    i=i+1
res=list(map(add,l))
print(res)