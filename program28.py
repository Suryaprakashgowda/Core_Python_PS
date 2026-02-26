# string reverse word
str="dog is drinking"
str1=str.split()
print(str)
print(str1)
rev=""
for i in str1:
    #rev=i+rev #it will give o/p without space
    rev=i+" "+rev
print(rev)
