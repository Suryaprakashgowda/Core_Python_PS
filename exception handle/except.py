a=int(input("enter a number A:"))
b=int(input("enter a number B:"))
try:
    res=a/b # ZeroDivisionError: division by zero
    print(res)
except Exception as e:
    print("Error occurred:",e)
    print(f"Error occurred:{e}")
# finally:
#     print("The program will stop")
else:
    print("A values is :",a)
    print("B values is :",b)


