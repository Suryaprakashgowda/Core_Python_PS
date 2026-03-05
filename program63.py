#implementation lambda function in map
l=[]
i=0
while i<=4:
    num=int(input("enter a number:"))
    l.insert(i,num)
    i=i+1
res=list(map(lambda num:num+10,l))
print(res)