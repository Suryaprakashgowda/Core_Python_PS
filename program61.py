#implementaion of lambda function

l=[]
i=0
while i<=4:
    num=int(input("enter a number:"))
    l.append(num)
    i=i+1
res=list(filter(lambda num:num%2==0,l))
print(res)