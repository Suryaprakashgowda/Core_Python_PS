class Mobile:
    def __init__(self):
        self.brand="Nokia"
    def call(self):
        print("mobile is ringing")
    @staticmethod
    def charge():
        print("mobile is charging")
    @classmethod
    def hang(cls):
        print("mobile is hanging")
m1=Mobile()
print(m1.brand)
m1.call()
m1.charge() #not standard way for calling static and class method
m1.hang()
#standard  way
Mobile.hang()
Mobile.charge()

#Mobile.call() #bcz its is instance method #through an error