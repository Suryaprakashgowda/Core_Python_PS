str=input("enter a string")
print(str)
if str.isalpha():
    print("string contain only aplha")
elif str.isdigit():
    print("string contain only digits")
elif str.isalnum():
    print("string contain number and aplha")
else:
    print("other charter")