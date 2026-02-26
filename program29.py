#pallindrome
str=input("enter a string:")
print(str)
rev=""
for i in str:
    rev=i+rev
print(rev)
if str==rev:
    print("its palindrome")
else:
    print("its not palindrome")