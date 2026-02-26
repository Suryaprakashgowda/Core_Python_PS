
# A=input("Enter yes if u r inserted card:")
# balance=10000
# if A=="yes":
#     pin=input("Enter the pin:")
#     if pin=="1234":
#         print("Pin correct")
#         print("select the language")
#         language=input("Enter the language:")
#         if language=="english":
#             print("Your English")
#             print("choose option 1- Balance enquiry")
#             print("choose option 2- Balance Whithdrawl")
#             option=input("Enter the option:")
#             if option=="1":
#                 print("Your Balance")
#                 print(balance)
#             elif option=="2":
#                 amount=input("Enter amount:")
#                 if amount=="3000":
#                     balance=input("Do u want check your balance?")
#                     if balance=="yes":
#                         print("Your Balance :'7000'")
#                     else:
#                         print("Thank you")
#
#     else:
#         print("Pin incorrect")
import time

print("Welcome to our bank atm")
print("Insert the card")
balance=10000
print("enter 1.yes 2.no")
card = input()
if card == "1":
    print("Enter a pin")
    pin = input()
    if pin=="1234":
        print("Select 1.english 2.kannada 3.hindi")
        language = input()
        if language == "1":
            print("Choose a choice 1.Balance enquiry 2.Withdraw amount")
            choice=input()
            if choice=="1":
                print("Your balance is",balance)
            elif choice=="2":
                print("Enter a amount withdrawal")
                amt=int(input())
                if amt<=balance:
                    print("your transaction is under process")
                    time.sleep(3)
                    if amt%100==0:
                        print("please collect our cash")
                        time.sleep(3)
                        print("enter our choice 1.check balance 2.no")
                        choice=input()
                        if choice=="1":
                            print("Your balance is",balance-amt)
                        else:
                            print("Visit again Thank you!...")
                    else:
                        print("enter a multiple of 100")
                else:
                    print("Insufficient Balance")
            else:
                print("incorrect choice")
        else:
            print("please select english only")
    else:
        print("Enter a correct password")
else:
    print("please insert a card")
