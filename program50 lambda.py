#lambda arguments:expression

#single argument and single expression only
lambda num:num*num
l=lambda num:num*num
res=l(5)
print(res)

#multiple argument can pass, but we can perform only single expression only in lambda
lambda a,b:a+b
s=lambda a,b:a+b
res=s(5,10)
print(res)